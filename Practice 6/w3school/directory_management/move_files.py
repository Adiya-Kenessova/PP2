import shutil 
import os


os.mkdir("folder")
with open ("file.txt","x") as f:
    pass 

# 1. Переместить один файл
shutil.move("file.txt", "folder/file.txt")

# 2. Переименовать файл
with open ("old_name.txt","x") as f:
    pass 
shutil.move("old_name.txt", "new_name.txt")

# 3. Переместить все файлы из одной папки в другую
source = "source_folder"
destination = "dest_folder"

os.mkdir("source_folder")
os.mkdir("dest_folder")
with open(os.path.join(source, "file1.txt"), "w") as f:
    f.write("Текст файла 1")
with open(os.path.join(source, "file2.json"), "w") as f:
    f.write("Текст файла 2")
with open(os.path.join(source, "file3.txt"), "w") as f:
    f.write("Текст файла 3")

for file in os.listdir(source):
        full_path = os.path.join(source, file)
        
        if os.path.isfile(full_path):
            shutil.move(full_path, destination)

# 4. Переместить только .txt файлы
with open(os.path.join(source, "a.txt"), "w") as f:
    f.write("Текст 1")
with open(os.path.join(source, "b.doc"), "w") as f:
    f.write("Текст 2")
with open(os.path.join(source, "c.txt"), "w") as f:
    f.write("Текст 3")

for file in os.listdir(source):
    if file.endswith(".txt"):
        shutil.move(os.path.join(source, file), destination)





import os
import shutil
from pathlib import Path


# CREATE DIR + FILE
os.mkdir("folder")                     # create folder
with open("file.txt", "x") as f:      # create file
    pass


# MOVE FILE
shutil.move("file.txt", "folder/file.txt")  # move file


# RENAME FILE
with open("old.txt", "x") as f:
    pass
shutil.move("old.txt", "new.txt")     # rename


# COPY FILE
shutil.copy("new.txt", "copy.txt")    # copy file


# DELETE FILE / DIR
os.remove("copy.txt")                 # delete file
os.rmdir("folder")                    # delete empty folder
# shutil.rmtree("folder")             # delete non-empty folder


# LIST FILES
os.listdir(".")                       # list files


# MOVE ALL FILES
src = "src"
dst = "dst"
os.mkdir(src)
os.mkdir(dst)

for f in os.listdir(src):
    path = os.path.join(src, f)
    if os.path.isfile(path):
        shutil.move(path, dst)


# MOVE ONLY .txt
for f in os.listdir(src):
    if f.endswith(".txt"):
        shutil.move(os.path.join(src, f), dst)


# PATHLIB BASIC
p = Path("file.txt")

p.exists()        # check exists
p.rename("new.txt")  # rename/move
p.unlink()        # delete file

Path("new_folder").mkdir()  # create folder
list(Path(".").iterdir())   # list files


# PATHLIB MOVE ALL FILES
src = Path("src2")
dst = Path("dst2")

src.mkdir()
dst.mkdir()

for f in src.iterdir():
    if f.is_file():
        f.rename(dst / f.name)  # move


# PATHLIB FILTER .txt
for f in src.iterdir():
    if f.suffix == ".txt":
        f.rename(dst / f.name)
