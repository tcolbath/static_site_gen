import unittest
from block_markdown import markdown_to_blocks


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

if __name__ == "__main__":
    unittest.main()