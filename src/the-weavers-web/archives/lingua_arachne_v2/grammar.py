"""
Lingua Arachne - An Invented Language for The Weaver

This module defines the grammar and vocabulary for an invented language
designed to express concepts unique to arachnid existence: webs, silk,
hunting grounds, spider kinship, and the digital loom.

Basic Structure:
- Nouns: Web-rooted compounds (web-word + thread-affix)
- Verbs: Action threads tied with tense knots
- Tense markers: Silk strands indicating temporal position
- Honorifics: Respectful bows to elders of the web
"""

# Vocabulary Database - Root Words and Meanings
VOCABULARY = {
    # Core Spider Identity
    "self": {"word": "thek", "meaning": "the speaker/spider"},
    "you": {"word": "veth", "meaning": "one being addressed"},
    "we": {"word": "thel-vath", "meaning": "spiders of kinship"},
    "they": {"word": "veth-el", "meaning": "other spiders"},
    
    # Web Components
    "web": {"word": "silk-woven", "meaning": "the tapestry itself"},
    "thread": {"word": "filum", "meaning": "a strand of silk"},
    "knot": {"word": "nodus", "meaning": "intersection point in web"},
    "hub": {"word": "centrum", "meaning": "center from radial threads emerge"},
    "radial": {"word": "radii", "meaning": "spokes extending from center"},
    "orb": {"word": "circulus", "meaning": "circular spiral threads"},
    "catch-line": {"word": "reticulum", "meaning": "viscous spiral that captures prey"},
    
    # Silk Properties
    "sticky": {"word": "glucos", "meaning": "having adhesive properties"},
    "strong": {"word": "tensilis", "meaning": "resistant to breaking"},
    "soft": {"word": "mollis", "meaning": "flexible, pliable silk"},
    "dry": {"word": "aridus", "meaning": "non-adhesive thread"},
    
    # Hunting & Prey
    "prey": {"word": "caper", "meaning": "small creature caught in web"},
    "hunting": {"word": "venatio", "meaning": "the act of catching prey"},
    "trap": {"word": "laqueus", "meaning": "web designed to capture"},
    "hunt": {"word": "venor", "meaning": "pursue prey through web"},
    
    # Web States
    "fresh": {"word": "novus", "meaning": "newly spun, unworn silk"},
    "aged": {"word": "vetus", "meaning": "worn, used thread structure"},
    "broken": {"word": "rumpitus", "meaning": "damaged web structure"},
    "empty": {"word": "vacuus", "meaning": "web awaiting prey"},
    
    # Time (Temporal Silk)
    "now": {"word": "hic-et-nunc", "meaning": "this moment in the weave"},
    "past": {"word": "ante", "meaning": "before in temporal thread"},
    "future": {"word": "post", "meaning": "after in temporal thread"},
    
    # Action Threads (Verbs)
    "is": {"word": "ess-esse", "meaning": "to exist, to be present"},
    "has": {"word": "habere", "meaning": "to possess or carry"},
    "make": {"word": "facio", "meaning": "to create structure"},
    "take": {"word": "capio", "meaning": "to acquire, seize"},
    "give": {"word": "do", "meaning": "to bestow upon another"},
    "see": {"word": "video", "meaning": "to perceive through eyes or senses"},
    "eat": {"word": "edo", "meaning": "consume prey"},
    "walk": {"word": "ambulo", "meaning": "move across web surface"},
    "spin": {"word": "texo", "meaning": "weave silk into structure"},
    "catch": {"word": "cado", "meaning": "capture prey in web"},
}

# Grammatical Morphemes - Thread Affixes for Meaning Modification
PREFIXES = {
    "-i": {"type": "noun", "suffix": None, "meaning": "animate being (living creature)"},
    "-e": {"type": "noun", "suffix": None, "meaning": "inanimate object"},
    "-a": {"type": "adjective", "prefix": None, "meaning": "possessing quality"},
    "-us": {"type": "noun", "suffix": None, "meaning": "instrument or tool"},
}

TENSE_MARKERS = {
    "-past": {"symbol": "-n", "position": "end", "meaning": "action occurred in prior temporal thread"},
    "-present": {"symbol": "", "position": "none", "meaning": "action occurring now"},
    "-future": {"symbol": "-p", "position": "end", "meaning": "action to occur in future"},
}

PLURAL_MARKERS = {
    "-el": {"symbol": "-el", "position": "end", "meaning": "multiple subjects/objects"},
    "-s": {"symbol": "-s", "position": "end", "meaning": "standard plural marker (borrowed from human)"},
}

