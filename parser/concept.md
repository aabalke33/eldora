# Parser Concept


Realized I have to define the bounding boxes to make it work.
Ocr and slicer no longer work.

Biggest problem is tesseract has trouble breaking down tables

Steps
1. Use ML to Classify form type (ie. W2 Form type A, type B etc)
    May not need to depending on Tesseract
2. Use template of how to chop up Type A form to chop image up
3. From chopped up image extract individual values (ie. Wages)
    May not need to depending on Tesseract
4. Append Indiviual Values to Json file


OpenCV, Tesseract


Need to flip 90 degree images
May need to handle multiple forms per scan

DevMap:

1. Hone in Tesseract
2. Parse Tesseract Data and convert to json


Classifier may not be necessary, specifying locations in ocr may not be necessary


Resources:
https://towardsdatascience.com/pre-processing-in-ocr-fc231c6035a7
https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
https://stackoverflow.com/questions/59660933/how-to-de-skew-a-text-image-and-retrieve-the-new-bounding-box-of-that-image-pyth
https://stackoverflow.com/questions/61832964/how-to-convert-pdf-into-image-readable-by-opencv-python
