import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is the content of a text node", TextType.LINK.value, "https://www.google.com")
        self.assertEqual(
            repr(node),
            "TextNode(This is the content of a text node, link, https://www.google.com)"
            )
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")        
        
if __name__ == "__main__":
    unittest.main()
