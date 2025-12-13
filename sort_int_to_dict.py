
import os
from glob import glob


def main():
    data_dir = "./data"
    save_dir = "./result"

    path_list = glob(f"{data_dir}/*.png")
    str_list = sorted([f"{str(x)}.png" for x in range(len(path_list))])

    for i, old_path in enumerate(path_list):
        new_path = str_list[i]
        os.rename(old_path, f"{save_dir}/{new_path}")


if __name__ == "__main__":
    main()

