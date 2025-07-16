
import cv2
import os
from src.imageset.imageset import Imageset

class ImageLoader():
    def __init__(self, save_dir, imageset: Imageset):
        os.makedirs(save_dir, exist_ok=True)
        self.save_dir = save_dir
        self.imageset = imageset
        pass

    def load_image(self, img_path):
        img = cv2.imread(img_path)

        return img

    def save_image(self, img, file_name):
        cv2.imwrite(f"{self.save_dir}/{file_name}", img)

        pass


