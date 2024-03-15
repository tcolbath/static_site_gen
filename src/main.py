from copy_static import copy_files
from generate_html_page import generate_page
import shutil, os

dir_path_static = "./static"
dir_path_public = "./public"
from_content_path = "./content/index.md"
template_path = "./template.html"
dest_content_path = "./public/index.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files(dir_path_static, dir_path_public)

    generate_page(from_content_path, template_path, dest_content_path)
main()