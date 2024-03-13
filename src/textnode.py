from htmlnode import LeafNode


class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.text_type = type
        self.url = url
        type_verify(self.text_type)

    def __eq__(self, node2):
        return self.text == node2.text and self.text_type == node2.text_type and self.url == node2.url
    
    def __repr__(self):
        return f"TextNode(TEXT={self.text}, TEXT_TYPE={self.text_type}, url={self.url})"
    
def type_verify(text_type):
    known_types = {
        "text": None,
        "bold": "b",
        "italic": "i",
        "code": "code",
        "link": "a",
        "image": "img"
    }
    if text_type not in known_types.keys():
        raise ValueError("Invalid Text Type.")
    return known_types[text_type]
    
def text_node_to_html_node(text_node):
    if text_node.text_type == "link":
        prop = {"href": text_node.url}
        return LeafNode(type_verify(text_node.text_type), text_node.text, prop)
    if text_node.text_type == "image":
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode(type_verify(text_node.text_type), "", props)
    return LeafNode(type_verify(text_node.text_type), text_node.text)