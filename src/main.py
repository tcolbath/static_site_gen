from textnode import TextNode
from htmlnode import HTMLNode

def main():
    texttester = TextNode("String of text", "bold", "https://www.google.com")
    htmltester = HTMLNode("p", "this is a paragraph", None, {"href": "https://www.google.com", "target": 
                                                             "_blank"})
    
    props = htmltester.props_to_html()
    print(props)
main()