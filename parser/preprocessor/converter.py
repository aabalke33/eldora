from matplotlib.pyplot import imread
from pdf2image import convert_from_path
import os
import cv2
import numpy as np

def convert_files(directory: str):

    imgs = []
    paths = []

    for file in os.listdir(directory):

        source_path = f"{directory}/{file}"

        if not os.path.isfile(source_path):
            print(f"File {file} does not exist")
            continue

        if file.endswith(".jpg") or file.endswith(".png"):
            imgs.append(cv2.imread(source_path))
            paths.append(source_path)
            continue

        if file.endswith(".pdf"): 
            convert_pdf(source_path, imgs, paths)

    return imgs, paths

def convert_pdf(source_path, imgs, paths):

    poppler = os.environ['POPPLER_PATH']

    pages = convert_from_path(
            source_path,
            poppler_path=poppler
            )

    for i, page in enumerate(pages):
        img = np.array(page)
        img = img[..., (2, 1, 0)]
        imgs.append(img)
        paths.append(f"Page {i+1} of {source_path}")
