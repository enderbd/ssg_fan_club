import os
import shutil


def recursive_copy_static(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)

    for item in os.listdir(src_folder):
        item_path = os.path.join(src_folder, item)
        dest_path = os.path.join(dest_folder, item)
        print(f"  {item_path} -> {dest_path}")
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest_path)
        else:
            recursive_copy_static(item_path, dest_path)
