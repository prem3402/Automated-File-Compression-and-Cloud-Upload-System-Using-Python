import os
import zipfile


def compress_files(input_paths, outfile="test6.zip"):
    try:
        with zipfile.ZipFile(outfile, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
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

        print(f"Files successfully compressed into {outfile}")
    except Exception as e:
        print(f"Error in compressing files: {e}")


input_paths = ["/Users/prem/Desktop", "/Users/prem/Downloads"]
compress_files(input_paths)
