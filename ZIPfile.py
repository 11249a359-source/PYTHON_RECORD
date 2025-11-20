import os
import shutil
from datetime import datetime

def zip_folder(folder_name, add_timestamp=True):
    cwd = os.getcwd()
    folder_path = os.path.join(cwd, folder_name)

    if not os.path.isdir(folder_path):
        raise FileNotFoundError(f"Folder '{folder_name}' not found in {cwd}")

    if add_timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.join(cwd, f"{folder_name}_backup_{timestamp}")
    else:
        base_name = os.path.join(cwd, f"{folder_name}_backup")

    archive_path = shutil.make_archive(base_name, 'zip', folder_path)
    return archive_path


if __name__ == "__main__":
    try:
        folder = input("Enter the folder name to backup (in current directory): ").strip()
        if not folder:
            print("No folder name entered. Exiting.")
        else:
            zip_path = zip_folder(folder, add_timestamp=True)
            print(f"\nBackup created successfully:\n{zip_path}")

    except FileNotFoundError as fnf:
        print(f"Error: {fnf}")

    except PermissionError:
        print("Error: Permission denied. Check folder/file permissions.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
