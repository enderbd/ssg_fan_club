import os
import shutil
import sys

from copy_static import recursive_copy_static
from generate_page import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Recursive copy static to public")
    recursive_copy_static(dir_path_static, dir_path_public)

    print("Generating page ...")
    generate_page_recursive(dir_path_content, template_path, dir_path_public, basepath)


if __name__ == "__main__":
    main()
