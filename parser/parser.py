import cv2
from preprocessor import converter, slicer, imageprocessor
from dev.timer import Timer
from dotenv import load_dotenv
from multiprocessing.dummy import Pool as ThreadPool
from matplotlib import pyplot as plt
from ocr import ocr
from temp import directory
import numpy as np

load_dotenv()

def process_image(i, img, path):
    form = imageprocessor.FormImageProcessor(img)
    form.preprocess()
    form.crop_image()
    form.correct_perspective()
    form.correct_skew()
    img = form.get_image()
    contour_ratio = form.contour_ratio

    w = 5000
    h = w / contour_ratio

    img = cv2.resize(
            img,
            (int(w), int(h)),
            interpolation=cv2.INTER_CUBIC
            )

    #img2 = form.get_image()
    #h, w = img2.shape[:2]
    #ratio = 5000 / w
    #form.resize(ratio)

    #form.view()

#    img = form.get_image()
#    if img is None:
#        return

    #if form.state != 1:
    #    print(f"Unable to process: {path}")
    #    return
    
    cv2.imwrite(f"./export/{i}.jpg", img)
    #img = form.get_image()
    #s = slicer.FormSlicer(img)
    #s.slice_form()
    #s.export("export")

if __name__ == "__main__":

    timer = Timer("All")

    #pool = ThreadPool(8)
    imgs, paths = converter.convert_files("./data/ssa")
    print("Here")
    #pool.starmap(process_image, zip(i, imgs, paths))
    #pool.close()
    #pool.join()

    #for i, img in enumerate(imgs):
    #    process_image(i, img, "")

    #img = cv2.imread(path)
    #process_image(img, "")

    # Fix Slicer
    #form = ocr.Ocr(directory)
    #form.parse()
    #form.print()
    timer.stop()
