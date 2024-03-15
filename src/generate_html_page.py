from block_markdown import markdown_to_html_node
from htmlnode import HTMLNode
import os


def extract_title(markdown):
    lines = markdown.split("\n")
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
            return title
    raise Exception("No Title Found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")
    with open(from_path, encoding="utf-8") as ff:
        markdown_file = ff.read()
    with open(template_path, encoding="utf-8") as tf:
        template_file = tf.read()
    title = extract_title(markdown_file)
    dest_file = template_file.replace("{{ Title }}", title, 1)
    nodes = markdown_to_html_node(markdown_file).to_html()
    dest_file = dest_file.replace("{{ Content }}", nodes, 1)
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path, 'w', encoding="utf-8") as df:
        df.write(dest_file)