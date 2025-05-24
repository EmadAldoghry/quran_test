# tajweed_analyzer/qalqalah_rules.py

import arabic_characters as ac
# from . import letter_analyzer as la # Not strictly needed here if stop_context is passed in

# Qalqalah Types
QALQALAH_SUGHRA = "Sughra (Minor)"
QALQALAH_KUBRA = "Kubra (Major)"
QALQALAH_AKBAR = "Akbar/Kubra (Greatest/Major)" # Or just "Akbar"

def check_qalqalah_for_letter_complex(letter_complex, stop_context, 
                                      all_complexes_in_segment=None, current_complex_idx=None): # Added extra args
    """
    Checks if a given letter_complex results in Qalqalah based on its properties and stop_context.
    
    Args:
        letter_complex (tuple): (letter, diacritics_str, start_idx, end_idx_after_diacritics)
        stop_context (dict): Output from letter_analyzer.get_letter_stop_context
        all_complexes_in_segment (list, optional): List of all letter complexes in the current text segment.
                                                   Not used by Qalqalah but provided for compatibility.
        current_complex_idx (int, optional): Index of letter_complex within all_complexes_in_segment.
                                             Not used by Qalqalah but provided for compatibility.

    Returns:
        dict: Qalqalah details if found (type, condition_details), otherwise None.
    """
    letter, diacritics, _, _ = letter_complex
    
    if letter not in ac.QALQALAH_LETTERS:
        return None

    is_qalqalah = False
    qalqalah_type = ""
    # Ensure condition_details starts fresh or correctly incorporates stop_context.details
    condition_details = stop_context.get("details", "").strip() 
    if condition_details and not condition_details.endswith("."): # Add a period if needed for better formatting
        condition_details += "."


    is_at_designated_stop = stop_context.get("is_stop", False)

    # Rule 1: Letter has an explicit Sukoon (ْ)
    if ac.SUKOON in diacritics:
        is_qalqalah = True
        if is_at_designated_stop:
            qalqalah_type = QALQALAH_KUBRA
            condition_details += " Explicit Sukoon at Stop."
        else:
            qalqalah_type = QALQALAH_SUGHRA
            condition_details += " Explicit Sukoon mid-speech."
    
    # Rule 2: Letter is at a Designated Stop and becomes Saakin
    elif is_at_designated_stop:
        has_vowel_or_plain = not diacritics or \
                             any(d in ac.VOWELS_TANWEEN for d in diacritics) and ac.SHADDA not in diacritics

        if has_vowel_or_plain:
            is_qalqalah = True
            qalqalah_type = QALQALAH_KUBRA
            condition_details += " Stop on voweled/plain letter."
        
        elif ac.SHADDA in diacritics: 
            is_qalqalah = True
            qalqalah_type = QALQALAH_AKBAR
            condition_details += " Shadda at Stop."

    if is_qalqalah:
        return {
            "type": qalqalah_type,
            "condition_details": condition_details.strip(),
            "qalqalah_letter": letter,
            "full_letter_complex": letter + diacritics
        }
    return None