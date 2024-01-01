def remove_char_at_index(input_string, index):
    # Convert the string to a list of characters
    char_list = list(input_string)

    # Check if the index is valid
    if 0 <= index < len(char_list):
        # Remove the character at the specified index
        char_list.pop(index)

        # Join the list back into a string
        result_string = ''.join(char_list)

        return result_string
    else:
        print("Invalid index.")
        return None

# Example usage
input_str = "example"
index_to_remove = 2
result = remove_char_at_index(input_str, index_to_remove)

if result is not None:
    print(f"Original string: {input_str}")
    print(f"String after removing character at index {index_to_remove}: {result}")