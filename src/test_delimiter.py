import unittest
from delimiter  import split_nodes_delimiter
from textnode import TextType, TextNode


class TestSplitNodesDelimiter(unittest.TestCase):

    def test_single_code_delimiter(self):
        node = TextNode("This is `code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE)
        ]
        self.assertEqual(result, expected)

    def test_multiple_code_blocks(self):
        node = TextNode("Text `code1` and `code2` done", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Text ", TextType.TEXT),
            TextNode("code1", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("code2", TextType.CODE),
            TextNode(" done", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_odd_number_of_delimiters(self):
        node = TextNode("Unfinished `code here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]  # Should be returned as is
        self.assertEqual(result, expected)

    def test_bold_text(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_italic_text(self):
        node = TextNode("This _italic_ word", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("This ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_mixed_formatting(self):
        node = TextNode("Mix `code` and **bold**", TextType.TEXT)
        step1 = split_nodes_delimiter([node], "`", TextType.CODE)
        result = split_nodes_delimiter(step1, "**", TextType.BOLD)
        expected = [
            TextNode("Mix ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    def test_non_text_node_pass_through(self):
        node1 = TextNode("This is text", TextType.TEXT)
        node2 = TextNode("bold", TextType.BOLD)
        result = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        expected = [TextNode("This is text", TextType.TEXT), node2]
        self.assertEqual(result, expected)

    def test_empty_string(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()