import unittest
from block_markdown import markdown_to_blocks, block_to_block_type


class TestHTMLNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """This is a **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""

        self.assertListEqual(
            ['This is a **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is'
             ' the same paragraph on a new line', '* This is a list\n* with items'],
             markdown_to_blocks(markdown)
        )

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), "head1")
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), "code")
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), "quote")
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), "ulist")
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), "olist")
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), "par")




if __name__ == "__main__":
    unittest.main()