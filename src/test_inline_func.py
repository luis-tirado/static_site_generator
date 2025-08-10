import unittest
from textnode import TextNode, TextType
from inline_func import *

class TestExtraFunc(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node1 = TextNode("This is text with a `code block` and `code`", TextType.TEXT)
        node2 = TextNode("Another text with a `code`", TextType.TEXT)
        node3 = TextNode("Third text with one more `code`", TextType.TEXT)

        list_of_nodes = [node1, node2, node3]

        test_list = split_node_delimiter(list_of_nodes, '`', TextType.CODE)

        self.assertListEqual(
            test_list,
            [
             TextNode("This is text with a ", TextType.TEXT), 
             TextNode("code block", TextType.CODE), 
             TextNode(" and ", TextType.TEXT), TextNode("code", TextType.CODE), 
             TextNode("Another text with a ", TextType.TEXT), TextNode("code", TextType.CODE), 
             TextNode("Third text with one more ", TextType.TEXT), 
             TextNode("code", TextType.CODE)
            ]
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        ) 
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png")
            ],
            new_nodes
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        textnodes = text_to_textnodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            textnodes
        )

if __name__ == "__main__":
    unittest.main()