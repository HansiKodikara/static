from textnode import *

def split_nodes_delimiter(old_nodes:list[TextNode], delimiter:str, text_type:TextType):
    # Initialize a new list of nodes to hold the processed result
    new_nodes = []
    # Iterate over each node in the old list
    for node in old_nodes:
        # If the node is not of type NORMAL, or doesn't contain the delimiter add it append it to the list as it is
        if node.text_type != TextType.NORMAL or delimiter not in node.text:
            new_nodes += [node]
        else:
            # Split NORMAL nodes that contain the delimiter
            new_nodes += split_one_node(node,delimiter,text_type)
    return new_nodes

        

def split_one_node(node:TextNode,delimiter:str,text_type:TextType):
    # Initialize an empty list of new nodes to hold the result
    new_nodes = []
    # Count the total number of delimiters; if odd one delimeter hasnt been closed which should raise an error
    if node.text.count(delimiter) % 2 != 0:
        raise Exception(f"Unmatched delimiter: {delimiter} in text: {node.text}")
    else:
        #copy text to a temporary variable so that it can be modified
        temp_text = node.text
        #Find the position of the first delimiter
        first = temp_text.find(delimiter)

        while first != -1:
            # Text before the first delimiter is NORMAL and added if non-empty
            if temp_text[:first]:
                new_nodes.append(TextNode(temp_text[:first],TextType.NORMAL))
            # Remove everything up to (and including) the first delimiter
            temp_text = temp_text[first+len(delimiter):]
             # Find the position of the next delimiter, marking the closing delimiter
            second = temp_text.find(delimiter)
            # Text between the first and second delimiters is assigned the new text_type
            if temp_text[:second]:
                new_nodes.append(TextNode(temp_text[:second],text_type))
            # Remove everything up to (and including) the second delimiter
            temp_text = temp_text[second+len(delimiter):]
            # Look for the next opening delimiter in the remaining text to continue the while loop
            first = temp_text.find(delimiter)

        # After exiting the loop, if text remains, it is treated as NORMAL
        if temp_text:
            new_nodes.append(TextNode(temp_text,TextType.NORMAL))
        return new_nodes



