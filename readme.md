# Eldora: Tax Data Entry Software

Eldora is a data entry software created to scan, and parse PDF tax documentation
to enter into Drake Tax Software.

## Parsing

Eldora uses OCR and AI to read data from tax documentation, including W2 and other
income forms. This data it then exported as a JSON file, to be used later.

## Data Entry

After parsing, Eldora uses autohotkey to next enter the data into Drake Tax Software.
It does this by taking the json data and converting it into a .ahk script