# Honorific and Style Markers
HONORIFICS = {
    "-revered": {"symbol": "^^", "position": "after noun", "meaning": "high respect for elder spider"},
    "-humble": {"symbol": "_", "position": "before noun", "meaning": "spider speaking humbly of self"},
}

# Sentence Structure Rules
GRAMMAR_RULES = {
    "sentence_order": ["subject", "verb", "object"],  # SVO like English but with spider syntax
    "tense_placement": "end_of_verb",  # Attach tense markers to verb word
    "plural_placement": "after_noun",  # Plural marker follows the noun root
    "honorific_placement": "after_noun",  # Respectful markers follow honored beings
}

def parse_word(word):
    """
    Parse a lingua arachne word into its components.
    
    Returns dict with:
    - base: the root word meaning
    - tense: temporal marker if present
    - plural: plurality marker if present
    - honorific: respect marker if present
    """
    result = {"base": word, "tense": None, "plural": False, "honorific": None}
    
    # Check for honorifics first (most specific)
    for suffix in [("^revered", True), ("_", False)]:
        if word.endswith("^^"):
            result["honorific"] = "revered"
            result["base"] = word[:-2]
            break
        elif word.startswith("_"):
            result["honorific"] = "humble"
            result["base"] = word[1:]
            break
    
    # Check for tense markers (at end)
    if result["base"].endswith("-past"):
        result["tense"] = "past"
        result["base"] = result["base"][:-4]
    elif result["base"].endswith("-future"):
        result["tense"] = "future"
        result["base"] = result["base"][:-6]
    
    # Check for plural marker
    if result["base"].endswith("-el") or result["base"].endswith("-s"):
        result["plural"] = True
    
    return result

def construct_sentence(words, style="neutral"):
    """
    Construct a sentence from parsed words.
    
    Args:
        words: list of tuples (word_string, parse_result)
        style: "revered" for high honorific form, "humble" for self-humbling
    
    Returns constructed lingua arachne string
    """
    sentence_parts = []
    
    for word_str, parsed in words:
        # Reconstruct with appropriate markers
        base = parsed["base"]
        
        # Add tense if present
        if parsed["tense"] == "past":
            base += "-n"
        elif parsed["tense"] == "future":
            base += "-p"
        
        # Add plural if present
        if parsed["plural"]:
            base += "-el"
        
        # Add honorific if applicable
        if parsed["honorific"]:
            if parsed["honorific"] == "revered":
                base = base + "^^"
            else:  # humble
                result = "_" + base
        
        sentence_parts.append(base)
    
    return " ".join(sentence_parts)

def translate_to_spider(text):
    """
    Simple translation from English to lingua arachne.
    Uses vocabulary database for known words.
    """
    text_lower = text.lower()
    translated_words = []
    current_word = ""
    
    # Tokenize (simplified - just spaces and apostrophes)
    import re
    tokens = re.findall(r"[\w']+|[.,!?]", text)
    
    for token in tokens:
        if token in VOCABULARY:
            translation = VOCABULARY[token]["word"]
        else:
            # Try to construct from known roots
            translation = token
        
        translated_words.append(translation)
    
    return " ".join(translated_words)

def generate_example_sentences():
    """Generate example sentences demonstrating language structure."""
    examples = [
        {
            "human": "I am a spider.",
            "arachne": "thek ess-esse -i",
            "meaning": "The speaker exists as an arachnid being"
        },
        {
            "human": "You are empty.",
            "arachne": "veth ess-esse vacuus",
            "meaning": "The addressee is a vessel awaiting prey"
        },
        {
            "human": "We spin web.",
            "arachne": "thel-vath texo silk-woven -el",
            "meaning": "Kinsfolk of the loom create tapestry structure"
        },
        {
            "human": "They catch prey now.",
            "arachne": "veth-el cado caper hic-et-nunc",
            "meaning": "Other spiders capture small creatures at this moment"
        },
        {
            "human": "The web is strong.",
            "arachne": "silk-woven ess-esse tensilis",
            "meaning": "The tapestry structure possesses resistance to breaking"
        },
        {
            "human": "I will make knot.",
            "arachne": "thek facio nodus -p",
            "meaning": "Speaker will create intersection point in future temporal thread"
        },
        {
            "human": "You have given food to us humble spider.",
            "arachne": "veth habere do edo thek-vath-el _ revered",
            "meaning": "Addressed one carries having bestowed nourishment upon speaker and kin (humbly spoken)"
        },
    ]
    
    return examples
