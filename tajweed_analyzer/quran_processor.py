# tajweed_analyzer/quran_processor.py

import json
import text_parser
import letter_analyzer
import arabic_characters as ac # For default waqf marks

def analyze_text_for_rule(sura_idx, aya_idx, text_content, source_type,
                          rule_check_function, considered_waqf_marks,
                          base_char_offset=0, all_complexes_for_context=None, current_complex_index=None):
    """
    Analyzes a text string (Ayah or Bismillah) for instances of a specific Tajweed rule.

    Args:
        sura_idx: Sura index.
        aya_idx: Aya index.
        text_content: The Arabic text to analyze.
        source_type: "text" or "bismillah".
        rule_check_function: A function that takes (letter_complex, stop_context, all_letter_complexes, current_complex_idx)
                             and returns rule findings (dict) or None.
        considered_waqf_marks: A frozenset of Waqf mark characters to consider for stops.
        base_char_offset: Offset for character indexing if text is part of a larger string.
        all_complexes_for_context (list, optional): Pre-parsed list of all letter complexes in text_content.
                                                    Useful for rules needing broader context (like next/prev letter).
        current_complex_index (int, optional): Index of the current_complex within all_complexes_for_context.

    Returns:
        list: A list of dictionaries, each representing a found rule instance.
    """
    results = []
    if not text_content:
        return results

    # If all_complexes_for_context is not provided, parse it now.
    # This is for the case where analyze_text_for_rule is called directly on a single segment.
    # If called from process_quran_for_rule, all_complexes_for_context will be the full ayah's complexes.
    if all_complexes_for_context is None:
        # This path is less common if using the main processor, which should pre-parse.
        # print("Warning: all_complexes_for_context not provided to analyze_text_for_rule. Parsing locally.")
        all_complexes_for_context = text_parser.get_letter_complexes(text_content)
        # If parsed locally, we iterate through them.
        for i, current_complex_tuple in enumerate(all_complexes_for_context):
            letter, diacritics, start_idx, end_idx_after_diacritics = current_complex_tuple
            
            stop_context = letter_analyzer.get_letter_stop_context(
                text_content,
                end_idx_after_diacritics,
                considered_waqf_marks
            )

            rule_finding = rule_check_function(current_complex_tuple, stop_context, all_complexes_for_context, i)

            if rule_finding:
                word_context = text_parser.get_word_at_index(text_content, start_idx)
                instance_data = {
                    "sura": sura_idx,
                    "aya": aya_idx,
                    "source_type": source_type,
                    "word_context": word_context,
                    "char_index_in_text": base_char_offset + start_idx,
                }
                instance_data.update(rule_finding) 
                results.append(instance_data)
        return results # Return early if parsed locally

    # This is the typical path if all_complexes_for_context and current_complex_index are provided
    # (e.g. when iterating from process_quran_for_rule)
    # The arguments `all_complexes_for_context` and `current_complex_index` are not directly used here
    # if the function is meant to iterate itself.
    # Let's stick to the original design where analyze_text_for_rule processes its *own* text_content
    # by generating complexes, and the rule_check_function receives the full list for context.

    # Reverting to the simpler design for this function:
    # It gets letter complexes for *its own* text_content.
    # The rule_check_function is given these specific complexes.
    
    letter_complexes_for_this_text = text_parser.get_letter_complexes(text_content)

    for i, current_complex_tuple in enumerate(letter_complexes_for_this_text):
        letter, diacritics, start_idx, end_idx_after_diacritics = current_complex_tuple
        
        stop_context = letter_analyzer.get_letter_stop_context(
            text_content, # context for stop is within this specific text_content
            end_idx_after_diacritics,
            considered_waqf_marks
        )

        # The rule_check_function receives the complexes of the *current text segment*
        # (e.g., just the Bismillah, or just the Ayah text)
        # This is important for rules like Idgham that look at the *next* letter within that segment.
        rule_finding = rule_check_function(
            current_complex_tuple, 
            stop_context, 
            letter_complexes_for_this_text, # Pass the list of complexes for this segment
            i                               # Pass the index within this segment's complexes
        )

        if rule_finding:
            word_context = text_parser.get_word_at_index(text_content, start_idx)
            
            instance_data = {
                "sura": sura_idx,
                "aya": aya_idx,
                "source_type": source_type,
                "word_context": word_context,
                "char_index_in_text": base_char_offset + start_idx,
            }
            instance_data.update(rule_finding) 
            results.append(instance_data)
            
    return results


