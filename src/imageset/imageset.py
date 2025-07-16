
from glob import glob
import cv2


class Imageset():
    def __init__(self, ):
        pass

    def make_paths(self, dir_path, extension=".png"):
        path_list = glob(f"{dir_path}/*{extension}")
        return path_list
