import re
import subprocess
from ocr.const import key_data, StatusCode

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