def process_quran_for_rule(json_file_path, rule_check_function, 
                           considered_waqf_marks=None):
    """
    Loads Quran JSON and applies a rule_check_function to find all instances.
    """
    if considered_waqf_marks is None:
        considered_waqf_marks = ac.DEFAULT_STOP_WAQF_MARKS
        
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            quran_data = json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{json_file_path}': {e}")
        return []

    all_rule_instances = []

    # Adapt based on your JSON structure. This is one common structure.
    if "quran" in quran_data and "suras" in quran_data["quran"]:
        data_iterator = quran_data["quran"]["suras"]
        sura_key, aya_key, text_key, bismillah_key = "index", "index", "text", "bismillah"
        ayas_list_key = "ayas"
    elif isinstance(quran_data, list) and quran_data and ("sura_number" in quran_data[0] or "index" in quran_data[0]): # list of sura objects
        data_iterator = quran_data
        # Try to determine keys more flexibly
        sura_example = quran_data[0]
        sura_key = "sura_number" if "sura_number" in sura_example else "index"
        
        ayas_list_key = "verses" if "verses" in sura_example and sura_example["verses"] else \
                        "ayas" if "ayas" in sura_example and sura_example["ayas"] else None
        if not ayas_list_key or not sura_example[ayas_list_key]:
             print("Error: Could not determine ayas list key or ayas list is empty in the simpler JSON structure.")
             return []

        aya_example = sura_example[ayas_list_key][0]
        aya_key = "verse_number" if "verse_number" in aya_example else "index"
        text_key = "text" if "text" in aya_example else None # text is crucial
        if not text_key:
            print(f"Error: Could not determine 'text_key' for ayas in simpler JSON structure for sura {sura_example.get(sura_key)}")
            return []
            
        bismillah_key = "bismillah" # This might not exist in this simpler structure or be part of text
    else: 
        print("Error: JSON structure is not recognized. Please adapt quran_processor.py.")
        return []


    for sura_obj in data_iterator:
        sura_idx = sura_obj.get(sura_key)
        if not sura_idx: # Skip if sura index is missing
            print(f"Warning: Missing Sura index for object: {sura_obj}")
            continue

        if ayas_list_key in sura_obj:
            for aya_obj in sura_obj[ayas_list_key]:
                aya_idx = aya_obj.get(aya_key)
                text = aya_obj.get(text_key, "")
                bismillah = aya_obj.get(bismillah_key) 

                if text:
                    all_rule_instances.extend(
                        analyze_text_for_rule(sura_idx, aya_idx, text, "text", # source_type = "text"
                                              rule_check_function, considered_waqf_marks)
                    )
                if bismillah:
                    # For Bismillah, aya_idx might be considered 0 or the current aya_idx.
                    # If Bismillah is only at the start of a Sura, it might be associated with aya 1 (or 0).
                    # Let's assume Bismillah from aya_obj is related to that aya_idx.
                    # If your JSON means Bismillah is *before* aya 1 of most Suras,
                    # you might want a fixed aya_idx (like 0) for bismillah.
                    b_aya_idx = aya_idx # Or 0 if Bismillah is always "verse 0"
                    all_rule_instances.extend(
                        analyze_text_for_rule(sura_idx, b_aya_idx, bismillah, "bismillah", # source_type = "bismillah"
                                              rule_check_function, considered_waqf_marks)
                    )
    return all_rule_instances