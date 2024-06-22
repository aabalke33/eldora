import re
import os
from multiprocessing.dummy import Pool as ThreadPool
from collections import Counter
from datetime import datetime
from typing import List
from ocr.const import form_data, valid_ein_prefixes, StatusCode
from ocr.slice import Slice
from ocr.adapter import W2Adapter
import json

class Ocr:

    def __init__(self, directory) -> None:
        self.slices: List[Slice] = []
        self.directory = directory
        self.ein = None

        def initial_processing(file):
            path = os.path.join(self.directory, file)
            slice = Slice(path)
            slice.recognize()
            self.slices.append(slice)

        pool = ThreadPool(16)
        files = os.listdir(self.directory)
        pool.map(initial_processing, files)
        pool.close()
        pool.join()

        self.get_general_info()

    def _count_matches(self, form_type_data) -> int:
        return sum({
            value: self.counter[value] for value in form_type_data}.values())

    def _get_type(self):

        counts = dict() 

        for k, v in form_data.items():
            counts[k] = self._count_matches(v)

        max_key = max(counts, key=lambda k: (counts[k]))
        if counts[max_key] < 5:
            return None

        self.form_type = max_key

    def _get_year(self):
        this_year = datetime.now().year

        common_year, common_count = 0, 0

        for i in range(this_year-10, this_year):
            count = self._count_matches([str(i)])
            if count > common_count:
                common_count = count
                common_year = i

        if common_year:
            self.form_year = common_year
            return

        self.form_year = None

    def _get_ein(self, words):
        pattern = re.compile(r'\d{2}-\d{7}')

        matches = []
        for word in words:
            if pattern.match(word):
                matches.append(word)

        if len(matches) == 1:
            self.ein = matches[0]
            return

        for match in matches:
            if int(match[:2]) in valid_ein_prefixes:
                self.ein = match
                return

        self.status = StatusCode.FAILED

    def get_general_info(self):

        cleaned_words = []
        for slice in self.slices:
            for line in slice.lines:
                for word in line.split():
                    cleaned_word = re.sub(r'[^a-zA-Z0-9\-]', '', word).lower()
                    cleaned_words.append(cleaned_word)

        self.counter = Counter(cleaned_words)
        self._get_ein(cleaned_words)
        self._get_type()
        self._get_year()

    def parse(self):

        self.final = dict()

        for _, slice in enumerate(self.slices):
                slice.parse(self.form_type)
                slice.sanitize()
                adapter = W2Adapter(slice.key, slice.value)
                self.final = {**self.final, **adapter.get_dictionary()}

    def print(self):


        print("Type: ", self.form_type)
        print("Year: ", self.form_year)
        print("EIN:  ", self.ein)

        if self.final is None:
            for slice in self.slices:
                if slice.status == StatusCode.COMPLETED:
                    slice.print()

            return

        print(json.dumps(self.final, indent=4))
