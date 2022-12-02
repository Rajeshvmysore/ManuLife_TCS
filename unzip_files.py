import os
import shutil
import zipfile

if not os.path.exists("Extracted_files"):
    os.makedirs("Extracted_files")
path1=os.getcwd()
for file in os.listdir(path1):
    # print(file)
    if file.endswith(".zip"):
        my_dir = r"Extracted_files"
        # print(file)
        with zipfile.ZipFile(file) as zip_file:
            for files in zip_file.namelist():
                filename = os.path.basename(files)
                if not filename:
                    continue
                source = zip_file.open(files)
                # print(source)
                target = open(os.path.join(my_dir, filename), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)