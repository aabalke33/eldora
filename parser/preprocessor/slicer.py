import numpy as np
import cv2
import math
import uuid
import os

class FormSlicer:
    def __init__(self, img):
        self.img = img
        self.width = self.img.shape[0]
        self.height = self.img.shape[1]
        self.uuid = uuid.uuid4()

    def get_location(self):
        return self.location

    def export(self, location):

        path = os.path.join(location, str(self.uuid))
        os.mkdir(path)

        if self.box_images is None:
            cv2.imwrite(f'{path}/full.jpg', self.img)
        else:
            for i, box_image in enumerate(self.box_images):
                cv2.imwrite(f'{path}/slice_{i}.jpg', box_image)

        self.location = path

    def view(self):
        if self.box_images is None:
            cv2.imshow(f'Image', self.img)
        else:
            for i, box_image in enumerate(self.box_images):
                cv2.imshow(f'Box {i}', box_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def slice_form(self, sharpness=10, hierachy=cv2.RETR_EXTERNAL):

        border_image = self._get_borders(sharpness)
        self.box_images, box_bounding = self._get_boxes(border_image, hierachy)

        if len(self.box_images) in [0, 1] or self.box_images is None:
            new_sharpness = math.floor(sharpness/2)
            if new_sharpness:
                self.slice_form(sharpness=new_sharpness)
            else:
                self.slice_form(sharpness=10, hierachy=cv2.RETR_TREE)
            return

        if self.box_images is None:
            print("Final Contour Count: 0")
        else:
            print(f"Final Contour Count: {len(self.box_images)}")

    def _get_borders(self, sharpness):

        if len(self.img.shape) == 2:
            self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2RGB)

        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 255)

        contours, _ = cv2.findContours(
                edges,
                cv2.RETR_LIST,
                cv2.CHAIN_APPROX_SIMPLE
                )

        filtered_contours = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 20000:
                filtered_contours.append(contour)

        output_border = np.zeros((self.width, self.height, 3), np.uint8)
        cv2.drawContours(
                output_border,
                filtered_contours,
                -1,
                (255,255,255),
                sharpness
                )

        return output_border

    def _filter_contours(self, contours, hierarchy, image_width, image_height):

        min_size = 40
        max_ratio = 20
        max_percentage = 0.9

        filtered_contours, filtered_hierarchy = [], []
        for i, contour in enumerate(contours):
            _, _, w, h = cv2.boundingRect(contour)
            ratio = w/h

            if w < min_size or h < min_size:
                continue
            if ratio > max_ratio or ratio < 1/max_ratio:
                continue
            if (w > image_width*max_percentage and h > image_height*max_percentage):
                continue

            filtered_contours.append(contour)
            filtered_hierarchy.append(hierarchy[0][i])

        return filtered_contours, filtered_hierarchy

    def _is_contour_within(self, contour1, contour2, tolerance=0):
        x1, y1, w1, h1 = cv2.boundingRect(contour1)
        x2, y2, w2, h2 = cv2.boundingRect(contour2)
        return (x1 > x2 - tolerance and
                y1 > y2 - tolerance and 
                (x1 + w1) < (x2 + w2 + tolerance) and 
                (y1 + h1) < (y2 + h2 + tolerance))

    def _get_boxes(self, border_image, hierachy):
        gray = cv2.cvtColor(border_image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        contours, hierarchy = cv2.findContours(edges, hierachy, cv2.CHAIN_APPROX_SIMPLE)

        box_images, box_bounding = [], []

        filtered_contours, filtered_hierarchy = self._filter_contours(
                contours, hierarchy, self.width, self.height
                )

        final_contours =[]
        for i, contour in enumerate(filtered_contours):
    #        if hierachy == cv2.RETR_TREE and filtered_hierarchy[i][2] == -1:
    #            continue

            has_nested = False
            is_nested = False
            for j, contour2 in enumerate(contours):
                if i != j:
                    if self._is_contour_within(contour, contour2):
                        is_nested = True
                    if self._is_contour_within(contour2, contour):
                        has_nested = True

            if is_nested or not has_nested:
                final_contours.append(contour)

        for i, contour in enumerate(final_contours):
            x, y, w, h = cv2.boundingRect(contour)
            box_image = self.img[y:y+h, x:x+w]
            box_images.append(box_image)
            box_bounding.append([x, y, w, h])

        return box_images, box_bounding
