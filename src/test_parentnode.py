import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_all_leaf(self):
        node = ParentNode(
                            "p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                            ],
                        )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_parent_inside_parent(self):
        node = ParentNode(
                            "p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                ParentNode(  # Add a nested ParentNode here
                                    "div",
                                    [
                                        LeafNode("i", "italic text"),
                                        LeafNode(None, "Another normal text"),
                                    ],
                                ),
                                LeafNode(None, "Final normal text"),
                            ],
                        )
        self.assertEqual(node.to_html(),
                         "<p><b>Bold text</b>Normal text<div><i>italic text</i>Another normal text</div>Final normal text</p>")
    
    def test_depth_3(self):
        node = ParentNode(
                            "div",  # Level 1
                            [
                                LeafNode("h1", "Header Text"),  # Level 1: <h1>
                                ParentNode(  # Level 2: Nested <section>
                                    "section",
                                    [
                                        LeafNode("p", "Paragraph inside section"),  # Level 2: <p>
                                        ParentNode(  # Level 3: Nested <article>
                                            "article",
                                            [
                                                LeafNode("b", "Bold text in article"),  # Level 3: <b>
                                                LeafNode(None, "Plain text in article") # Level 3: Plain text
                                            ]
                                        ),
                                        LeafNode(None, "Another plain text in section")  # Level 2: Plain text
                                    ]
                                ),
                                LeafNode(None, "Footer text at the bottom")  # Level 1: Plain text
                            ]
                        )

        self.assertEqual(node.to_html(),
                         "<div><h1>Header Text</h1><section><p>Paragraph inside section</p><article><b>Bold text in article</b>Plain text in article</article>Another plain text in section</section>Footer text at the bottom</div>")
    
    def test_no_tag(self):
        node = ParentNode(
                            None,  # No tag for the parent node
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Plain text"),
                                LeafNode("i", "Italic text"),
                            ]
                        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception),"Parent node must have a tag")
    
    def test_depth_no_tag(self):
        node = ParentNode(
                            "div",  # Outer ParentNode with a tag
                            [
                                ParentNode(
                                    None,  # Inner ParentNode with no tag
                                    [
                                        LeafNode("b", "Bold text"),  # Child of the inner ParentNode
                                        LeafNode(None, "Plain text")  # Another child
                                    ]
                                ),
                                LeafNode("p", "A paragraph outside the inner node")  # Child of the outer ParentNode
                            ]
                        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception),"Parent node must have a tag")
    
    def test_no_children(self):
        with self.assertRaises(ValueError) as context:
            node = node = ParentNode(
                                        "div",  # Parent node with a valid tag
                                        []      # No children
                                    )
            node.to_html()
        self.assertEqual(str(context.exception),"Parent node must have child nodes")
    
    def test_depth_no_children(self):
        node = ParentNode(
                            "div",  # Outer ParentNode with a tag
                            [
                                ParentNode(
                                    "section",  # Inner ParentNode with a tag but no children
                                    []  # No children
                                ),
                                LeafNode("p", "A paragraph outside the inner node")  # Child of the outer ParentNode
                            ]
                        )
        with self.assertRaises(ValueError) as context:
            node.to_html()
        self.assertEqual(str(context.exception),"Parent node must have child nodes")
    
    
