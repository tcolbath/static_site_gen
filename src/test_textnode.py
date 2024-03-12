import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_ineq(self):
        node = TextNode("This is a string", "bold")
        node2 = TextNode("This is a different string", "bold")
        self.assertNotEqual(node, node2)
    
    def test_ineq2(self):
        node = TextNode("This is a string", "bold")
        node2 = TextNode("This is a string", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a string", "bold", "https://www.google.com")
        node2 = TextNode("This is a string", "bold", "https://www.google.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a string", "bold", "https://www.google.com")
        self.assertEqual(
            "TextNode(TEXT=This is a string, TEXT_TYPE=bold, URL=https://www.google.com)",
            repr(node)
        )

if __name__ == "__main__":
    unittest.main()
