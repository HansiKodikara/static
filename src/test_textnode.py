import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    
    def test_same_properties(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)
    
    def test_eq_None(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,None)
        self.assertEqual(node,node2)
    
    def test_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node",TextType.BOLD,"http://boot.dev")
        self.assertNotEqual(node,node2)
    
    def test_different_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node,node2)
    
    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different node", TextType.BOLD)
        self.assertNotEqual(node,node2)



if __name__ == "__main__":
    unittest.main()