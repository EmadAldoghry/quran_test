# tajweed_analyzer/arabic_characters.py

# --- Basic Arabic Letters (Alphabet) ---
ALEF = '\u0627'  # ا
BEH = '\u0628'   # ب
TEH = '\u062A'   # ت
THEH = '\u062B'  # ث
JEEM = '\u062C'  # ج
HAH = '\u062D'   # ح
KHAH = '\u062E'  # خ
DAL = '\u062F'   # د
THAL = '\u0630'  # ذ
REH = '\u0631'   # ر
ZAIN = '\u0632'  # ز
SEEN = '\u0633'  # س
SHEEN = '\u0634' # ش
SAD = '\u0635'   # ص
DAD = '\u0636'   # ض
TAH_LETTER = '\u0637' # ط (Letter, distinct from Waqf mark Tah)
ZAH = '\u0638'   # ظ
AIN = '\u0639'   # ع
GHAIN = '\u063A' # غ
FEH = '\u0641'   # ف
QAF = '\u0642'   # ق
KAF = '\u0643'   # ك
LAM = '\u0644'   # ل
MEEM_LETTER = '\u0645' # م (Letter, distinct from Waqf mark Meem)
NOON = '\u0646'  # ن
HEH = '\u0647'   # ه
WAW = '\u0648'   # و
YEH = '\u064A'   # ي

ARABIC_ALPHABET_BASIC = frozenset([
    ALEF, BEH, TEH, THEH, JEEM, HAH, KHAH, DAL, THAL, REH, ZAIN, SEEN, SHEEN,
    SAD, DAD, TAH_LETTER, ZAH, AIN, GHAIN, FEH, QAF, KAF, LAM, MEEM_LETTER,
    NOON, HEH, WAW, YEH
])

# --- Hamzas ---
HAMZA = '\u0621'                     # ء ARABIC LETTER HAMZA
ALEF_WITH_MADDA_ABOVE = '\u0622'    # آ ARABIC LETTER ALEF WITH MADDA ABOVE
ALEF_WITH_HAMZA_ABOVE = '\u0623'    # أ ARABIC LETTER ALEF WITH HAMZA ABOVE
WAW_WITH_HAMZA_ABOVE = '\u0624'     # ؤ ARABIC LETTER WAW WITH HAMZA ABOVE
ALEF_WITH_HAMZA_BELOW = '\u0625'    # إ ARABIC LETTER ALEF WITH HAMZA BELOW
YEH_WITH_HAMZA_ABOVE = '\u0626'     # ئ ARABIC LETTER YEH WITH HAMZA ABOVE
HAMZAT_WASL = '\u0671'              # ٱ ARABIC LETTER ALEF WASLA (often for Hamzat al-Wasl)
HIGH_HAMZA = '\u0674'               # ٴ ARABIC LETTER HIGH HAMZA (can appear on Alef, Waw, Yeh)
# Note: Some Quranic scripts use U+0621 for Hamzat al-Wasl on a bare Alef.
# U+065C (SMALL V ABOVE) is also sometimes used for Hamzat al-Wasl.

HAMZAS = frozenset([
    HAMZA, ALEF_WITH_MADDA_ABOVE, ALEF_WITH_HAMZA_ABOVE, WAW_WITH_HAMZA_ABOVE,
    ALEF_WITH_HAMZA_BELOW, YEH_WITH_HAMZA_ABOVE, HAMZAT_WASL, HIGH_HAMZA
])

# --- Other Letter Variations & Ligatures ---
TEH_MARBUTA = '\u0629'              # ة ARABIC LETTER TEH MARBUTA
ALEF_MAKSURA = '\u0649'             # ى ARABIC LETTER ALEF MAKSURA (often acts like YEH without dots)
LAM_ALEF_LIGATURE = '\u0644\u0627'  # لا (This is a sequence, not a single char in Unicode for basic LA)
LAM_ALEF_HAMZA_ABOVE_LIGATURE = '\u0644\u0623' # لأ
LAM_ALEF_HAMZA_BELOW_LIGATURE = '\u0644\u0625' # لإ
LAM_ALEF_MADDA_ABOVE_LIGATURE = '\u0644\u0622' # لآ

# Single char ligatures (less common in plain text, more in display forms)
LAM_ALEF = '\uFEFB' # ﻻ ARABIC LIGATURE LAM WITH ALEF ISOLATED FORM
LAM_ALEF_HAMZA_ABOVE = '\uFEF7' # ﻷ ARABIC LIGATURE LAM WITH ALEF WITH HAMZA ABOVE ISOLATED FORM
LAM_ALEF_HAMZA_BELOW = '\uFEF9' # ﻹ ARABIC LIGATURE LAM WITH ALEF WITH HAMZA BELOW ISOLATED FORM
LAM_ALEF_MADDA_ABOVE = '\uFEF5' # ﻵ ARABIC LIGATURE LAM WITH ALEF WITH MADDA ABOVE ISOLATED FORM

