from recognizer import recognizer as rec
from converter import converter as con
from dev.timer import Timer
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    timer = Timer("All")

    imgs = con.convert_files("./data")

    for i, img in enumerate(imgs):
        if i:
            form = rec.Form(img)
            form.process(True)
            form.export(f"./temp/{i}.jpg")

    



    timer.stop()
