
from tqdm import tqdm
import numpy as np
from src.loader.loader import ImageLoader
from src.utils.params import cal_size


class ImageEditor():
    def __init__(self, img_paths, imageloader: ImageLoader):
        self.img_paths = img_paths
        self.imageloader = imageloader
        pass

    def trimming(self, ratio="hakugin", shift=17, save_start=0):
        for i, path in tqdm(enumerate(self.img_paths)):
            img_raw = self.imageloader.load_image(path)
            H, W, _ = img_raw.shape
            # trimm_size = [int(W * np.sqrt(2)), W]
            trimm_size = cal_size([H, W], W, ratio)
            img_trimm = trimm(img_raw, [H, W], trimm_size, shift)
            self.imageloader.save_image(img_trimm, f"{save_start + i}.png")
        print(trimm_size)

        return


def trimm(img_raw, default_size, trimm_size: list, shift):
    H_center, W_center = [x//2 for x in default_size]
    img_trimm = img_raw[H_center - trimm_size[0]//2 - shift : H_center + trimm_size[0]//2 - shift,
                        W_center - trimm_size[1]//2 : W_center + trimm_size[1]//2,
                          :]

    return img_trimm

