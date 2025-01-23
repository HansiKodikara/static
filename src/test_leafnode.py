import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_all_included(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(),'<a href="https://www.google.com">Click me!</a>')
    
    def test_no_tag(self):
        leaf = LeafNode(value = "Click me!")
        self.assertEqual(leaf.to_html(),'Click me!')
    
    def test_no_value(self):
        with self.assertRaises(ValueError) as context:
            leaf = LeafNode("p")
            leaf.to_html()
        self.assertEqual(str(context.exception), "A leaf node must have a value.")
    
    def test_no_props(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(),"<p>This is a paragraph of text.</p>")
    

