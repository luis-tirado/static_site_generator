import unittest
from block_markdown import *    

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        # CASE: PARAGRAPHS
        md_paragraphs = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        paragraphs_node = markdown_to_html_node(md_paragraphs)
        html = paragraphs_node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

        # CASE: CODE BLOCK
        md_codeblock = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        codeblock_node = markdown_to_html_node(md_codeblock)
        html = codeblock_node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

        # CASE: ORDERED LIST
        md_ordered_list="""
This is **bolded** paragraph text in a p tag here.

1. item number one
2. item number two
3. item number three
"""
        ordered_list_node = markdown_to_html_node(md_ordered_list)
        html = ordered_list_node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here.</p><ol><li>item number one</li><li>item number two</li><li>item number three</li></ol></div>",
        )

        # CASE UNORDORED LIST
        md_unordered_list = """
This is text with _italic_ text in a p tag here.

- item number one
- item number two
- item number three
"""
        unordered_list_node = markdown_to_html_node(md_unordered_list)
        html = unordered_list_node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is text with <i>italic</i> text in a p tag here.</p><ul><li>item number one</li><li>item number two</li><li>item number three</li></ul></div>",
        )

        # CASE QUOTE
        md_quote = """
>\"BELIEVE IN YOURSELF\"
    """
        quote_node = markdown_to_html_node(md_quote)
        html = quote_node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>\"BELIEVE IN YOURSELF\"</blockquote></div>",
        )        

        # CASE HEADING
        md_heading = "# This is a **Heading**\n\nThis is just a paragraph in another paragraph block"
        heading_node = markdown_to_html_node(md_heading)
        html = heading_node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a <b>Heading</b></h1><p>This is just a paragraph in another paragraph block</p></div>"
        )


    def test_block_to_block_type(self):
        heading_text = "# This is a heading"
        code_text = "```This is a code block that starts and ends with three backticks```"
        quote_text = ">\"Believe in yourself\""
        unordered_list_text =  "- List item #1\n- List item #2\n- List item #3"
        ordered_list_text = "1. Banana\n2. Apple\n3.Orange"
        paragraph_text = "This is raw text in a paragraph"

        heading_block_test = block_to_block_type(heading_text)
        self.assertEqual(heading_block_test, BlockType.HEADING)

        code_block_test = block_to_block_type(code_text)
        self.assertEqual(code_block_test, BlockType.CODE)

        quote_block_test = block_to_block_type(quote_text)
        self.assertEqual(quote_block_test, BlockType.QUOTE)

        unordered_list_block_test = block_to_block_type(unordered_list_text)
        self.assertEqual(unordered_list_block_test, BlockType.UNORDERED_LIST)

        ordered_list_block_test = block_to_block_type(ordered_list_text)
        self.assertEqual(ordered_list_block_test, BlockType.ORDERED_LIST)

        paragraph_block_test = block_to_block_type(paragraph_text)
        self.assertEqual(paragraph_block_test, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()