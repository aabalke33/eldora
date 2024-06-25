import cv2
import re
import os
import subprocess
import tempfile
from collections import namedtuple
import numpy as np

Bbox = namedtuple("Bbox", ["x", "y", "w", "h"])

class BoundingBox:
    def __init__(self, img, bbox: Bbox) -> None:
        
        x = int(bbox.x)
        y = int(bbox.y)
        w = int(bbox.w)
        h = int(bbox.h)

        self.img = img[y:y + h, x:x + w]
        self.bbox = Bbox(x, y, w, h)

    def draw(self, img, color=(0,0,255), thickness=30):
        x, y, w, h = self.bbox

        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)

    def read(self, psm=3, lang="eng", user_pattern="number", bool_threshold=240):

        if user_pattern == "checkbox":
            avg_row = np.average(self.img, axis=0)
            avg = np.average(avg_row, axis=0)[0]
            if avg > bool_threshold:
                return False
            
            return True

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
                args.append('./templates/patterns/number.user-patterns')
            case "ein":
                args.append("--user-patterns")
                args.append('./templates/patterns/ein.user-patterns')
            case "ssn":
                args.append("--user-patterns")
                args.append('./templates/patterns/ssn.user-patterns')
            case "code":
                args.append("--user-patterns")
                args.append('./templates/patterns/code.user-patterns')
            case "state":
                args.append("--user-patterns")
                args.append('./templates/patterns/state.user-patterns')
            case "checkbox":
                args.append("--user-patterns")
                args.append('./templates/patterns/checkbox.user-patterns')

        p = subprocess.run(args, capture_output=True, text=True)

        match user_pattern:
            case "number":
                output = re.sub("[^0-9.]", "", p.stdout)
            case "ein" | "ssn":
                output = re.sub("[^0-9]", "", p.stdout)
            case "code" | "state":
                output = re.sub("[^A-Z]", "", p.stdout)
            case "checkbox":
                output = re.sub("[^X]", "", p.stdout)
            case "other":
                output = re.sub("[^A-Z0-9a-z. \n\r]", "", p.stdout)
            case "single":
                output = re.sub("[\n]", "", p.stdout)
            case _:
                output = p.stdout

        return output
