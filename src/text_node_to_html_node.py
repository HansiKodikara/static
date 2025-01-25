from textnode import *
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node,TextNode):
        raise Exception("not a TextNode")
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(value=text_node.text) 
        case TextType.BOLD:
            return LeafNode("b",text_node.text)
        case TextType.ITALIC:
            return LeafNode("i",text_node.text)
        case TextType.CODE:
            return LeafNode("code",text_node.text)
        case TextType.LINK:
            if text_node.url == None:
                raise ValueError("links should have a url")
            return LeafNode("a",text_node.text,{"href" : text_node.url})
        case TextType.IMAGE:
            if text_node.url == None:
                raise ValueError("image should have a src")
            return LeafNode("img","",{"src":text_node.url, 
                                        "alt" : text_node.text})


