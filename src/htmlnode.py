class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(TAG={self.tag}, VALUE={self.value}, CHILDREN={self.children}, PROPS={self.props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode(TAG={self.tag}, VALUE={self.value}, PROPS={self.props})"

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: No value given")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"