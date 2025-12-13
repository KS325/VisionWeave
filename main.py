
import argparse

from src.imageset.imageset import Imageset
from src.loader.loader import ImageLoader
from src.editor.editor import ImageEditor
from src.utils.remover import remove_files

def main(extension: str, ratio: str, shift:int, start:int, num_dir: int, delete: bool, rename: bool):
    if num_dir:
        for i in range(num_dir):
            data_dir = f"./data/dir_{i + 1}"
            myimageset = Imageset()
            myimageloader = ImageLoader(f"./result/dir_{i + 1}", myimageset)

            raw_paths = myimageset.make_paths(data_dir, extension=extension)
            myimageeditor = ImageEditor(raw_paths, myimageloader)
            if rename:
                myimageeditor.rename(save_start=start)
            else:
                myimageeditor.trimming(ratio=ratio, shift=shift, save_start=start)
            # 古いスマホは shift = 0 でいいかも
            # "hakugin": 17
            # "ougon", -80

            if delete:
                remove_files(raw_paths)
    else:
        data_dir = f"./data"
        myimageset = Imageset()
        myimageloader = ImageLoader(f"./result", myimageset)

        raw_paths = myimageset.make_paths(dir_path=data_dir, extension=extension)
        myimageeditor = ImageEditor(raw_paths, myimageloader)
        if rename:
            myimageeditor.rename(save_start=start)
        else:
            myimageeditor.trimming(ratio=ratio, shift=shift, save_start=start)
        # shift = 17, 0, -163
        # "hakugin": 17
        # "ougon", -80

        if delete:
            remove_files(raw_paths)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--delete", action="store_true", help="Enable deletion of raw image files")
    parser.add_argument("--num_dir", type=int, default=0, help="Directory number to process (default: 0)")
    parser.add_argument("--start", type=int, default=0, help="Directory number to process (default: 0)")
    parser.add_argument("--shift", type=int, default=-163, help="Directory number to process (default: 0)")
    parser.add_argument("--ratio", type=str, default="hakugin", help="Directory number to process (default: 0)")
    parser.add_argument("--rename", action="store_true", help="Enable deletion of raw image files")
    parser.add_argument("--extension", type=str, default=".png", help="Directory number to process (default: 0)")
    args = parser.parse_args()

    main(
        extension=args.extension, 
        ratio=args.ratio, 
        shift=args.shift, 
        start=args.start, 
        num_dir=args.num_dir, 
        delete=args.delete, 
        rename=args.rename
    )

