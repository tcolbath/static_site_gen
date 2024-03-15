from copy_static import copy_files
from generate_content import generate_pages_recursive
import shutil, os


dir_path_static = "./static"
dir_path_public = "./public"
content_path_dir = "./content/"
template = "./template.html"
dest_content_dir = "./public/"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)

    generate_pages_recursive(content_path_dir, template, dest_content_dir)


main()