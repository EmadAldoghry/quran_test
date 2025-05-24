# tajweed_analyzer/letter_analyzer.py

import arabic_characters as ac

def is_end_of_text(text_length, char_end_index_after_diacritics):
    """Checks if the letter (including its diacritics) is at the very end of the text."""
    return char_end_index_after_diacritics == text_length

def get_next_meaningful_char_and_index(text, start_index):
    """
    Finds the next non-space character and its index starting from start_index.
    Returns (None, -1) if no such character is found.
    """
    idx = start_index
    while idx < len(text):
        if not text[idx].isspace():
            return text[idx], idx
        idx += 1
    return None, -1

def is_followed_by_waqf(text, char_end_index_after_diacritics, considered_waqf_marks):
    """
    Checks if the letter is followed by one of the considered Waqf marks,
    possibly with spaces in between.
    Returns the Waqf mark character if found, otherwise None.
    """
    next_char, _ = get_next_meaningful_char_and_index(text, char_end_index_after_diacritics)
    if next_char and next_char in considered_waqf_marks:
        return next_char
    return None

def is_end_of_word(text, char_end_index_after_diacritics, letter_start_index):
    """
    Checks if the letter is at the end of a word.
    A word ends if followed by a space, end of text, or a Waqf mark (usually).
    This is a simplified check; true word boundaries can be complex.
    """
    if char_end_index_after_diacritics >= len(text): # End of text
        return True
    
    next_char = text[char_end_index_after_diacritics]
    if next_char.isspace(): # Followed by space
        return True
    
    # Consider if next char is a Waqf mark for end-of-word context,
    # though `is_followed_by_waqf` is more specific for stop rules.
    # if next_char in ac.DEFAULT_STOP_WAQF_MARKS:
    #     return True
        
    return False


STOP_REASON_END_OF_AYAH = "end_of_ayah"
STOP_REASON_WAQF_MARK = "waqf_mark"

def get_letter_stop_context(text_content, char_end_index_after_diacritics, considered_waqf_marks):
    """
    Determines if a letter is at a "designated stop" position.
    A designated stop can be the end of the Ayah/text or immediately preceding a Waqf mark.

    Returns a dictionary:
    {
        "is_stop": True/False,
        "reason": "end_of_ayah" | "waqf_mark" | None,
        "waqf_char": actual waqf character if reason is "waqf_mark", else None
        "details": string description
    }
    """
    stop_context = {"is_stop": False, "reason": None, "waqf_char": None, "details": ""}

    # Check 1: End of the entire text (Ayah or Bismillah)
    if is_end_of_text(len(text_content), char_end_index_after_diacritics):
        stop_context["is_stop"] = True
        stop_context["reason"] = STOP_REASON_END_OF_AYAH
        stop_context["details"] = "End of text."
        return stop_context

    # Check 2: Followed by a Waqf mark (potentially with spaces in between)
    waqf_mark_found = is_followed_by_waqf(text_content, char_end_index_after_diacritics, considered_waqf_marks)
    if waqf_mark_found:
        stop_context["is_stop"] = True
        stop_context["reason"] = STOP_REASON_WAQF_MARK
        stop_context["waqf_char"] = waqf_mark_found
        waqf_display = ac.WAQF_MARK_NAMES.get(waqf_mark_found, waqf_mark_found)
        stop_context["details"] = f"Followed by Waqf mark '{waqf_display}'."
        return stop_context
        
    return stop_context