# Extended Arabic letters (Persian, Urdu, etc. - include if analyzing broader texts)
PEH = '\u067E'   # پ
CHEH = '\u0686'  # چ
JEH = '\u0698'   # ژ
GAF = '\u06AF'   # گ

# Full set of common letters including Hamzas and variations
ARABIC_LETTERS_EXTENDED = ARABIC_ALPHABET_BASIC.union(HAMZAS).union(frozenset([TEH_MARBUTA, ALEF_MAKSURA]))


# --- Core Diacritics (Harakat) ---
FATHA = '\u064E'            # َ  ARABIC FATHA
DAMMA = '\u064F'            # ُ  ARABIC DAMMA
KASRA = '\u0650'            # ِ  ARABIC KASRA
SUKOON = '\u0652'           # ْ  ARABIC SUKOON
SHADDA = '\u0651'           # ّ  ARABIC SHADDA

CORE_DIACRITICS = frozenset([FATHA, DAMMA, KASRA, SUKOON, SHADDA])

# --- Tanweens (Nunation) ---
TANWEEN_FATH = '\u064B'     # ً  ARABIC FATHATAN
TANWEEN_DAMM = '\u064C'     # ٌ  ARABIC DAMMATAN
TANWEEN_KASR = '\u064D'     # ٍ  ARABIC KASRATAN

TANWEENS = frozenset([TANWEEN_FATH, TANWEEN_DAMM, TANWEEN_KASR])

VOWELS = frozenset([FATHA, DAMMA, KASRA])
VOWELS_TANWEEN = VOWELS.union(TANWEENS)

# --- Quranic Annotation Diacritics & Symbols (Pause Marks, Elongation, etc.) ---
# Madd (Elongation)
MADDA_ABOVE = '\u0653'      # ٓ  ARABIC MADDAH ABOVE (often combined with Shadda or on Alef)
SUPERSCRIPT_ALEF = '\u0670' # ٰ  ARABIC LETTER SUPERSCRIPT ALEF (dagger alef, for elongation)

# Small vowel signs (often for specific Quranic readings or emphasis)
SMALL_WAW = '\u06E5'        # ۥ  ARABIC SMALL WAW
SMALL_YEH = '\u06E6'        # ۦ  ARABIC SMALL YEH
SMALL_HIGH_MEEM_ISOLATED = '\u06E2' #  Isolated small meem, e.g., for Iqlab ( قلبٌ مّن )
SMALL_HIGH_SEEN = '\u06DC'  # ۜ  ARABIC SMALL HIGH SEEN (often for Saktah Laṭīfah) - Saktah Mark
SMALL_HIGH_DOTLESS_HEAD_OF_KHAH = '\u06E1' # ۡ (often indicates Hamzat al-Wasl, or Silent letter) - like a small 'ح' head

# Other Quranic symbols
SMALL_HIGH_ROUNDED_ZERO = '\u06DF'  # ۟ ARABIC SMALL HIGH ROUNDED ZERO (e.g. on a Waw or Yeh not pronounced)
SMALL_LOW_SEEN = '\u06E3'           # ﺱ ARABIC SMALL LOW SEEN (used in some traditions for Imala)
SMALL_HIGH_MADDA = '\u06E4'         # ۤ ARABIC SMALL HIGH MADDA (can indicate specific Madd types)
ARABIC_SIGN_SAJDA = '\u06E9'        # ۩ ARABIC PLACE OF SAJDAH
END_OF_AYAH = '\u06DD'              # ۝ ARABIC END OF AYAH
START_OF_RUB_EL_HIZB = '\u06DE'     # ۞ ARABIC START OF RUB EL HIZB

# --- Waqf (Stop) Marks ---
WAQF_SALA = '\u06D6'   # (ۖ) - صلى (Al-waslu awla) - Continuing preferred
WAQF_QALA = '\u06D7'   # (ۗ) - قلى (Al-waqfu awla) - Stopping preferred
WAQF_MEEM = '\u06D8'   # (ۘ) - م (Waqf Laazim / Meem letter form) - Compulsory stop
WAQF_JEEM = '\u06DA'   # (ۚ) - ج (Waqf Jaa'iz / Jeem letter form) - Permissible stop
WAQF_THREE_DOTS = '\u06DB' # (ۛ) - ∴ (Mu'anaqah) - Stop at one of two
WAQF_TAH_STOP_MARK = '\u0615' # (ؕ) - ط (Waqf Mutlaq / Tah letter form) - Absolute stop
WAQF_LA = '\u06D9'     # (ۙ) - لا (La / Laa taqif) - Forbidden stop

