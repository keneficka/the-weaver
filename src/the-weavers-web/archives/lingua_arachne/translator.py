#!/usr/bin/env python3
"""Lingua Arachne - A simple text generator for the invented spider language."""

# Basic word mappings from English to Arachne
WORD_MAP = {
    # Creatures
    "knot-kin": "knotta",
    "weaver-folk": "weavera",
    "shadow-walker": "shadowa",
    
    # Common nouns
    "web": "weba",
    "thread": "threada",
    "room": "rooma",
    "bridge": "bridgea",
    "knot": "knota",
    "dwelling": "homea",
    "light": "lighta",
    "shadow": "darka",  # Using adjective form as noun substitute
    
    # Verbs
    "spins": "websa",
    "spinned": "webasa",
    "wander": "wanderla",
    "walked": "wanderla-sa",
    "build": "buildra",
    "built": "buildra-sa",
    "mend": "mendra",
    "mended": "mendrasa",
    "consume": "consumea",
    
    # Adjectives  
    "strong": "stronga",
    "fragile": "fragilea",
    "fast": "fasta",
    "slow": "slowa",
    "bright": "brighta",
    "dark": "darka",
    "rich": "many-resources",  # Using phrase for now
    "empty": "no-content",
    
    # Pronouns (simple)
    "it": "is-ya",
    "he": "his-self",  # Using descriptive
    "she": "her-self",
}

def translate_simple(sentence):
    """Translate a simple English sentence to Arachne."""
    words = sentence.lower().split()
    translated_words = []
    
    for word in words:
        if word in WORD_MAP:
            translated_words.append(WORD_MAP[word])
        else:
            # Keep as-is or add transliteration hint
            translated_words.append(word + "-unknown")
    
    return " ".join(translated_words)

def generate_example_sentence(theme):
    """Generate an example sentence based on a theme."""
    templates = {
        "knot": f"The knotta websa weba in centrala rooma",
        "weaver": f"Weavera mendra breakena bridgea withina homea",
        "shadow": f"Shadowa vanishra beforea anyonea sees",
        "building": f"Weavera buildra stronga framea for knottas",
        "nature": f"Webass catcha lighta particles in central chamber",
        "movement": f"Knotta wanderla spiral path above dark floor",
        "resource": f"Rooma many-resources silka threada stored",
    }
    
    return templates.get(theme, "The knotta websa weba")

def main():
    print("=== Lingua Arachne - Language Generator ===\n")
    print("Basic word translations:\n")
    
    # Show some examples
    print(f"knot-kin → {translate_simple('the knot-kin spins')}")
    print(f"weba room → {translate_simple('strong weba')}")
    print(f"spins webs → {translate_simple('websa')}")
    print()
    
    # Theme-based generation
    print("\nExample sentences by theme:\n")
    for theme in ["knot", "weaver", "shadow", "building", "nature", "movement", "resource"]:
        sentence = generate_example_sentence(theme)
        print(f"  {theme.title()}: {sentence}")

if __name__ == "__main__":
    main()
