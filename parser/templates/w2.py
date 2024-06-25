import cv2
import json
from multiprocessing.dummy import Pool as ThreadPool
from dataclasses import dataclass, fields
from bbox import BoundingBox
import math
import re
from form import Form

def draw_grid(img, size=1000, color=(105, 200, 105), thickness=5):
    h, w, _ = img.shape

    count_h = math.floor(h/size)
    count_w = math.floor(w/size)

    for height in range(count_h):
        cv2.line(img, (0, height*size), (w, height*size), color=color, thickness=thickness)
    for width in range(count_w):
        cv2.line(img, (width*size, 0), (width*size, h), color=color, thickness=thickness)

    return img

@dataclass
class Bboxes():
    wages: BoundingBox
    withholding: BoundingBox
    ss_wages: BoundingBox
    ss_withholding: BoundingBox
    med_wages: BoundingBox
    med_withholding: BoundingBox
    ein: BoundingBox
    ssn: BoundingBox
    ss_tips: BoundingBox
    nq_plans: BoundingBox
    allocated_tips: BoundingBox
    dependent_benefits: BoundingBox
    code1: BoundingBox
    code1_amount: BoundingBox
    code2: BoundingBox
    code2_amount: BoundingBox
    code3: BoundingBox
    code3_amount: BoundingBox
    code4: BoundingBox
    code4_amount: BoundingBox
    statutory: BoundingBox
    retirement: BoundingBox
    sick_pay: BoundingBox
    other: BoundingBox
    employer: BoundingBox
    employee: BoundingBox
    state: BoundingBox
    state_id: BoundingBox
    state_wages: BoundingBox
    state_tax: BoundingBox

class W2(Form):
    def __init__(self, img, bboxes: Bboxes) -> None:
        self.img = img
        self.height, self.width = img.shape[:2]
        self.bboxes = bboxes
        self.data = dict()

    def _read_other(self, bbox): 
            lines = bbox.read(psm=6, user_pattern="multi_line").splitlines()

            other = dict()

            for line in lines:
                key, value = None, None
                for word in line.split():
                    if re.match("^[0-9.]", word):
                        value = float(word)
                        continue

                    key = word

                if key and value:
                    other[key] = str(value)

            return other

    def _read_personal(self, bbox):
        lines = bbox.read(psm=6, user_pattern="multi_line").splitlines()

        match len(lines):
            case 3:
                name = lines[0]
                street = lines[1]
                address = lines[2].split()

            case 4:
                if re.match('0-9',lines[1][0]):
                    name = lines[0]
                    street = ' '.join(lines[1:3])
                else:
                    name = lines[0:2]
                    street = ' '.join(lines[2])

                address = lines[3].split()
            case 5:
                if str(lines[-1][0:6]).lower().startswith("batch"):
                    if re.match('0-9',lines[1][0]):
                        name = lines[0]
                        street = ' '.join(lines[1:3])
                    else:
                        name = lines[0:2]
                        street = ' '.join(lines[2])

                    address = lines[3].split()
                else:
                    name = lines[0:2]
                    street = ' '.join(lines[2:4])
                    address = lines[4].split()
            case _:
                return None, None, None, None, None

        city = ' '.join(address[:-2])
        state = address[-2]
        zip = address[-1][0:5]
        return name, street, city, state, zip

    def _read_bbox(self, field):
        bbox = getattr(self.bboxes, field.name)

        match field.name:
            case "ein": 
                self.data[field.name] = bbox.read(user_pattern="ein")
            case "ssn":
                self.data[field.name] = bbox.read(user_pattern="ssn")
            case "state":
                self.data[field.name] = bbox.read(psm=8, user_pattern="state")
            case "code1" | "code2" | "code3" | "code4":
                self.data[field.name] = bbox.read(psm=8, user_pattern="code")
            case "statutory" | "retirement" | "sick_pay":
                self.data[field.name] = bbox.read(
                        user_pattern="checkbox", bool_threshold=230)
            case "other":
                self.data["other"] = self._read_other(bbox)
            case "employer" | "employee":
                name, street, city, state, zip = self._read_personal(bbox)
                self.data[f"{field.name}_name"] = name
                self.data[f"{field.name}_street"] = street
                self.data[f"{field.name}_city"] = city
                self.data[f"{field.name}_state"] = state
                self.data[f"{field.name}_zip"] = zip
            case "state_id":
                self.data[field.name] = bbox.read(user_pattern="single")
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

        cv2.namedWindow("W2", cv2.WINDOW_NORMAL)
        cv2.imshow("W2", img_draw)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def print(self):
        for k, v in self.data.items():
            if type(v) is dict:
                print(f'{k:>24}')
                for ka, va in v.items():
                    print(f'\t{ka:>24}',f'{va:>32}')
                continue

            print(f'{k:>24}',f'{v:>32}')

    def get_json(self):
        with open("test_nested.json", "w") as file:
            json.dump(self.data, file, indent=4, sort_keys=False)
