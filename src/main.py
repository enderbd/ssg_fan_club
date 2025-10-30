import os
import shutil

from copy_static import recursive_copy_static

dir_path_static = "./static"
dir_path_public = "./public"


def main():
    #    delete_folder_content("./public")
    print("Deleting public directory !")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Recursive copy static to public")
    recursive_copy_static(dir_path_static, dir_path_public)


if __name__ == "__main__":
    main()
