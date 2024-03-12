class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.text_type = type
        self.url = url

    def __eq__(self, node2):
        return self.text == node2.text and self.text_type == node2.text_type and self.url == node2.url
    
    def __repr__(self):
        return f"TextNode(TEXT={self.text}, TEXT_TYPE={self.text_type}, URL={self.url})"