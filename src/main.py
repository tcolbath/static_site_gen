from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    texttester = TextNode("String of text", "bold", "https://www.google.com")
    htmltester = HTMLNode("p", "this is a paragraph", None, {"href": "https://www.google.com", "target": 
                                                             "_blank"})
    leaftester = LeafNode("a", "click here", {"href": "https://www.google.com"})
    leaftester2 = LeafNode("p", "This is a paragraph.")
    
    parenttester = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    
    print(parenttester.to_html())


main()