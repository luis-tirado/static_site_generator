import unittest
from htmlnode import HTMLNode, LeafNode,  ParentNode

class TestHTMLNode(unittest.TestCase):
    # Tests for HTMLNodes
    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )
        
    def test_repr(self):
        node = HTMLNode("p", "This is a paragraph in HTML", None, None)
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, This is a paragraph in HTML, None, None)"
        )
        
    def test_props_to_html(self):
        node = HTMLNode("h1", "Title 1", None, {"href": "https://www.google.com", "class":"main_title"})
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" class="main_title"'
        )


    # Tests for LeafNodes
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    # Tests for ParentNodes
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()