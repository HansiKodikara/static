import unittest
from markdown_utils import extract_markdown_images, extract_markdown_links 

class TestMarkdownExtraction(unittest.TestCase):

    def test_extract_markdown_images(self):
        # Test cases for extract_markdown_images
        self.assertEqual(
            extract_markdown_images("![image](url1)"),
            [("image", "url1")]
        )
        self.assertEqual(
            extract_markdown_images("![alt text](https://example.com/image.png)"),
            [("alt text", "https://example.com/image.png")]
        )
        self.assertEqual(
            extract_markdown_images("![img1](url1) ![img2](url2)"),
            [("img1", "url1"), ("img2", "url2")]
        )
        self.assertEqual(
            extract_markdown_images("[link](url1) ![image](url2)"),
            [("image", "url2")]
        )
        self.assertEqual(
            extract_markdown_images("No images here"),
            []
        )

    def test_extract_markdown_links(self):
        # Test cases for extract_markdown_links
        self.assertEqual(
            extract_markdown_links("[link](url1)"),
            [("link", "url1")]
        )
        self.assertEqual(
            extract_markdown_links("Check [this](url1) and [that](url2)"),
            [("this", "url1"), ("that", "url2")]
        )
        self.assertEqual(
            extract_markdown_links("![image](url1) [link](url2)"),
            [("link", "url2")]
        )
        self.assertEqual(
            extract_markdown_links("[link](url1) ![image](url2) [another link](url3)"),
            [("link", "url1"), ("another link", "url3")]
        )
        self.assertEqual(
            extract_markdown_links("No links here"),
            []
        )

    def test_edge_cases(self):
        # Test mixed cases
        self.assertEqual(
            extract_markdown_images("[link](url1) ![image](url2) [another link](url3)"),
            [("image", "url2")]
        )
        self.assertEqual(
            extract_markdown_links("[link](url1) ![image](url2) [another link](url3)"),
            [("link", "url1"), ("another link", "url3")]
        )

        # Empty string
        self.assertEqual(extract_markdown_images(""), [])
        self.assertEqual(extract_markdown_links(""), [])

        # Malformed Markdown
        self.assertEqual(extract_markdown_images("![image](url"), [])
        self.assertEqual(extract_markdown_links("[link](url"), [])
        self.assertEqual(extract_markdown_images("[link](url)"), [])
        self.assertEqual(extract_markdown_links("![image](url)"), [])
