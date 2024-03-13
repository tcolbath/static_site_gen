import unittest, re
from textnode import TextNode, type_verify
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", "text")
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", "text"
        )
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded", "bold"),
                TextNode(" word and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", "text"
        )
        new_nodes = split_nodes_delimiter([node], "**", "bold")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("bolded word", "bold"),
                TextNode(" and ", "text"),
                TextNode("another", "bold"),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", "text")
        new_nodes = split_nodes_delimiter([node], "*", "italic")
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", "text")
        new_nodes = split_nodes_delimiter([node], "`", "code")
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("code block", "code"),
                TextNode(" word", "text"),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        text = (
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            " and ![another](https://i.imgur.com/dfsdkjfd.png)"
        )
        self.assertListEqual(
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"), 
                ("another", "https://i.imgur.com/dfsdkjfd.png")
            ],
            extract_markdown_images(text)
        )

    def test_extract_markdown_links(self):
        text = (
            "This is text with a [link](https://www.example.com)"
            " and [another](https://www.example.com/another)"
        )
        self.assertListEqual(
            [
                ("link", "https://www.example.com"), 
                ("another", "https://www.example.com/another")
            ],
            extract_markdown_links(text)
        )



if __name__ == "__main__":
    unittest.main()