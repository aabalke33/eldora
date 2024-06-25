import cv2
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(parent_dir)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(parent_dir)

from dev.timer import Timer
from templates.w2 import W2, Bboxes
from bbox import BoundingBox, Bbox

img = cv2.imread("./temp.jpg")
#img = draw_grid(img, size=250)

h, w = img.shape[:2]

adp_bboxes = Bboxes(
    wages=BoundingBox(img, Bbox(100, 200, w/2-150, 240)),
    withholding=BoundingBox(img, Bbox(w/2+100, 200, w/2-150, 240)),
    ss_wages=BoundingBox(img, Bbox(100, 650, w/2-150, 240)),
    ss_withholding=BoundingBox(img, Bbox(w/2+100, 650, w/2-150, 240)),
    med_wages=BoundingBox(img, Bbox(100, 1050, w/2-150, 240)),
    med_withholding=BoundingBox(img, Bbox(w/2+100, 1050, w/2-150, 240)),
    ein=BoundingBox(img, Bbox(100, 3650, w/2-150, 240)),
    ssn=BoundingBox(img, Bbox(w/2+100, 3650, w/2-150, 240)),
    ss_tips=BoundingBox(img, Bbox(100, 4000, w/2-150, 240)),
    nq_plans=BoundingBox(img, Bbox(100, 4750, w/2-150, 240)),
    allocated_tips=BoundingBox(img, Bbox(w/2+100, 4000, w/2-150, 240)),
    dependent_benefits=BoundingBox(img, Bbox(w/2+100,4400,w/2-150,240)),
    code1=BoundingBox(img, Bbox(w/2+250, 4740, 375, 245)),
    code1_amount=BoundingBox(img, Bbox(w/2+750, 4750, w/2-800, 240)),
    code2=BoundingBox(img, Bbox(w/2+250, 5025, 375, 240)),
    code2_amount=BoundingBox(img, Bbox(w/2+750, 5025, w/2-800, 240)),
    code3=BoundingBox(img, Bbox(w/2+250, 5300, 375, 240)),
    code3_amount=BoundingBox(img, Bbox(w/2+750, 5300, w/2-800, 240)),
    code4=BoundingBox(img, Bbox(w/2+250, 5550, 375, 240)),
    code4_amount=BoundingBox(img, Bbox(w/2+750, 5550, w/2-800, 240)),
    statutory=BoundingBox(img, Bbox(w/2+250,6000,400,100)),
    retirement=BoundingBox(img, Bbox(w/2+900,6000,400,100)),
    sick_pay=BoundingBox(img, Bbox(w/2+1400,6000, 1000,100)),
    other=BoundingBox(img, Bbox(100, 5200, w/2-150, 1000)),
    employer=BoundingBox(img, Bbox(100, 2000, w-150, 1250)),
    employee=BoundingBox(img, Bbox(50, 6400, w-150, 1000)),
    state=BoundingBox(img, Bbox(100,7645,600,240)),
    state_id=BoundingBox(img, Bbox(775,7650,1700,240)),
    state_wages=BoundingBox(img, Bbox(2550,7650,2400,240)),
    state_tax=BoundingBox(img, Bbox(100,8050,2400,240)),
)

timer = Timer("")
w2 = W2(img, adp_bboxes)
w2.read()
#w2.draw()
w2.print()
#w2.get_json()
timer.stop()
