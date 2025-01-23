import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty(self):
        node = HTMLNode("p","text inside the paragraph",[])
        self.assertEqual(node.props_to_html(),"")
    
    def test_blank_dict(self):
        node = HTMLNode("p","text inside the paragraph",[],{})
        self.assertEqual(node.props_to_html(),"")
    
    def test_include_dict(self):
        node = HTMLNode("p",
                        "text inside the paragraph",
                        [],
                        {"href": "https://www.google.com", "target": "_blank"}
                    )
        self.assertEqual(node.props_to_html(),' href="https://www.google.com" target="_blank"')
