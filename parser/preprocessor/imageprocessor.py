import cv2
import numpy as np
from scipy import ndimage
# Future: may want to split if multiple forms on one page

class FormImageProcessor:
    def __init__(self, img) -> None:
        #self.img = cv2.imread(path)
        self.img = img
        self.state = 0

        if self.img is None:
            print(f"Image could not be loaded.")
            exit(0)

    def get_image(self):
        return self.img

    def export(self, path):
        cv2.imwrite(path, self.img)

    def view(self, img=None):

        cv2.namedWindow("Form", cv2.WINDOW_NORMAL)
        if img is None:
            img = self.img
        cv2.imshow('Form', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def process(self, export: bool = False):
        if export: self.export("./1_original.jpg")
        self.resize()
        if export: self.export("./2_resized.jpg")
        self.preprocess()
        if export: self.export("./3_preprocess.jpg")
        self.crop_image()
        if export: self.export("./4_cropped.jpg")
        self.correct_skew()
        if export: self.export("./6_deskew.jpg")

        if self.state == 0:
            self.state = 1

    def resize(self, ratio=3.0, img=None, interpolation=cv2.INTER_CUBIC, immutable=False):

        if img is None:
            height, width = self.img.shape[:2]
        else:
            height, width = img.shape[:2]

        image = cv2.resize(
                self.img,
                (int(width * ratio), int(height * ratio)),
                interpolation=interpolation
                )
        if immutable:
            return image
        
        self.img = image

    def preprocess(self):
        grayscale = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        binary = cv2.adaptiveThreshold(
            grayscale, 
            255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 
            33,
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

                    if w * h < 0.95 * width * height:
                        filtered_contours.append(contour)
        
            return filtered_contours

        contours = remove_excess_contours()

        if not len(contours):
            print("No contours found")
            exit()

        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        self.bbox = largest_contour
        self.contour_ratio = w / h
#
#        #temp_image = self.img[y:y+h, x:x+w]
#        #self.img = temp_image
#        size_limit = 6000
#
#        if max(w, h) > size_limit:
#            self.state = -1
#        #    ratio = size_limit / max(w, h)
#        #    self.resize(ratio, temp_image, interpolation=cv2.INTER_AREA)
#        #    self.erosion()
#        #    self.crop_image()

    def erosion(self):
        size = 2
        kernel = np.ones((size, size), np.uint8)
        #self.img = cv2.dilate(self.img, kernel, iterations=1)
        self.img = cv2.erode(self.img, kernel, iterations=1)

    def correct_skew(self, delta=1, limit=10):
        def determine_score(arr, angle):
            data = ndimage.rotate(arr, angle, reshape=False, order=0)
            histogram = np.sum(data, axis=1, dtype=float)
            score = np.sum((histogram[1:] - histogram[:-1]) ** 2, dtype=float)
            return histogram, score
       
        img = self.img
        if len(self.img.shape) == 3:
            img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + 
                cv2.THRESH_OTSU)[1] 

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

    def correct_perspective(self):
        rect = cv2.minAreaRect(self.bbox)
        #rect = cv2.boundingRect(self.bbox)

        # Get the four points of the rectangle
        box = cv2.boxPoints(rect)
        #box = np.int32(box)
        #temp = self.img
        #cv2.rectangle(temp, rect, (0,0,255), 10)
        #cv2.drawContours(temp,[box],0,(0,0,255),10)
        #self.view(temp)
        # Order the points in a consistent manner: top-left, top-right, bottom-right, bottom-left
        def order_points(pts):
            rect = np.zeros((4, 2), dtype="float32")

            # the top-left point will have the smallest sum, whereas
            # the bottom-right point will have the largest sum
            s = pts.sum(axis=1)
            rect[0] = pts[np.argmin(s)]
            rect[2] = pts[np.argmax(s)]

            # the top-right point will have the smallest difference,
            # whereas the bottom-left will have the largest difference
            diff = np.diff(pts, axis=1)
            rect[1] = pts[np.argmin(diff)]
            rect[3] = pts[np.argmax(diff)]

            return rect

        ordered_box = order_points(box)
        # Get the width and height of the original image
        orig_height, orig_width = self.img.shape[:2]

        # Define the destination points to fit within the original image dimensions
        dst_pts = np.array([
            [0, 0],
            [orig_width - 1, 0],
            [orig_width - 1, orig_height - 1],
            [0, orig_height - 1]], dtype="float32")

        # Get the perspective transform matrix
        M = cv2.getPerspectiveTransform(ordered_box, dst_pts)

        # Apply the perspective transformation
        self.img = cv2.warpPerspective(self.img, M, (orig_width, orig_height))
