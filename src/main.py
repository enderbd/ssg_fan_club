import os
import shutil

from copy_static import recursive_copy_static
from generate_page import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Recursive copy static to public")
    recursive_copy_static(dir_path_static, dir_path_public)

    print("Generating page ...")
    generate_page_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
    )


if __name__ == "__main__":
    main()
