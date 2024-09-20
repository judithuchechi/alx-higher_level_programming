#!/usr/bin/python3


'''
   5-text_indentation
   Contains a function that adds new line after characters
'''


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ''' List of characters that should trigger a new line'''
    special_chars = ['.', '?', ':']

    '''Temporary string to hold the modified text'''
    new_text = ""

    ''' Iterate through each character in the text'''
    for char in text:
        new_text += char
        ''' Add the character to the new_text string'''
        if char in special_chars:
            new_text += "\n\n"
            ''' Add two newlines after special characters'''
    ''' Split text by lines, strip excess spaces from each line, and print'''
    lines = new_text.splitlines()
    for line in lines:
        print(line.strip(), end="")
        ''' Strip spaces and print each line without adding extra newlines'''
        if line != lines[-1]:
            print()
            ''' Print a newline between lines'''
