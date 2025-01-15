import os
import zipfile
import datetime
from smb.SMBConnection import SMBConnection
import logging


def compress_files(input_paths, output_zip_name):
    logging.info(f"Compressing files into {output_zip_name}")
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

        logging.info(f"Files successfully compressed into {output_zip_name}")

        for path in input_paths:
            if os.path.isdir(path):
                # Remove files inside the directory
                for root, _, files in os.walk(path, topdown=False):
                    for file in files:
                        full_path = os.path.join(root, file)
                        try:
                            os.remove(full_path)
                            logging.info(f"Removed file: {full_path}")
                        except Exception as e:
                            logging.error(f"Error removing file {full_path}: {e}")

                try:

                    for root, dirs, _ in os.walk(path, topdown=False):
                        for dir in dirs:
                            dir_path = os.path.join(root, dir)
                            try:
                                os.rmdir(dir_path)
                                logging.info(f"Removed empty directory: {dir_path}")
                            except Exception as e:
                                logging.error(
                                    f"Error removing directory {dir_path}: {e}"
                                )
                except Exception as e:
                    logging.error(f"Error removing directory {path}: {e}")
            else:
                try:
                    os.remove(path)
                    logging.info(f"Removed file: {path}")
                except Exception as e:
                    logging.error(f"Error removing file {path}: {e}")

    except Exception as e:
        logging.error(f"Error in compressing files: {e}")


def upload_to_windows_share(
    file_path,
    remote_host,
    share_name,
    remote_path,
    user_name,
    user_password,
    host_machine_name,
):
    logging.info(f"Uploading {file_path} to {remote_host}")
    try:

        if not os.path.isfile(file_path):
            logging.error(f"File does not exist: {file_path}")
            return

        conn = SMBConnection(
            user_name,
            user_password,
            "local_machine",
            host_machine_name,
            use_ntlm_v2=True,
        )

        if not conn.connect(remote_host, 139):
            logging.error(f"Failed to connect to {remote_host}")
            return

        with open(file_path, "rb") as file_obj:
            file_name = os.path.basename(file_path)
            remote_full_path = os.path.join(remote_path, file_name).replace("\\", "/")
            conn.storeFile(share_name, remote_full_path, file_obj)

        logging.info(
            f"Uploaded {file_path} to {remote_host}\\{share_name}\\{remote_path}"
        )

        conn.close()
        os.remove(file_path)
    except Exception as e:
        logging.error(f"Error uploading {file_path} to {remote_host}: {e}")


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    input_paths = ["/Users/prem/Desktop", "/Users/prem/Downloads"]
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    output_zip_name = f"backup_{current_date}.zip"
    file_to_upload = f"backup_{current_date}.zip"

    user_name = "premachars96@gmail.com"
    user_password = "Premkumar593402!"

    remote_computer = "192.168.0.143"
    shared_folder = "d"
    destination_path = "macbook/backup"
    host_machine_name = "Desktop-vboln0f"

    compress_files(input_paths, output_zip_name)

    upload_to_windows_share(
        file_to_upload,
        remote_computer,
        shared_folder,
        destination_path,
        user_name,
        user_password,
        host_machine_name,
    )
