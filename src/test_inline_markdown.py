import unittest, re
from textnode import TextNode, type_verify
from inline_markdown import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links, 
    split_nodes_images,
    split_nodes_links,
    text_to_textnodes
)


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

    def test_split_nodes_images(self):
        node = TextNode((
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)" 
            "and another ![second image](https://i.imgur.com/3elNhQu.png)"),
            "text",
        )
        self.assertListEqual(
            [
                TextNode("This is text with an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("and another ", "text"),
                TextNode("second image", "image", "https://i.imgur.com/3elNhQu.png"),
            ],
            split_nodes_images([node])
        )

    def test_split_nodes_images_2(self):
        node = TextNode(
            "![picture](https://i.imgur.com//fjdsaf.png) Here is an image!", "text"
        )
        self.assertListEqual(
            [
                TextNode("picture", "image", "https://i.imgur.com//fjdsaf.png"),
                TextNode(" Here is an image!", "text")
            ],
            split_nodes_images([node])
        )
        
    def test_split_links(self):
        node = TextNode((
            "This is text with a [link](https://boot.dev) and "
            "[another link](https://blog.boot.dev) with text that follows"
            ),
            "text"
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
                TextNode(" and ", "text"),
                TextNode("another link", "link", "https://blog.boot.dev"),
                TextNode(" with text that follows", "text"),
            ],
            new_nodes,
        )
    
    def test_text_to_textnodes(self):
        nodes = text_to_textnodes(
            "This is **bold text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        )
        self.assertListEqual(
            [
                TextNode("This is ", "text"),
                TextNode("bold text", "bold"),
                TextNode(" with an ", "text"),
                TextNode("italic", "italic"),
                TextNode(" word and a ", "text"),
                TextNode("code block", "code"),
                TextNode(" and an ", "text"),
                TextNode("image", "image", "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", "text"),
                TextNode("link", "link", "https://boot.dev"),
            ],
            nodes,
        )



if __name__ == "__main__":
    unittest.main()