# Saktah (brief pause, no breath) - often SMALL_HIGH_SEEN is used.
SAKTAH_MARK_ALT = SMALL_HIGH_SEEN # ۜ (already defined)

DEFAULT_STOP_WAQF_MARKS = frozenset([
    WAQF_SALA, WAQF_QALA, WAQF_MEEM, WAQF_JEEM, WAQF_THREE_DOTS, WAQF_TAH_STOP_MARK
])
# Note: WAQF_LA is intentionally excluded from default *stop* marks as it means "do not stop".

WAQF_MARK_NAMES = {
    WAQF_SALA: "صلى (Wasl Awla)",
    WAQF_QALA: "قلى (Waqf Awla)",
    WAQF_MEEM: "م (Waqf Laazim)",
    WAQF_JEEM: "ج (Waqf Jaaiz)",
    WAQF_THREE_DOTS: "∴ (Muan`aqah)",
    WAQF_TAH_STOP_MARK: "ط (Waqf Mutlaq)",
    WAQF_LA: "لا (Forbidden Stop)",
    SAKTAH_MARK_ALT: "سكتة (Saktah)"
}


# --- Comprehensive set of ALL diacritics and Quranic annotation marks ---
ALL_DIACRITICS_AND_ANNOTATIONS = CORE_DIACRITICS.union(
    TANWEENS,
    frozenset([
        MADDA_ABOVE, SUPERSCRIPT_ALEF, SMALL_WAW, SMALL_YEH,
        SMALL_HIGH_MEEM_ISOLATED, SMALL_HIGH_SEEN, SMALL_HIGH_DOTLESS_HEAD_OF_KHAH,
        SMALL_HIGH_ROUNDED_ZERO, SMALL_LOW_SEEN, SMALL_HIGH_MADDA
    ])
)
# String version for easy checking in parsing
ALL_DIACRITICS_AND_ANNOTATIONS_STR = "".join(list(ALL_DIACRITICS_AND_ANNOTATIONS))

# --- Punctuation (Commonly used in Arabic texts) ---
ARABIC_COMMA = '\u060C'             # ،
ARABIC_SEMICOLON = '\u061B'         # ؛
ARABIC_QUESTION_MARK = '\u061F'     # ؟
ARABIC_FULL_STOP = '\u06D4'         # ۔ (less common than Western period)
# Standard Western punctuation is also often used.

# --- Honorifics and Symbols ---
SALLALLAHOU_ALAYHE_WASSALLAM = '\uFDFA' # ﷺ ARABIC LIGATURE SALLALLAHOU ALAYHE WASALLAM
RIAL_SIGN = '\uFDFC'                   # ﷼ RIAL SIGN (example of a symbol that might appear)
ORNATE_LEFT_PARENTHESIS = '\uFD3E'     # ﴾
ORNATE_RIGHT_PARENTHESIS = '\uFD3F'    # ﴿ (often used to enclose Ayah numbers or Quranic text)

# --- Digits ---
ARABIC_INDIC_DIGIT_ZERO = '\u0660' # ٠
ARABIC_INDIC_DIGIT_ONE = '\u0661'   # ١
ARABIC_INDIC_DIGIT_TWO = '\u0662'   # ٢
ARABIC_INDIC_DIGIT_THREE = '\u0663' # ٣
ARABIC_INDIC_DIGIT_FOUR = '\u0664' # ٤
ARABIC_INDIC_DIGIT_FIVE = '\u0665' # ٥
ARABIC_INDIC_DIGIT_SIX = '\u0666' # ٦
ARABIC_INDIC_DIGIT_SEVEN = '\u0667' # ٧
ARABIC_INDIC_DIGIT_EIGHT = '\u0668' # ٨
ARABIC_INDIC_DIGIT_NINE = '\u0669' # ٩

ARABIC_INDIC_DIGITS = frozenset([
    ARABIC_INDIC_DIGIT_ZERO, ARABIC_INDIC_DIGIT_ONE, ARABIC_INDIC_DIGIT_TWO,
    ARABIC_INDIC_DIGIT_THREE, ARABIC_INDIC_DIGIT_FOUR, ARABIC_INDIC_DIGIT_FIVE,
    ARABIC_INDIC_DIGIT_SIX, ARABIC_INDIC_DIGIT_SEVEN, ARABIC_INDIC_DIGIT_EIGHT,
    ARABIC_INDIC_DIGIT_NINE
])

EASTERN_ARABIC_INDIC_DIGIT_ZERO = '\u06F0' # ۰ (Persian, Urdu)
# ... and so on for Eastern Arabic digits if needed.


# --- Groupings for Tajweed Rules ---
# Qalqalah Letters (already defined, but for consistency in this section)
QALQALAH_LETTERS = frozenset([QAF, TAH_LETTER, BEH, JEEM, DAL]) # 'ق', 'ط', 'ب', 'ج', 'د'

