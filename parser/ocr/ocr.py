import pandas as pd
import re
import subprocess
import os
import numpy as np
import spacy
from autocorrect import Speller
from multiprocessing.dummy import Pool as ThreadPool

# Lookup form data to find best match
from collections import Counter

w2 = [
	"w2",
	"wages",
	"wage",
	"employee",
	"employees",
	"employer",
	"employers",
	"tips",
	"other",
	"12a",
	"12b",
	"12c",
	"12d",
	"ein"
]

retirement = [
	"1099r",
	"retirement",
	"irr",
	"roth",
	"fatca",
	"distribution",
	"distributions",
	"ira",
	"sep",
	"simple",
	"recipient",
	"recipients",
	"payer",
	"payers",
	"gross",
]

class FormInfoParser:
    def __init__(self, form_words):
        self.counter = Counter(form_words)

    def _count_matches(self, form_type_data) -> int:
        return sum({
            value: self.counter[value] for value in form_type_data}.values())

    def get_type(self):

        counts = {
            'w2': self._count_matches(w2),
            '1099r': self._count_matches(retirement),
        }

        return max(counts, key=lambda k: (counts[k]))

class FormOcr:

    form_type = None
    slices = []

    def __init__(self, directory) -> None:
        self.directory = directory

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

        self.get_type()

    def get_type(self):
        cleaned_words = []

        for slice in self.slices:
            for line in slice.data:
                words = line.split()
                for word in words:
                    cleaned_word = re.sub(r'[^a-zA-Z0-9]', '', word).lower()
                    cleaned_words.append(cleaned_word)

        parser = FormInfoParser(cleaned_words)
        self.form_type = parser.get_type()

    def get_year(self):
        for slice in self.slices:
            if "2022" in slice.data:
                print("2022")
                self.form_year = 2022
            if "2023" in slice.data:
                print("2023")
                self.form_year = 2023

    def print(self):
        for slice in self.slices:
            print(slice.data)

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

        #self.field, self.value = self.parse()

    def parse(self):
#       
#        match len(self.data):
#            case 2 | 3 | 4:
#                print("----------------------------")
#                print("Key", self.data[0])
#                print("Value", self.data[1:])
#                print("----------------------------")
#                return self.data[0], self.data[1:]
##            case 3:
##                return self.data[0], self.data[1:]
##            case 4:
##                return self.data[0], self.data[1:]
#            case _:
#                print("----------------------------")
#                print("No Pattern")
#                print("----------------------------")
#                return "", ""
#
#
#
#        print("split len", len(self.data))
        return "", ""
