import cv2
import re
import os
import subprocess
import tempfile
from collections import namedtuple
Bbox = namedtuple("Bbox", ["x", "y", "w", "h"])

class BoundingBox:
    def __init__(self, img, name, bbox: Bbox, keywords) -> None:
        self.img = img[bbox.y:bbox.y + bbox.h, bbox.x:bbox.x + bbox.w]
        self.name = name
        self.bbox = bbox
        self.keywords = keywords

    def draw(self, img, color=(0,0,255), thickness=30):
        x, y, w, h = self.bbox
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)

    def read(self, psm=6, lang="eng", user_pattern="number"):

        temp_name = tempfile.mktemp(prefix='tess_')
        input_file_name = temp_name + os.extsep + "jpg"
        cv2.imwrite(input_file_name, self.img)

        args = [
            "tesseract.exe",
            input_file_name,
            "-",
            "-l",
            lang,
            "--psm",
            str(psm),
            "--oem",
            "2",
        ]

        match user_pattern:
            case "number":
                args.append("--user-patterns")
                args.append('./templates/number.user-patterns')
            case "ein":
                args.append("--user-patterns")
                args.append('./templates/ein.user-patterns')
            case "ssn":
                args.append("--user-patterns")
                args.append('./templates/ssn.user-patterns')

        p = subprocess.run(args, capture_output=True, text=True)

        match user_pattern:
            case "number":
                output = re.sub("[^0-9.]", "", p.stdout)
            case "ein" | "ssn":
                output = re.sub("[^-0-9]", "", p.stdout)
            case _:
                output = p.stdout

        return output
