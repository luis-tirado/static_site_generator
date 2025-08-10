from enum import Enum
from htmlnode import LeafNode, ParentNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE =  "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text   
        self.text_type = text_type
        self.url = url

    # This function checks if two text nodes are equal
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        
        return( 
            self.text == other.text
            and self.text_type == other.text_type 
            and self.url == other.url 
        )
    
    def __repr__(self):
        if self.url is None:
            return f"TextNode({self.text}, {self.text_type.value})" 
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    
    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT:
            return LeafNode(None, self.text)
        if self.text_type == TextType.BOLD:
            return LeafNode("b", self.text)
        if self.text_type == TextType.ITALIC:
            return LeafNode("i", self.text)
        if self.text_type == TextType.CODE:
            return LeafNode("code", self.text)
        if self.text_type == TextType.LINK:
            return LeafNode("a", self.text, {"href": self.url})
        if self.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": self.url, "alt": self.text})
        raise ValueError(f"invalid text type: {self.text_type}")