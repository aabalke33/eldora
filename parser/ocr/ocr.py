import re
import subprocess
import os
from multiprocessing.dummy import Pool as ThreadPool
from collections import Counter
from datetime import datetime
from typing import List
from ocr.const import form_data, key_data, valid_ein_prefixes, StatusCode, state_abbreviations

class Slice:

    key = None
    value = None
    
    _key = None
    _value = None

    def __init__(self, path) -> None:
        self.path = path
        self.status = StatusCode.INITIATED

    def recognize(self, psm=6, lang="eng"):
        p = subprocess.run([
            "tesseract.exe",
            self.path,
            "-",
            "-l",
            lang,
            "--psm",
            str(psm),
        ], capture_output=True, text=True)

        self.lines = p.stdout.splitlines()

    def parse(self, form_type):
        if len(self.lines) < 2:
            self.status = StatusCode.FAILED
            return

        filtered_lines = []
        for line in self.lines:
            temp = self._filter_string(line)
            if len(temp):
                filtered_lines.append(temp)

        self._key = filtered_lines[0]
        self._value = filtered_lines[1:]
        self.form_type = form_type

    def print(self):
        print("---------------------------------------")
        match self.status:
            case StatusCode.COMPLETED:
                print("Key:   ", self.key)
                print("Value: ", self.value)
            case StatusCode.INITIATED:
                print("Key:   Data unparsed")
                print("Value: Data unparsed")
            case _:
                print("Key:   None")
                print("Value: None")

    def _filter_string(self, input):

        # Keep only A-Z, 0-9, periods and spaces
        pattern = r'[^a-zA-Z0-9.\* ]'
        limited = re.sub(pattern, '', input).lower()

        # Keep only periods followed by 0-9 (financial numbers)
        filtered_string = re.sub(r'\.(?!\d)', '', limited)

        #Remove extra whitespace
        return re.sub(r'\s+', ' ', filtered_string).strip()

    def sanitize(self):

        if self._key is None or self._value is None:
            return

        form = key_data[self.form_type]
        scores = {key: 0 for key in form.keys()}
        words = self._key.split()

        if len(words) > 20:
            return

        for word in words: 
            for k, v in form.items():
                for sub_v in v:
                    if word == sub_v:
                        scores[k] = scores[k] + 1

        for k, v in scores.items():
            if v > len(words):
                scores[k] = -1

        max_key = max(scores, key=lambda k: (scores[k]))

        if scores[max_key] > len(words):
            return
        if scores[max_key] < int(len(words)*0.5):
            return
        if not scores[max_key]:
            return

        self.key = max_key
        self.value = self._value
        self.status = StatusCode.COMPLETED

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
        for _, slice in enumerate(self.slices):
                slice.parse(self.form_type)
                slice.sanitize()

    def print(self):

        print("Type: ", self.form_type)
        print("Year: ", self.form_year)
        print("EIN:  ", self.ein)

        for slice in self.slices:
            if slice.status == StatusCode.COMPLETED:
                slice.print()


class W2Adapter:

    def __init__(self, key, value_lines) -> None:
        self.key = key
        self.value_lines = value_lines

        match self.key:
            case "c":
                values = self.adapt_personal()
                if values is None:
                    return

                d = {
                    "employer_name": values[0],
                    "employer_street": values[1],
                    "employer_city": values[2],
                    "employer_state": values[3],
                    "employer_zip": values[4] 
                }
            case "e/f":
                values = self.adapt_personal()
                if values is None:
                    return

                d = {
                    "employee_name": values[0],
                    "employee_street": values[1],
                    "employee_city": values[2],
                    "employee_state": values[3],
                    "employee_zip": values[4] 
                }



    def adapt_number(self):
        if len(self.value_lines) > 1:
            print("Too Many Lines")
            return

        value = self.value_lines[0]
        #May need to make sure extra numbers do not collide
        amount = float(re.sub(r'[^0-9.]', '', value))
        return round(amount, 0)

    def adapt_personal(self):
        # will need to be able to process 4 lines
        if len(self.value_lines) not in [3]:
            print("Line Number incorrect")
            return

        name = str(self.value_lines[0]).upper()
        address = str(self.value_lines[1]).upper()
        address_two = self.value_lines[2].split()

        if len(address_two) < 3:
            return

        zip_code = int(address_two[-1][:5])
        state = str(address_two[-2][:2]).upper()
        city = ' '.join(address_two[:-2]).upper()

        if state not in state_abbreviations:
            state = "CO"

        return [name, address, city, state, zip_code]
