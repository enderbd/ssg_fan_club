import os

from markdown_blocks import extract_title, markdown_to_html_node


def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            dest_file = dest_path.replace(".md", ".html")
            generate_page(item_path, template_path, dest_file, basepath)

        else:
            generate_page_recursive(item_path, template_path, dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    print(
        f"  --- generating page from {from_path} to {dest_path} using {template_path}"
    )
    markdown_content = ""
    with open(from_path, "r") as f:
        markdown_content = f.read()
    template_html = ""
    with open(template_path, "r") as f:
        template_html = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    html_title = extract_title(markdown_content)
    template_html = template_html.replace("{{ Title }}", html_title).replace(
        "{{ Content }}", html_content
    )
    template_html = template_html.replace('href="/', 'href="' + basepath)
    template_html = template_html.replace('src="/', 'src="' + basepath)

    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as out:
        out.write(template_html)
