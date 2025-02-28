# Python RegEx exercises

import re

def process_receipt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

    a_b_matches = [line.strip() for line in lines if re.search(r'а[б]*', line, re.IGNORECASE)]
    
    # 2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

    a_bb_matches = [line.strip() for line in lines if re.search(r'а[б]{2,3}', line, re.IGNORECASE)]
    
    # 3.Write a Python program to find sequences of lowercase letters joined with a underscore.

    underscore_sequences = [match for line in lines for match in re.findall(r'[а-яё]+_[а-яё]+', line, re.IGNORECASE)]
    
    # 4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.

    capital_sequences = [match for line in lines for match in re.findall(r'[А-ЯЁ][а-яё]+', line)]
    
    # 5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

    a_anything_b = [line.strip() for line in lines if re.search(r'а.*б', line, re.IGNORECASE)]
    
    # 6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.

    replaced_text = [re.sub(r'\s*[ ,.]+\s*', ':', line.strip()) for line in lines]
    
    # 7. Write a python program to convert snake case string to camel case string.

    def snake_to_camel(s):
        return ''.join(word.capitalize() if i > 0 else word for i, word in enumerate(s.split('_')))
    
    camel_case_conversion = [snake_to_camel(line.strip()) for line in lines]
    
    # 8. Write a Python program to split a string at uppercase letters.

    split_uppercase = [re.findall(r'[А-ЯЁ][а-яё]*', line) for line in lines if re.search(r'[А-ЯЁ][а-яё]', line)]
    
    # 9. Write a Python program to insert spaces between words starting with capital letters.

    spaced_capitals = [re.sub(r'([а-яё])([А-ЯЁ])', r'\1 \2', line.strip()) for line in lines]
    
    # 10. Write a Python program to convert a given camel case string to snake case.

    def camel_to_snake(s):
        return re.sub(r'([а-яё])([А-ЯЁ])', r'\1_\2', s).lower()
    
    snake_case_conversion = [camel_to_snake(line.strip()) for line in lines]

    return {
        "a_b_matches": a_b_matches,
        "a_bb_matches": a_bb_matches,
        "underscore_sequences": underscore_sequences,
        "capital_sequences": capital_sequences,
        "a_anything_b": a_anything_b,
        "replaced_text": replaced_text,
        "camel_case_conversion": camel_case_conversion,
        "split_uppercase": split_uppercase,
        "spaced_capitals": spaced_capitals,
        "snake_case_conversion": snake_case_conversion,
    }

# Example

if __name__ == "__main__":
    file_path = r"C:\Users\ACER\Downloads\row.txt"
    result = process_receipt(file_path)
    for key, value in result.items():
        print(f"{key}: {value[:5]}...\n")
