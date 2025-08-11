import os
import shutil
import sys

from copydirectory import copy_files
from content_generator import generate_pages_recursive


def main():
    # BASEPATH is the root directory path where the website will be served from on the web server
    # if the length of the list returned by sys.argv is greater than 1, basepath is the second element in the CLI commands list
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        # for local testing, main.py is default to /
        basepath = '/'

    print(f"Using basepath: *{basepath}")

    # static directory
    static_folder_filepath = "/home/luist/workspace/github.com/luis-tirado/static_site_generator/static"

    # template filepath
    template_filepath = "/home/luist/workspace/github.com/luis-tirado/static_site_generator/template.html"

    # source directory
    source_folder_filepath = "/home/luist/workspace/github.com/luis-tirado/static_site_generator/content"
    
    # destination directory
    docs_folder_filepath = "/home/luist/workspace/github.com/luis-tirado/static_site_generator/docs"

    # delete content in destination directory
    print("Deleting docs directory...")
    if os.path.exists(docs_folder_filepath):
        shutil.rmtree(docs_folder_filepath)

    # move all files from static to docs
    print("Copying files from /static to /docs")
    copy_files(static_folder_filepath, docs_folder_filepath)

    # generate a page from content/ to docs/, using template.html
    # basepath 
    print("Generating content...")
    generate_pages_recursive(source_folder_filepath, template_filepath, docs_folder_filepath, basepath)

    
    

main()