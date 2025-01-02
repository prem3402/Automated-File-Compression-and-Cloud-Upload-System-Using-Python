import os
import zipfile
import zipfile


def compress_files(input_file="/Users/prem/Desktop/", outfile="test2.zip"):
    try:
        with zipfile.ZipFile(outfile, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
            if os.path.isdir(input_file):
                for root, _, files in os.walk(input_file):
                    for file in files:
                        full_path = os.path.join(root, file)
                        arcname = os.path.relpath(full_path, start=input_file)
                        zf.write(full_path, arcname=arcname)
    except:
        print("Error in compressing files")


compress_files()
