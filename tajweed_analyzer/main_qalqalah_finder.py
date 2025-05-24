# tajweed_analyzer/main_qalqalah_finder.py

import json
import quran_processor
import qalqalah_rules
import arabic_characters as ac # To select specific waqf marks if needed

def main():
    quran_json_file = "tajweed_analyzer/quran_data/quran_nasekh.json" # Adjust path

    print(f"Finding Qalqalah instances in '{quran_json_file}'...")

    # --- Configuration for Qalqalah Search ---
    # 1. Define which Waqf marks should be considered as causing a stop for Qalqalah Kubra/Akbar
    #    You can use the default, or a subset, or an empty set if you only want end-of-ayah stops.
    
    # Example 1: Use all default stop marks
    active_waqf_marks_for_stop = ac.DEFAULT_STOP_WAQF_MARKS
    
    # Example 2: Only consider compulsory (Meem) and preferred (Qala) stops
    # active_waqf_marks_for_stop = frozenset([ac.WAQF_MEEM, ac.WAQF_QALA])

    # Example 3: Only consider end of Ayah (no explicit Waqf marks causing stop effect for Qalqalah Kubra)
    # active_waqf_marks_for_stop = frozenset()


    # 2. The rule checking function for Qalqalah
    rule_to_apply = qalqalah_rules.check_qalqalah_for_letter_complex

    # --- Run the processor ---
    qalqalah_list = quran_processor.process_quran_for_rule(
        json_file_path=quran_json_file,
        rule_check_function=rule_to_apply,
        considered_waqf_marks=active_waqf_marks_for_stop
    )

    if qalqalah_list:
        print(f"\nFound {len(qalqalah_list)} Qalqalah instances.")
        
        # Print a sample
        sample_size = 10
        if len(qalqalah_list) > 2 * sample_size:
            for i, instance in enumerate(qalqalah_list[:sample_size]):
                print_instance(instance)
            print("...")
            for i, instance in enumerate(qalqalah_list[-sample_size:]):
                print_instance(instance)
        else:
            for instance in qalqalah_list:
                print_instance(instance)
        
        # Optionally save to file
        # output_file = "qalqalah_found_modular.json"
        # with open(output_file, 'w', encoding='utf-8') as f:
        #     json.dump(qalqalah_list, f, ensure_ascii=False, indent=2)
        # print(f"\nSaved detailed list to {output_file}")

    else:
        print("No Qalqalah instances found or an error occurred.")

def print_instance(instance):
    print(f"S{instance['sura']}:A{instance['aya']} ({instance['source_type']}) "
          f"W:'{instance['word_context']}', "
          f"L:'{instance.get('full_letter_complex', instance.get('qalqalah_letter', 'N/A'))}', " # Use .get for safety
          f"T:{instance['type']}, C:{instance['condition_details']}")

if __name__ == "__main__":
    # To run this from the parent directory of tajweed_analyzer:
    # python -m tajweed_analyzer.main_qalqalah_finder
    # Or, if you are inside the tajweed_analyzer directory:
    # Ensure __init__.py exists in tajweed_analyzer if running as a package.
    # Then, from one level up: python -m tajweed_analyzer.main_qalqalah_finder
    # If running this file directly and it's in a subdirectory, Python path issues might occur.
    # For simplicity if running directly from its own directory, change imports from
    # `from . import module` to `import module` and ensure parent path is in PYTHONPATH.
    
    # The simplest way to make imports work for this structure is often to
    # navigate to the directory *above* `tajweed_analyzer` and run:
    # `python -m tajweed_analyzer.main_qalqalah_finder`
    # This requires an empty `__init__.py` file in the `tajweed_analyzer` directory.
    
    # Create an empty __init__.py in tajweed_analyzer/
    # tajweed_analyzer/__init__.py (can be empty)
    main()