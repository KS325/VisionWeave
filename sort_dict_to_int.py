
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def rename_pngs_in_folder(folder_path):
    files = os.listdir(folder_path)
    png_files = [f for f in files if f.endswith(".png") and f[:-4].isdigit()]
    png_files.sort(key=lambda x: int(x[:-4]))

    for file_name in png_files:
        number = int(file_name[:-4])
        new_name = f"{str(number).zfill(7)}.png"
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        if old_path != new_path:
            os.rename(old_path, new_path)

def main():
    root = tk.Tk()
    root.withdraw()

    messagebox.showinfo("Select Directory", "Select TOP directory.")
    base_dir = filedialog.askdirectory(title="Select TOP directory")
    if not base_dir:
        print("NO Directory selected")
        return

    for dir_path, _, _ in os.walk(base_dir):
        rename_pngs_in_folder(dir_path)
    # base_folder = folder_paths
    # subfolders = [os.path.join(base_folder, f) for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]

    # if not subfolders:
    #     print("NO Sub directory selected")
    #     return
    
    # for folder in subfolders:
    #     rename_pngs_in_folder(folder)
    
    messagebox.showinfo("Completed!", "All files has renamed.")

if __name__ == "__main__":
    main()



