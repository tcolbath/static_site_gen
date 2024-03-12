from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.text_type = type
        self.url = url
        self.type_verify()

    def __eq__(self, node2):
        return self.text == node2.text and self.text_type == node2.text_type and self.url == node2.url
    
    def __repr__(self):
        return f"TextNode(TEXT={self.text}, TEXT_TYPE={self.text_type}, url={self.url})"
    
    def type_verify(self):
        known_types = {
            "text": None,
            "bold": "b",
            "italic": "i",
            "code": "code",
            "link": "a",
            "image": "img"
        }
        if self.text_type not in known_types.keys():
            raise ValueError("Incorrect Text Type in TextNode")
        return known_types[self.text_type]
    
def text_node_to_html_node(text_node):
    if text_node.text_type == "link":
        prop = {"href": text_node.url}
        return LeafNode(text_node.type_verify(), text_node.text, prop)
    if text_node.text_type == "image":
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode(text_node.type_verify(), "", props)
    return LeafNode(text_node.type_verify(), text_node.text)