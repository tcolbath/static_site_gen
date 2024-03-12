import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        link = HTMLNode(
            "a", 
            "click here", 
            None, 
            {"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(
            "HTMLNode(TAG=a, VALUE=click here, CHILDREN=None, PROPS={'href': 'https://www.google.com', 'target': '_blank'})",
            repr(link)
        )
    
    def test_props_to_html(self):
        test_link = HTMLNode(
            "a", 
            "click here", 
            None, 
            {"href": "https://www.google.com", "target": "_blank"}
        )
        html_link = test_link.props_to_html()
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', 
            html_link
        )
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

if __name__ == "__main__":
    unittest.main()