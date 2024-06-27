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

img = cv2.imread("./5.jpg")
#img = draw_grid(img, size=250)

h, w = img.shape[:2]
#9660, 5000

sizes = {
        }

adp_bboxes = Bboxes(
    wages=BoundingBox(img,
					Bbox(
                    w/50,
					200,
					w/2-150,
					h/40)),
					
    withholding=BoundingBox(img,
					Bbox(
					w/2+w/50,
					200,
					w/2-150,
					h/40)),
					
    ss_wages=BoundingBox(img,
					Bbox(
					w/50,
					650,
					w/2-150,
					h/40)),
					
    ss_withholding=BoundingBox(img,
					Bbox(
					w/2+w/50,
					650,
					w/2-150,
					h/40)),
					
    med_wages=BoundingBox(img,
					Bbox(
					w/50,
					1050,
					w/2-150,
					h/40)),
					
    med_withholding=BoundingBox(img,
					 Bbox(
					w/2+w/50,
					 1050,
					 w/2-150,
					 h/40)),
					
    ein=BoundingBox(img,
					 Bbox(
					w/50,
					 3650,
					 w/2-150,
					 h/40)),
					
    ssn=BoundingBox(img,
					 Bbox(
					w/2+w/50,
					 3650,
					 w/2-150,
					 h/40)),
					
    ss_tips=BoundingBox(img,
					 Bbox(
					w/50,
					 4000,
					 w/2-150,
					 h/40)),
					
    nq_plans=BoundingBox(img,
					 Bbox(
					w/50,
					 4750,
					 w/2-150,
					 h/40)),
					
    allocated_tips=BoundingBox(img,
					 Bbox(
					w/2+w/50,
					 4000,
					 w/2-150,
					 h/40)),
					
    dependent_benefits=BoundingBox(img,
					 Bbox(
					w/2+w/50,
					4400,
					w/2-150,
					h/40)),
					
    code1=BoundingBox(img,
					 Bbox(
					w/2+w/20,
					 4740,
					 375,
					 h/40)),
					
    code1_amount=BoundingBox(img,
					 Bbox(
					w/2+w/4-w/10,
					 4750,
					 w/2-800,
					 h/40)),
					
    code2=BoundingBox(img,
					 Bbox(
					w/2+w/20,
					 5025,
					 375,
					 h/40)),
					
    code2_amount=BoundingBox(img,
					 Bbox(
					w/2+w/4-w/10,
					 5025,
					 w/2-800,
					 h/40)),
					
    code3=BoundingBox(img,
					 Bbox(
					w/2+w/20,
					 5300,
					 375,
					 h/40)),
					
    code3_amount=BoundingBox(img,
					 Bbox(
					w/2+w/4-w/10,
					 5300,
					 w/2-800,
					 h/40)),
					
    code4=BoundingBox(img,
					 Bbox(
					w/2+w/20,
					 5550,
					 375,
					 h/40)),
					
    code4_amount=BoundingBox(img,
					 Bbox(
					w/2+w/4-w/10,
					 5550,
					 w/2-800,
					 h/40)),
					
    statutory=BoundingBox(img,
					 Bbox(
					w/2+w/20,
					6000,
					400,
					h/100)),
					
    retirement=BoundingBox(img,
					 Bbox(
					w/2+w/8+w/18,
					6000,
					400,
					h/100)),
					
    sick_pay=BoundingBox(img,
					 Bbox(
					w/2+w/4+w/32,
					6000,
					 1000,
					h/100)),
					
    other=BoundingBox(img,
					 Bbox(
					w/50,
					 5200,
					 w/2-150,
					 h/10)),
					
    employer=BoundingBox(img,
					 Bbox(
					w/50,
					 2000,
					 w-150,
					 h/7.5)),
					
    employee=BoundingBox(img,
					 Bbox(
					w/100,
					 6400,
					 w-150,
					 h/10)),
					
    state=BoundingBox(img,
					 Bbox(
					w/50,
					7645,
					600,
					h/40)),
					
    state_id=BoundingBox(img,
					 Bbox(
					w/10+w/20+w/200,
					7650,
					1700,
					h/40)),
					
    state_wages=BoundingBox(img,
					 Bbox(
					2550,
					7650,
					2400,
					h/40)),
					
    state_tax=BoundingBox(img,
					 Bbox(
					w/50,
					8050,
					2400,
					h/40)),
					
)

timer = Timer("")
w2 = W2(img, adp_bboxes)
w2.read()
w2.draw()
#w2.print()
#w2.get_json()
timer.stop()
