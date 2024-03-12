from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    texttester = TextNode("String of text", "bold", "https://www.google.com")
    htmltester = HTMLNode("p", "this is a paragraph", None, {"href": "https://www.google.com", "target": 
                                                             "_blank"})
    leaftester = LeafNode("a", "click here", {"href": "https://www.google.com"})
    leaftester2 = LeafNode("p", "This is a paragraph.")
    print(leaftester.to_html())
    print(leaftester2.to_html())

main()