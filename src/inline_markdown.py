import re
from textnode import TextNode, type_verify


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    type_verify(text_type)
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode):
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalied Markdown.  Type Flag Not Closed.")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], "text"))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode):
            new_nodes.append(old_node)
            continue
        split_nodes = []
        text = old_node.text
        image_tuples = extract_markdown_images(text)
        if len(image_tuples) == 0:
            new_nodes.append(old_node)
            continue
        for i, image_tuple in enumerate(image_tuples):
            sections = text.split(f"![{image_tuple[0]}]({image_tuple[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown: Image Section Not Properly Enclosed")
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], "text"))
            split_nodes.append(TextNode(image_tuple[0], "image", image_tuple[1]))
            if i < len(image_tuples) - 1:
                text = sections[1]
            elif sections[1] == "":
                continue
            else:
                split_nodes.append(TextNode(sections[1], "text"))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if not isinstance(old_node, TextNode):
            new_nodes.append(old_node)
            continue
        split_nodes = []
        text = old_node.text
        link_tuples = extract_markdown_links(text)
        if len(link_tuples) == 0:
            new_nodes.append(old_node)
            continue
        for i, link_tuple in enumerate(link_tuples):
            sections = text.split(f"[{link_tuple[0]}]({link_tuple[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid Markdown: Link Section Not Properly Enclosed")
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], "text"))
            split_nodes.append(TextNode(link_tuple[0], "link", link_tuple[1]))
            if i < len(link_tuples) - 1:
                text = sections[1]
            elif sections[1] == "":
                continue
            else:
                split_nodes.append(TextNode(sections[1], "text"))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)                