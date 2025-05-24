# tajweed_analyzer/text_parser.py

import arabic_characters as ac

def get_letter_complexes(text):
    """
    Breaks down Arabic text into a list of (letter, diacritics_string, start_idx, end_idx_after_diacritics) tuples.
    Skips over non-letter characters like spaces or Waqf marks initially,
    these are handled by the letter_analyzer.
    """
    complexes = []
    i = 0
    while i < len(text):
        char = text[i]

        # Skip spaces, waqf marks, or diacritics if they appear before a letter
        # (though ideally, input is clean or diacritics are part of a letter complex)
        if char.isspace() or char in ac.ARABIC_DIACRITICS_CHARS or char in ac.DEFAULT_STOP_WAQF_MARKS: # Using default here, can be parameterized
            i += 1
            continue

        # Assume 'char' is a base letter
        letter = char
        original_letter_start_idx = i
        diacritics_str = ""
        j = i + 1
        while j < len(text) and text[j] in ac.ARABIC_DIACRITICS_CHARS:
            diacritics_str += text[j]
            j += 1
        
        complexes.append((letter, diacritics_str, original_letter_start_idx, j))
        i = j  # Move to the character after the diacritics
    return complexes

def get_words(text):
    """
    Splits text into words. Basic implementation, might need refinement for complex cases.
    """
    # For simplicity, splitting by space. More robust tokenization might be needed.
    return text.split()

def get_word_at_index(text, char_index):
    """
    Finds the word containing the character at char_index.
    """
    if not text or char_index < 0 or char_index >= len(text) or text[char_index].isspace():
        return ""

    word_start = char_index
    while word_start > 0 and not text[word_start - 1].isspace():
        word_start -= 1
    
    word_end = char_index
    while word_end < len(text) -1 and not text[word_end + 1].isspace(): # Check word_end + 1
        word_end += 1
    
    return text[word_start : word_end + 1]