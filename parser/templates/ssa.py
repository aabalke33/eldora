import cv2
import json
from multiprocessing.dummy import Pool as ThreadPool
from dataclasses import dataclass, fields
from bbox import BoundingBox, fix_currency_string
import re
from form import Form

@dataclass
class Bboxes():
	year: BoundingBox
	ssa: BoundingBox
	benefits: BoundingBox
	repaid: BoundingBox
	net_benefits: BoundingBox
	description: BoundingBox
	withheld: BoundingBox

class SSA(Form):
    def __init__(self, img, bboxes: Bboxes) -> None:
        self.img = img
        self.height, self.width = img.shape[:2]
        self.bboxes = bboxes
        self.data = dict()

    def _read_description(self, bbox):
        lines = bbox.read(psm=6, user_pattern="multi_line").splitlines()
        
        for line in lines:
            if line == "":
                lines.remove(line)

        match len(lines):
            case 5:
                s = lines[2].split()[-1]
                amount = re.sub("[^0-9.]", "", s)
                premiums = float(fix_currency_string(amount))
                return premiums
            case 7:
                premiums = 0
                for line in [lines[2], lines[4]]:
                    s = lines[2].split()[-1]
                    amount = re.sub("[^0-9.]", "", s)
                    premiums = premiums + float(fix_currency_string(amount))
                return premiums

        return None

    def _read_bbox(self, field):
        bbox = getattr(self.bboxes, field.name)

        match field.name:
            case "ssn":
                self.data[field.name] = bbox.read(user_pattern="ssn")
            case "description":
                value = self._read_description(bbox)
                if value is not None:
                    self.data["medicare_premiums"] = value
            case _:
                self.data[field.name] = bbox.read()

    def read(self):
        pool = ThreadPool(16)
        pool.starmap(
                self._read_bbox,
                [(field,) for field in fields(self.bboxes)]
                )
        pool.close()
        pool.join()

    def draw(self):

        img_draw = self.img

        for field in fields(self.bboxes):
            bbox = getattr(self.bboxes, field.name)
            bbox.draw(img_draw)

        cv2.namedWindow("SSA", cv2.WINDOW_NORMAL)
        cv2.imshow("SSA", img_draw)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def print(self):
        for k, v in self.data.items():
            print(f'{k:>24}',f'{v}')

    def get_json(self):
        with open("test_nested.json", "w") as file:
            json.dump(self.data, file, indent=4, sort_keys=False)
