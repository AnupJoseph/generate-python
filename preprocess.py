from rich import print
from tqdm import tqdm,notebook

from pathlib import Path
import os

MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 400

full_paths = []
for dirpath, dirnames, filenames in tqdm(os.walk("repos")):
    dirpath = Path(dirpath)
    for f in filenames:
        full_path = dirpath / f
        full_paths.append(full_path)

with open("python_code_text.txt", "a") as file:
    for fpath in notebook.tqdm(full_paths):
        try:
            with open(fpath, "r") as f:
                d = f.read()
                fd = d.replace("\n", "<N>")
                if 20 < len(d) <= MAX_CHAR_LENGTH:
                    file.write(f"{fd} \n")
                    break
                else:
                    sd = fd.split("<N><N>")
                    substring = ""
                    for split in sd:
                        substring += split + "<N><N>"
                        if MIN_CHAR_LENGTH < len(substring) <= MAX_CHAR_LENGTH:
                            f.write(substring + "\n")
                            substring = ""
        except Exception as e:
            print(e)
