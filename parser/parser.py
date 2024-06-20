import cv2
from preprocessor import converter, slicer, imageprocessor
from dev.timer import Timer
from dotenv import load_dotenv
from multiprocessing.dummy import Pool as ThreadPool
from matplotlib import pyplot as plt
#from ocr import ocr

load_dotenv()

def process_image(img, path):
    form = imageprocessor.FormImageProcessor(img)
    form.process(export=False)

    if form.state != 1:
        print(f"Unable to process: {path}")
        return

    img = form.get_image()
    s = slicer.FormSlicer(img)
    s.slice_form()
    s.export("export")

if __name__ == "__main__":

    timer = Timer("All")

    #pool = ThreadPool(8)
    #imgs, paths = converter.convert_files("./data/w2/adp")
    #pool.starmap(process_image, zip(imgs, paths))
    #pool.close()
    #pool.join()

    #form = ocr.FormOcr(directory)
    #print(form.form_type)
    #print(form.form_year)
    #form.print()
    timer.stop()
