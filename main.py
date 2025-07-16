
from src.imageset.imageset import Imageset
from src.loader.loader import ImageLoader
from src.editor.editor import ImageEditor

data_dir = "./data"
myimageset = Imageset()
myimageloader = ImageLoader("./result", myimageset)

raw_paths = myimageset.make_paths(data_dir)
myimageeditor = ImageEditor(raw_paths, myimageloader)
myimageeditor.trimming()



