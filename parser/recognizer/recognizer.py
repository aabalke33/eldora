import cv2
import numpy as np
from scipy import ndimage
# Future: may want to split if multiple forms on one page

class Form:
    def __init__(self, img) -> None:
        #self.img = cv2.imread(path)
        self.img = img
        if self.img is None:
            print(f"Image could not be loaded.")
            exit(0)

    def export(self, path):
        cv2.imwrite(path, self.img)

    def view(self):
        cv2.imshow('Form', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def process(self, export: bool = False):
        if export: self.export("./1_original.jpg")
        self.preprocess()
        if export: self.export("./2_preprocess.jpg")
        self.crop_image()
        if export: self.export("./3_cropped.jpg")
        self.correct_skew()
        if export: self.export("./4_deskew.jpg")

    def preprocess(self):
        grayscale = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        binary = cv2.adaptiveThreshold(
            grayscale, 
            255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 
            11,
            25
        )

        self.img = binary

    def crop_image(self):
        contours, _ = cv2.findContours(
            self.img,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if not len(contours):
            print("No contours found")
            exit()

        def remove_excess_contours():
            height, width = self.img.shape[:2]
            margin = 1
        
            filtered_contours = []
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                
                if (x > margin and
                    y > margin and
                    (x + w) < (width - margin) and
                    (y + h) < (height - margin)):

                    if w * h < 0.9 * width * height:
                        filtered_contours.append(contour)
        
            return filtered_contours

        contours = remove_excess_contours()

        if not len(contours):
            print("No contours found")
            exit()

        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        self.img = self.img[y:y+h, x:x+w]

    def correct_skew(self, delta=1, limit=5):
        def determine_score(arr, angle):
            data = ndimage.rotate(arr, angle, reshape=False, order=0)
            histogram = np.sum(data, axis=1, dtype=float)
            score = np.sum((histogram[1:] - histogram[:-1]) ** 2, dtype=float)
            return histogram, score

        thresh = cv2.threshold(self.img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1] 

        scores = []
        angles = np.arange(-limit, limit + delta, delta)
        for angle in angles:
            _, score = determine_score(thresh, angle)
            scores.append(score)

        best_angle = angles[scores.index(max(scores))]

        (h, w) = self.img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, best_angle, 1.0)
        corrected = cv2.warpAffine(self.img, M, (w, h), flags=cv2.INTER_CUBIC, \
                borderMode=cv2.BORDER_REPLICATE)

        self.img = corrected
