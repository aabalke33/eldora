from preprocessor import converter, slicer, imageprocessor
from dev.timer import Timer
from dotenv import load_dotenv
from multiprocessing.dummy import Pool as ThreadPool
from ocr import ocr

load_dotenv()

def process_image(img):

    form = imageprocessor.FormImageProcessor(img)
    form.process(export=False)
    img = form.get_image()
    s = slicer.FormSlicer(img)
    s.slice_form()
    s.export("export")
    slice_directory = s.get_location()

if __name__ == "__main__":

    timer = Timer("All")

    pool = ThreadPool(8)
    imgs = converter.convert_files("./data")
    pool.map(process_image, imgs)
    pool.close()
    pool.join()


    timer.stop()
