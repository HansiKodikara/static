import unittest
from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode,TextType
from leafnode import LeafNode

class Test_text_to_html(unittest.TestCase):
    def test_invalid_type(self):
        with self.assertRaises(AttributeError):
            node = TextNode("example text",TextType.INVALID)
            text_node_to_html_node(node)
    
    def test_not_textnode(self):
        with self.assertRaises(Exception) as context:
            node = "string"
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception),"not a TextNode")
    
    def test_normal(self):
        node = TextNode("Hello world", TextType.NORMAL)
        self.assertEqual(text_node_to_html_node(node).to_html(),LeafNode(value="Hello world").to_html())
    
    def test_bold(self):
        node = TextNode("Important text", TextType.BOLD)
        self.assertEqual(text_node_to_html_node(node).to_html(),LeafNode("b", "Important text").to_html())
    
    def test_italic(self):
        node = TextNode("Emphasized text", TextType.ITALIC)
        self.assertEqual(text_node_to_html_node(node).to_html(),LeafNode("i", "Emphasized text").to_html())
    
    def test_code(self):
        node = TextNode("print('hello')", TextType.CODE)
        self.assertEqual(text_node_to_html_node(node).to_html(),LeafNode("code", "print('hello')").to_html())
    
    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "https://www.example.com")
        self.assertEqual(text_node_to_html_node(node).to_html(),LeafNode("a", "Click here", {"href": "https://www.example.com"}).to_html())
    
    def test_link_without_url(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("Click here", TextType.LINK)
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception),"links should have a url")
        
    
    def test_image(self):
        node = TextNode("Cute cat picture", TextType.IMAGE, "https://www.example.com/cat.jpg")
        self.assertEqual(text_node_to_html_node(node).to_html(),LeafNode("img","", {"src": "https://www.example.com/cat.jpg", "alt": "Cute cat picture"}).to_html())
    
    def test_image_without_src(self):
        with self.assertRaises(ValueError) as context:
            node = TextNode("Alt text", TextType.IMAGE)
            text_node_to_html_node(node)
        self.assertEqual(str(context.exception),"image should have a src")

