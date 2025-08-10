import re

from textnode import TextNode, TextType

def text_to_textnodes(text):
    original_node = TextNode(text, TextType.TEXT)

    first_node_list = split_node_delimiter([original_node], '**', TextType.BOLD)
    second_node_list = split_node_delimiter(first_node_list, '_', TextType.ITALIC)
    third_node_list = split_node_delimiter(second_node_list, '`', TextType.CODE)
    fourth_node_list = split_nodes_image(third_node_list)
    fifth_node_list = split_nodes_link(fourth_node_list)

    return fifth_node_list

def split_node_delimiter(old_nodes, delimiter, text_type):
    if not (delimiter == '`' or delimiter == '**' or delimiter == '_'):
        raise Exception("ERROR: Please enter a valid delimiter.")
    
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            # append to list as-is, we only want to split "text" type objects 
            new_nodes.append(old_node)
        else:
            split_node = old_node.text.split(delimiter)
            for words in split_node:
                index = split_node.index(words) + 1

                # textnodes with empty text should not be added to new_nodes
                if words.strip() == '':
                    continue

                if index % 2 != 0:
                    new_nodes.append(TextNode(words, TextType.TEXT))
                    continue
                else:
                    new_nodes.append(TextNode(words, text_type))

    return new_nodes

def extract_markdown_images(text):
    # images format --> ![rick roll](https://i.imgur.com/aKaOqIh.gif)
    image_pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    images_list = re.findall(image_pattern, text)

    return images_list

def extract_markdown_links(text):
    # links format --> [to boot dev](https://www.boot.dev)
    link_pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    links_list = re.findall(link_pattern, text)

    return links_list

def split_nodes_image(old_nodes):
    final_new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            final_new_nodes.append(old_node)
            continue

        node_text = old_node.text
        images = extract_markdown_images(node_text)

        # Check if images are found in node_text, if not, append node as-is
        if len(images) == 0:
            final_new_nodes.append(old_node)
            continue

        for image in images:
            image_alt = image[0]
            image_url = image[1]
            split_text = node_text.split(f"![{image_alt}]({image_url})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid image format.")
            
            if split_text[0] != "":
                final_new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            
            final_new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            node_text = split_text[1]

        if node_text != "":
            final_new_nodes.append(TextNode(node_text, TextType.TEXT))

    return final_new_nodes

def split_nodes_link(old_nodes):
    final_new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            final_new_nodes.append(old_node)
            continue

        node_text = old_node.text
        links = extract_markdown_links(node_text)

        # Check if links are found in node_text, if not, append node as-is
        if len(links) == 0:
            final_new_nodes.append(old_node)
            continue

        for link in links:
            link_alt = link[0]
            link_url = link[1]
            split_text = node_text.split(f"[{link_alt}]({link_url})", 1)
            if len(split_text) != 2:
                raise ValueError("Invalid image format.")
            
            if split_text[0] != "":
                final_new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            
            final_new_nodes.append(TextNode(link_alt, TextType.LINK, link_url))
            node_text = split_text[1]

        if node_text != "":
            final_new_nodes.append(TextNode(node_text, TextType.TEXT))

    return final_new_nodes