import os

from block_markdown import markdown_to_html_node


def extract_title(md):
    # list of individual lines
    lines = md.split('\n')

    for line in lines:
        if len(line) > 2 and line.startswith('#'):
            if line[1] != '#':
                return line[2:]
            
    raise ValueError('h1 header was not found.')


def convert_to_html_file(filename):
    html_extension = '.html'

    filename_split = filename.split('.', maxsplit=1)    # list: ['doc', '.file_extension']
    doc = filename_split[0]

    return doc + html_extension

def generate_pages_recursive(from_path, template_path, dst_path, basepath):
    src_content = os.listdir(from_path)
    
    for item in src_content:
        # item filepath inside the source folder from_path=(static_site_generator/content)
        item_from_filepath = os.path.join(from_path, item)
        # item filepath inside the destination folder dst_path=(static_site_generator/public)
        item_dst_filepath = os.path.join(dst_path, item)

        if os.path.isfile(item_from_filepath):
            item_dst_filepath = os.path.join(dst_path, convert_to_html_file(item))
            generate_page(item_from_filepath, template_path, item_dst_filepath, basepath)
        else:
            generate_pages_recursive(item_from_filepath, template_path, item_dst_filepath, basepath)


def generate_page(from_path, template_path, dst_path, basepath):
    print(f" * {from_path} --> {dst_path}\nUsing template: {template_path}\n")

    # use with open() to open a file, read it, and close it
    with open(from_path, 'r') as from_file:
        md_content = from_file.read()

    with open(template_path, 'r') as template_file:
        template_content = template_file.read()

    title = extract_title(md_content)
    node = markdown_to_html_node(md_content)    # node is a ParentNode 
    node_to_html = node.to_html()  # .to_html() converts node into html string

    # replace title and content with proper data 
    dst_content = template_content.replace("{{ Title }}", title)
    dst_content = dst_content.replace("{{ Content }}", node_to_html)

    # replace any instances of href="/ with href="{basepath}
    dst_content = dst_content.replace("href=\"/", f"href=\"{basepath}")
    # replace any instances of src="/ with src="{basepath}
    dst_content = dst_content.replace("src=\"/", f"src=\"{basepath}")


    # create filepath to make necessary directories
    dest_directory_filepath = os.path.dirname(dst_path)

    # validate new filepath
    if dest_directory_filepath != "":
        os.makedirs(dest_directory_filepath, exist_ok=True)

    # use with open() to open a file, write on it, and close it
    with open(dst_path, 'w') as dst_file:
        dst_file.write(dst_content)