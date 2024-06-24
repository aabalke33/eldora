import cv2
import re
import os
import sys
import subprocess
import tempfile
from collections import namedtuple

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(parent_dir)

from preprocessor import converter, slicer, imageprocessor

img = cv2.imread("./temp.jpg")
h, w = img.shape[:2]
half_w = int(w/2)
h_1 = 425

#box1 = BoundingBox(img, "1", Bbox(100, 200, half_w-150, 240), "")
#box2 = BoundingBox(img, "3", Bbox(100, 650, half_w-150, 240), "")
#box3 = BoundingBox(img, "5", Bbox(100, 1050, half_w-150, 240), "")
#box4 = BoundingBox(img, "2", Bbox(half_w+100, 200, half_w-150, 240), "")
#box5 = BoundingBox(img, "4", Bbox(half_w+100, 650, half_w-150, 240), "")
#box6 = BoundingBox(img, "6", Bbox(half_w+100, 1050, half_w-150, 240), "")
#boxein = BoundingBox(img, "ein", Bbox(100, 3650, half_w-150, 240), "")
boxssn = BoundingBox(img, "ssn", Bbox(half_w+100, 3650, half_w-150, 240), "")
#box7 = BoundingBox(img, "7", Bbox(100, 4000, half_w-150, 240), "")
#box11 = BoundingBox(img, "11", Bbox(100, 4750, half_w-150, 240), "")

#print(box1.name, "\t", box1.read(psm=3))
#print(box2.name, "\t", box2.read(psm=3))
#print(box3.name, "\t", box3.read(psm=3))
#print(box4.name, "\t", box4.read(psm=3))
#print(box5.name, "\t", box5.read(psm=3))
#print(box6.name, "\t", box6.read(psm=3))
#print(box7.name, "\t", box7.read(psm=3))
#print(boxein.name, "\t", boxein.read(psm=3, user_pattern="ein"))
print(boxssn.name, "\t", boxssn.read(psm=3, user_pattern="ssn"))

#box1.draw(img)
#box2.draw(img)
#box3.draw(img)
#box4.draw(img)
#box5.draw(img)
#box6.draw(img)
#box7.draw(img)
#boxein.draw(img)
boxssn.draw(img)
#box11.draw(img)

cv2.namedWindow("a", cv2.WINDOW_NORMAL)
cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
