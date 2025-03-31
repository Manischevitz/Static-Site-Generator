from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        # Only process TEXT type nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        # Process the text to find delimiter pairs
        text = old_node.value
        # Start searching from the beginning
        remaining_text = text
        current_position = 0
        
        while delimiter in remaining_text:
            # Find opening delimiter
            start_delimiter = remaining_text.find(delimiter)
            
            # Add text before delimiter as TEXT type
            if start_delimiter > 0:
                before_text = remaining_text[:start_delimiter]
                new_nodes.append(TextNode(before_text, TextType.TEXT))
            
            # Find closing delimiter
            after_opening = remaining_text[start_delimiter + len(delimiter):]
            end_delimiter = after_opening.find(delimiter)
            if end_delimiter == -1:
                raise Exception(f"No closing delimiter found for {delimiter}")
            
            # Extract the content between delimiters
            content = after_opening[:end_delimiter]
            new_nodes.append(TextNode(content, text_type))
            
            # Update remaining text to process
            remaining_text = after_opening[end_delimiter + len(delimiter):]
            
        # Don't forget any remaining text after the last delimiter
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
            
    return new_nodes