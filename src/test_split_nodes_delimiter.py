import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import *

class Test_split_nodes_delimiter(unittest.TestCase):
    def test_basic_usage(self):
        node = TextNode("A *bold* word and more *which is italic*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "*", TextType.BOLD)
        self.assertEqual(new_nodes,[
                                    TextNode("A ", TextType.NORMAL),
                                    TextNode("bold", TextType.BOLD),
                                    TextNode(" word and more ", TextType.NORMAL),
                                    TextNode("which is italic", TextType.BOLD),
                                ])
    
    def test_no_matching_delimeter(self):
        node = TextNode("This is text without a closing delimiter `oops", TextType.NORMAL)
        with self.assertRaises(Exception) as context:
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception),f"Unmatched delimiter: ` in text: {node.text}")
    
    #need to add more tests (lesson 3.1 )

