import unittest
from htmlnode import HTMLNode


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
    

if __name__ == "__main__":
    unittest.main()