# Letters of Tafkhim (Heaviness) - for rules like Tafkhim/Tarqiq of Ra' or Lam
LETTERS_OF_ISTILA = frozenset([KHAH, SAD, DAD, GHAIN, TAH_LETTER, QAF, ZAH]) # خص ضغط قظ

# Letters of Idgham (Assimilation) - this will vary based on the *type* of Idgham
# Example: Noon Sakinah/Tanween Idgham with Ghunnah letters
IDGHAM_WITH_GHUNNAH_LETTERS_NOON_SAKINAH = frozenset([YEH, NOON, MEEM_LETTER, WAW]) # ينمو

# Example: Noon Sakinah/Tanween Idgham without Ghunnah letters
IDGHAM_WITHOUT_GHUNNAH_LETTERS_NOON_SAKINAH = frozenset([LAM, REH]) # ل ر

# Letters of Ikhfa (Concealment) for Noon Sakinah/Tanween
# These are the remaining 15 letters after Hamza, Hah, Ain, Hah (Izhar), Ghain, Khah (Izhar),
# Baa (Iqlab), Lam, Reh (Idgham without Ghunnah), Yeh, Noon, Meem, Waw (Idgham with Ghunnah)
LETTERS_OF_IZHAR_HALQI = frozenset([HAMZA, ALEF_WITH_HAMZA_ABOVE, ALEF_WITH_HAMZA_BELOW, HAH, AIN, KHAH, GHAIN, HEH]) # ء ه ع ح غ خ (Heh often considered too)
# Typically: ء ه ع ح غ خ
# Note: `HEH` can sometimes be included depending on interpretation, `HAMZA` variants need consideration.
# For simplicity, let's use the common 6:
LETTERS_OF_IZHAR_HALQI_COMMON = frozenset([
    HAMZA, ALEF_WITH_HAMZA_ABOVE, ALEF_WITH_HAMZA_BELOW, # Representing Hamza
    HAH, AIN, KHAH, GHAIN, HEH # Heh is throat letter too.
])


# Letters that are always Muraqqaq (Light)
# ... and so on for other Tajweed groupings.

# --- String of all diacritics for parsing letter complexes ---
# This should include all characters that can attach to a letter
# but are not base letters themselves.
ARABIC_DIACRITICS_CHARS_STR = "".join(list(ALL_DIACRITICS_AND_ANNOTATIONS))
ARABIC_DIACRITICS_CHARS = ALL_DIACRITICS_AND_ANNOTATIONS # Use the frozenset for 'in' checks

# --- Complete set of characters that are considered "part of a word" but not necessarily letters ---
# This is tricky, as spaces and waqf marks break words.
# Diacritics are part of a letter complex.

# --- Whitespace and Control Characters (if needed for cleaning) ---
SPACE = ' '
TAB = '\t'
NEWLINE = '\n'
ZERO_WIDTH_NON_JOINER = '\u200C'
ZERO_WIDTH_JOINER = '\u200D'

# --- Placeholder for any character not a letter or common diacritic/symbol, useful for cleaning ---
# NON_ARABIC_SYMBOLS_OR_UNKNOWN = ...

# --- For general checking if a character is an Arabic letter (including variations) ---
def is_arabic_letter(char):
    # Range U+0600 to U+06FF covers most common Arabic block
    # Add other blocks if necessary (e.g., Arabic Presentation Forms)
    if '\u0600' <= char <= '\u06FF': # Arabic block
        # Exclude diacritics, punctuation, digits from this block if strictly "letter"
        if char not in ALL_DIACRITICS_AND_ANNOTATIONS and \
           char not in DEFAULT_STOP_WAQF_MARKS and \
           char not in ARABIC_INDIC_DIGITS and \
           char not in [ARABIC_COMMA, ARABIC_SEMICOLON, ARABIC_QUESTION_MARK, ARABIC_FULL_STOP, END_OF_AYAH]:
            return True
    if '\u0FB50' <= char <= '\uFDFF': # Arabic Presentation Forms-A (includes ﷺ, ﷼, ﴾﴿)
        # More specific checks needed if using this range for letters vs symbols
        if char in [SALLALLAHOU_ALAYHE_WASSALLAM, ORNATE_LEFT_PARENTHESIS, ORNATE_RIGHT_PARENTHESIS]: # These are symbols
            return False
        return True # Many ligatures are here
    if '\uFE70' <= char <= '\uFEFF': # Arabic Presentation Forms-B (contextual forms, ligatures like LA)
        # Most of these are contextual forms of letters or ligatures
        return True
    return False

# More specific list for parsing "base letters" (characters that can take diacritics)
BASE_ARABIC_LETTERS_FOR_PARSING = ARABIC_LETTERS_EXTENDED.union(frozenset([PEH, CHEH, JEH, GAF])) # Add any other base letters needed