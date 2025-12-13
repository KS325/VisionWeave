
import os


def remove_files(path_list):
    for _, path in enumerate(path_list):
        os.remove(path)
    pass


