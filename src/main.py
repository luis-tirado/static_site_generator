import os
import shutil

from copydirectory import copy_files
from content_generator import generate_pages_recursive


def main():
    # static directory
    static_folder_filepath = "/home/luist/workspace/github.com/luis-tirado/static_site_generator/static"

    # template filepath
    template_filepath = "/home/luist/workspace/github.com/luis-tirado/static_site_generator/template.html"

    # source directory
    source_folder_filepath = "/home/luist/workspace/github.com/luis-tirado/static_site_generator/content"
    
    # destination directory
    public_folder_filepath = "/home/luist/workspace/github.com/luis-tirado/static_site_generator/public"

    # delete content in destination directory
    print("Deleting public directory...")
    if os.path.exists(public_folder_filepath):
        shutil.rmtree(public_folder_filepath)

    # move all files from static to public
    print("Copying files from /static to /public")
    copy_files(static_folder_filepath, public_folder_filepath)

    # generate a page from content/index.md using template.html and write it to public/index.html
    print("Generating content...")
    generate_pages_recursive(source_folder_filepath, template_filepath, public_folder_filepath)

main()