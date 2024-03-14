from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes
from htmlnode import HTMLNode, ParentNode


def markdown_to_blocks(markdown):
    blocks = []
    lines = markdown.split("\n\n")
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        blocks.append(line)
    return blocks

def markdown_to_html_node(markdown):
    dispatch_to_html_node = {
        "code": code_to_html_node,
        "olist": olist_to_html_node,
        "ulist": ulist_to_html_node,
        "quote": quote_to_html_node,
        "h1": heading_to_html_node,
        "h2": heading_to_html_node,
        "h3": heading_to_html_node,
        "h4": heading_to_html_node,
        "h5": heading_to_html_node,
        "h6": heading_to_html_node,
        "par": paragraph_to_html_node
    }
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type not in dispatch_to_html_node.keys():
            raise ValueError(f"Unknown Block Type: '{block_type}'")
        html_node = dispatch_to_html_node[block_type](block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_block_type(block):
    #Simple block types
    headers = {
        "# ": "h1",
        "## ": "h2",
        "### ": "h3",
        "#### ": "h4",
        "##### ": "h5",
        "######": "h6",
    }
    for key in headers.keys():
        if block.startswith(key):
            return headers[key]
    if block.startswith("```"):
        if block.endswith("```"):
            return "code"
    
    #More complex block types
    prev_block_type = "init"
    for i, line in enumerate(block.splitlines()):
        all_lines = False
        
        #Block types
        if line.startswith("> "):
            block_type = "quote"
            all_lines = True
        if line.startswith("* ") or line.startswith("- "):
            block_type = "ulist"
            all_lines = True
        if line.startswith(f"{i+1}."):
            block_type = "olist"
            all_lines = True

        #Verify all lines are matching.
        if prev_block_type != "init":
            if block_type != prev_block_type:
                all_lines = False
        if all_lines == False:
            break
        prev_block_type = block_type

    if all_lines == True:
        return(block_type)
    return("par")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    header_level = block_to_block_type(block)
    text = block.lstrip("#").strip()
    children = text_to_children(text)
    return ParentNode(header_level, children)


def code_to_html_node(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

