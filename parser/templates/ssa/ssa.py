import cv2
import numpy as np
import math
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(parent_dir)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(parent_dir)

from dev.timer import Timer
from templates.ssa import SSA, Bboxes
from bbox import BoundingBox, Bbox

def draw_grid(img, grid_shape, color=(0, 255, 0), thickness=1):
    h, w, _ = img.shape
    rows, cols = grid_shape
    dy, dx = h / rows, w / cols

    # draw vertical lines
    for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
        x = int(round(x))
        cv2.line(img, (x, 0), (x, h), color=color, thickness=thickness)

    # draw horizontal lines
    for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
        y = int(round(y))
        cv2.line(img, (0, y), (w, y), color=color, thickness=thickness)

    return img

img = cv2.imread("./export/14.jpg")
#img = draw_grid(img, (64, 64), (100,100,100), 2)

h, w = img.shape[:2]

w64 = w/64
h64 = h/64

ssa_boxes = Bboxes(
        year=BoundingBox(img, Bbox(w64*0.5, h64*0, w64*9, h64*5)),
        ssa=BoundingBox(img, Bbox(w64*43, h64*6.5, w64*20, h64*3)),
        benefits=BoundingBox(img, Bbox(w64*0.5, h64*11.5, w64*20, h64*3)),
        repaid=BoundingBox(img, Bbox(w64*22, h64*11.5, w64*20, h64*3)),
        net_benefits=BoundingBox(img, Bbox(w64*43, h64*11.5, w64*20, h64*3)),
        description=BoundingBox(img, Bbox(w64*0.5, h64*16.5, w64*31.5, h64*24)),
        withheld=BoundingBox(img, Bbox(w64*32.5, h64*40.5, w64*31, h64*5)),
)

timer = Timer("")
ssa = SSA(img, ssa_boxes)
ssa.read()
#ssa.draw()
ssa.print()
#ssa.get_json()
timer.stop()
