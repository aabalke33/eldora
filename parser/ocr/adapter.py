import re
from ocr.const import state_abbreviations

class W2Adapter:

    def __init__(self, key, value_lines) -> None:
        self.key = key
        self.value_lines = value_lines
        self.dictionary = dict()

        match self.key:
            case "c":
                values = self.adapt_personal()
                if values is None:
                    return

                self.dictionary = {
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

                self.dictionary = {
                    "employee_name": values[0],
                    "employee_street": values[1],
                    "employee_city": values[2],
                    "employee_state": values[3],
                    "employee_zip": values[4] 
                }
            case ("1" | "2" | "3" | "4" | "5" |
                "6" | "7" | "8" | "9" | "10" | "11"):

                value = self.adapt_number()
                if value is None:
                    return

                self.dictionary = {self.key: value}

    def get_dictionary(self):
        return self.dictionary

    def adapt_number(self):
        if len(self.value_lines) > 1:
            print("Too Many Lines")
            return

        value = self.value_lines[0]
        #May need to make sure extra numbers do not collide
        amount = float(re.sub(r'[^0-9.]', '', value))

        if amount > 500_000:
            return None

        return int(round(amount, 0))

    def adapt_personal(self):
        match len(self.value_lines):
            case 3:
                name = str(self.value_lines[0]).upper()
                street = str(self.value_lines[1]).upper()
                address_two = self.value_lines[2].split()
            case 4:
                # idx of split between name and street
                # Assumes Street starts with number ie 1221
                split_idx = 1
                if self.value_lines[2][0].isnumeric():
                    split_idx = 2

                name = str(' '.join(self.value_lines[0:split_idx])).upper()
                street = str(' '.join(self.value_lines[split_idx:3])).upper()
                address_two = self.value_lines[3].split()
            case 5:
                print("FIVE LINES IN EMPLOYER OR EMPLOYEE DATA, PROBABLY ERROR")
                return
                name = str(self.value_lines[:2]).upper()
                street = str(self.value_lines[2:4]).upper()
                address_two = self.value_lines[4].split()

            case _:
                print("Line Number incorrect")
                return

        if len(address_two) < 3:
            return

        zip_code = int(address_two[-1][:5])
        state = str(address_two[-2][:2]).upper()
        city = ' '.join(address_two[:-2]).upper()

        if state not in state_abbreviations:
            state = "CO"

        return [name, street, city, state, zip_code]

#    def adapt_checkboxes(self):
#        if len(self.value_lines) != 1:
#            return
#
#    def adapt_other(self):
#
#        for line in self.value_lines:
#            for word in line.split():
#                if str(word).isdigit():
#


            
