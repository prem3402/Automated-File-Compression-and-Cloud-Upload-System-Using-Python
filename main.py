import os
import zipfile
import datetime


def compress_files(input_paths, output_zip_name):
    try:
        with zipfile.ZipFile(
            output_zip_name, mode="w", compression=zipfile.ZIP_DEFLATED
        ) as zf:
            for path in input_paths:
                if not os.path.exists(path):
                    print(f"Path does not exist: {path}")
                    continue

                base_folder = os.path.basename(os.path.normpath(path))

                if os.path.isdir(path):
                    for root, _, files in os.walk(path):
                        for file in files:
                            full_path = os.path.join(root, file)

                            arcname = os.path.join(
                                base_folder, os.path.relpath(full_path, start=path)
                            )
                            zf.write(full_path, arcname=arcname)
                else:

                    arcname = os.path.join(base_folder, os.path.basename(path))
                    zf.write(path, arcname=arcname)
            # need to add logic to delete the files and folders after compressing
        print(f"Files successfully compressed into {output_zip_name}")
    except Exception as e:
        print(f"Error in compressing files: {e}")


input_paths = ["/Users/prem/Desktop", "/Users/prem/Downloads"]
current_date = datetime.datetime.now().strftime("%d-%m-%Y")
output_zip_name = f"backup_{current_date}.zip"
compress_files(input_paths, output_zip_name)
