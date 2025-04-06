import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, url = None)
        node2 = TextNode("This is a text node", TextType.BOLD, url = None)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, url = None)
        node2 = TextNode("This is a text node", TextType.ITALIC, url = None)
        self.assertNotEqual(node, node2)
    
    def test_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, url = "www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, url = "www.boot.dev")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()