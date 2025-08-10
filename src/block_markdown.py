# Run in CLI to run script testing functions:
# ./test.sh
# * Expecting exit code: 0


from enum import Enum
from htmlnode import *
from inline_func import *
from textnode import *


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown):
    # returns the BlockType representing the type of block it is
    if markdown.startswith("#"):
        if get_heading_size(markdown) < 7:
            return BlockType.HEADING
        else:
            return BlockType.PARAGRAPH
        
    elif markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    
    elif markdown.startswith(">"):
        return BlockType.QUOTE
    
    elif markdown.startswith("- "):
        return BlockType.UNORDERED_LIST
    
    elif markdown.startswith('1'):
        split_md = markdown.split('. ')

        if len(split_md) > 1:
            return BlockType.ORDERED_LIST
        
        return BlockType.PARAGRAPH
    
    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    markdown = markdown.strip('\n')
    blocks_list = markdown.split('\n\n')
    cleaned = []

    for block in blocks_list:
        if block != '':
            b_type = block_to_block_type(block)
            match b_type:
                case BlockType.CODE:
                    cleaned.append(block)
                case BlockType.ORDERED_LIST:
                    cleaned.append(block)
                case BlockType.UNORDERED_LIST:
                    cleaned.append(block)
                case BlockType.QUOTE:
                    cleaned.append(block.replace('\n', ' ').strip())
                case BlockType.PARAGRAPH:
                    cleaned.append(block.replace('\n', ' ').strip())
                case BlockType.HEADING:
                    cleaned.append(block.replace('\n', ' ').strip())

    return cleaned


def markdown_to_html_node(markdown):
    # converts a full markdown document into a single parent HTMLNode
    children_list = []

    str_list = markdown_to_blocks(markdown)

    for str in str_list:
        block_type = block_to_block_type(str)
        match block_type:
            case BlockType.HEADING:
                h_size = get_heading_size(str)
                sliced_str = str[h_size+1:]
                new_children = text_to_children(sliced_str)
                heading_node = ParentNode(f"h{h_size}", new_children)
                children_list.append(heading_node)

            case BlockType.PARAGRAPH:
                new_children = text_to_children(str)
                paragraph_node = ParentNode("p", new_children)
                children_list.append(paragraph_node)

            case BlockType.QUOTE:
                sliced_str = str[1:].strip()
                new_children = text_to_children(sliced_str)
                quote_node = ParentNode("blockquote", text_to_children(sliced_str))
                children_list.append(quote_node)

            case BlockType.CODE:
                sliced_str = str[3:-3]

                if sliced_str[0] == '\n':
                    sliced_str = sliced_str[1:]

                text_node = TextNode(sliced_str, TextType.TEXT)
                code_node = ParentNode("pre", [LeafNode("code", text_node.text)])
                children_list.append(code_node)

            case BlockType.UNORDERED_LIST:
                new_children = convert_list_block(str, BlockType.UNORDERED_LIST)
                unordered_list_node = ParentNode("ul", new_children)
                children_list.append(unordered_list_node)

            case BlockType.ORDERED_LIST:
                new_children = convert_list_block(str, BlockType.ORDERED_LIST)
                ordered_list_node = ParentNode("ol", new_children)
                children_list.append(ordered_list_node)

            case _:
                raise NotImplementedError("Error: This BlockType has not been implemented.")
              
    HTML_Node = ParentNode("div", children_list)

    return HTML_Node


def text_to_children(str):
    text_nodes_list = text_to_textnodes(str)
    html_nodes_list = []

    for item in text_nodes_list:
        # since every item in the text_nodes_list is an object of the class TextNode, we can use method .text_node_to_html_node()
        html_nodes_list.append(item.text_node_to_html_node())

    return html_nodes_list


def get_heading_size(str):
    return len(str.split()[0])


def convert_list_block(block, list_type):
    items = block.split("\n")

    children_list = []

    for item in items:
        if list_type is BlockType.UNORDERED_LIST:
            str_needed = item[2:]
            new_parent_node = ParentNode("li", text_to_children(str_needed))
            children_list.append(new_parent_node)
        elif list_type is BlockType.ORDERED_LIST:
            str_needed = item[item.find('.')+2:]
            new_parent_node = ParentNode("li", text_to_children(str_needed))
            children_list.append(new_parent_node)
        else:
            raise NotImplementedError("This type of list has not been implemented.")

    return children_list