import os
from tqdm import tqdm, notebook
from pathlib import Path

MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 400

full_paths = []
for dirpath, dirnames, filenames in tqdm(os.walk("repos")):
    dirpath = Path(dirpath)
    for f in filenames:
        full_path = dirpath / f
        full_paths.append(full_path)

with open("python_code_text.txt","a") as file:
    for fpath in notebook.tqdm(full_paths):
        with open(fpath, "r") as f:
            d = f.read()
            if 20 < len(d) <= MAX_CHAR_LENGTH:
                fd = d.replace("\n", "<N>")
                file.write(f"{fd} \n")
                break
            else:
                sd = d.split("\n\n")
                substring = ""
                for split in sd:
                    
