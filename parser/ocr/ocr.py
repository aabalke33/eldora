import pandas as pd
import re
import subprocess
import os
import numpy as np
import spacy
from multiprocessing.dummy import Pool as ThreadPool
from collections import Counter
from datetime import datetime

form_data = {
    'wages': [
        "w2", "wages", "wage", "employee", "employees", "employer", "employers",
        "tips", "other", "12a", "12b", "12c", "12d", "ein"
    ],
    'retirement': [
        "1099r", "retirement", "irr", "roth", "fatca", "distribution",
        "distributions", "ira", "sep", "simple", "recipient", "recipients",
        "payer", "payers", "gross"
    ],
    'interest': [
        "interest", "1099int", "int", "payer", "payers", "withdrawal",
        "recipient", "recipients", "savings", "treasury", "bond", "market"
        ]
}

class FormOcr:

    slices = []
    slice_data = []

    def __init__(self, directory) -> None:
        self.directory = directory
        self.recognize()

    def recognize(self):

        def initial_processing(file):
            path = os.path.join(self.directory, file)
            slice = SliceOcr(path)
            slice.recognize()
            self.slices.append(slice)

        pool = ThreadPool(16)
        files = os.listdir(self.directory)
        pool.map(initial_processing, files)
        pool.close()
        pool.join()

        self.get_general_info()

    def get_general_info(self):
        cleaned_words = []

        for slice in self.slices:
            for line in slice.data:
                for word in line.split():
                    cleaned_word = re.sub(r'[^a-zA-Z0-9]', '', word).lower()
                    cleaned_words.append(cleaned_word)

        parser = FormParser(cleaned_words)
        self.form_type = parser.get_type()
        self.form_year = parser.get_year()

    def print(self):
        for slice in self.slices:
            #print(slice.data)
            slice.parse()

class SliceOcr:

    def __init__(self, path) -> None:
        self.path = path

    def recognize(self, psm=6, lang="eng"):
        p = subprocess.run([
            "tesseract.exe",
            self.path,
            #out,
            "-",
            "-l",
            lang,
            "--psm",
            str(psm),
        ], capture_output=True, text=True)

        self.data = p.stdout.splitlines()

    def parse(self):
        parser = SliceParser(self.data)
        print("-------------------------------------")
        print("Key:\t", parser.key)
        print("Value:\t", parser.value)
        print("-------------------------------------")

class FormParser:
    def __init__(self, form_words):
        self.counter = Counter(form_words)

    def _count_matches(self, form_type_data) -> int:
        return sum({
            value: self.counter[value] for value in form_type_data}.values())

    def get_type(self):

        counts = dict() 

        for k, v in form_data.items():
            counts[k] = self._count_matches(v)

        max_key = max(counts, key=lambda k: (counts[k]))
        if counts[max_key] < 5:
            return None

        return max_key

    def get_year(self):
        this_year = datetime.now().year

        common_year, common_count = 0, 0

        for i in range(this_year-10, this_year):
            count = self._count_matches([str(i)])
            if count > common_count:
                common_count = count
                common_year = i

        if common_year == 0:
            return None

        return common_year

class SliceParser:

    key = None
    value = None

    def __init__(self, slice_lines) -> None:
        match len(slice_lines):
            case 1:
                self.parse_single_line(slice_lines)
            case 2:
                self.parse_two_lines(slice_lines)
            case 3 | 4:
                self.parse_multi_lines(slice_lines)

    def _line_is_dollar(self, line_words):
        return len(line_words) == 1 and self._is_dollar(line_words[0])

    def _is_dollar(self, word):
        pattern = r'^\d{1,3}(,\d{3})*(\.\d+)?$'
        return bool(re.fullmatch(pattern, word))

    # Will need to extend further
    def parse_single_line(self, slice_lines):
        return
#        line_words = slice_lines[0].split()
#
#        if len(line_words) == 1:
#            return
#
#        for i, word in enumerate(line_words):
#            if self._is_dollar(word):
#                self.key = line_words[0:i]
#                self.value = word
#                return

    # Will need to extend further
    def parse_two_lines(self, slice_lines):
        self.key = slice_lines[0]
        self.value = slice_lines[1]


    # Will need to extend further
    def parse_multi_lines(self, slice_lines):
        self.key = slice_lines[0]
        self.value = slice_lines[1:]
#
#        top_words = slice_lines[0].split()
#        if self._line_is_dollar(top_words):
#            self.value = slice_lines[0]
#            self.key = slice_lines[1:]
#            return
#
#        bottom_words = slice_lines[-1].split()
#        if self._line_is_dollar(bottom_words):
#            self.value = slice_lines[-1]
#            self.key = slice_lines[:-1]
#            return
