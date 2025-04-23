import unittest
from gencontent import extract_title, generate_pages_recursive

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_simple(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")
    
    def test_extract_title_with_whitespace(self):
        markdown = "#    Title with spaces    "
        self.assertEqual(extract_title(markdown), "Title with spaces")
    
    def test_extract_title_multiline(self):
        markdown = """
        Some text
        # The Real Title
        More text
        """
        self.assertEqual(extract_title(markdown), "The Real Title")
    
    def test_extract_title_no_h1(self):
        markdown = """
        ## This is an h2
        Not an h1 in sight
        """
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()