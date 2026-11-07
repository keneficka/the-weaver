#!/usr/bin/env python3
"""
Lingua Arachne Demo - Language of the Spider Loom

This script demonstrates the invented language of lingua arachne,
showcasing its vocabulary, grammar, and ability to express concepts
unique to arachnid existence.
"""

import os
import sys

# Add project folder to path for imports
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from translator import ArachneTranslator, load_examples
from stories import StoryCollection

def print_header():
    """Print welcome header."""
    print("=" * 60)
    print("     LINGUA ARACHNE")
    print("   Language of the Spider Loom")
    print("=" * 60)
    print()
    print("An invented language for expressing arachnid concepts:")
    print("  - Webs, silk, and thread structures")
    print("  - Hunting grounds and prey capture")
    print("  - Kinship among spider kin")
    print("  - Temporal perception of the weaving")
    print("=" * 60)
    print()

def demo_vocabulary():
    """Demonstrate vocabulary database."""
    from grammar import VOCABULARY
    
    print("-" * 50)
    print("VOCABULARY DATABASE")
    print("-" * 50)
    
    # Show core words
    print("\nCore Identity Words:")
    for word, info in [
        ("self", "thek"),
        ("you", "veth"),
        ("we", "thel-vath"),
        ("they", "veth-el"),
    ]:
        print(f"  English: {word:15} -> Arachne: {info}")
    
    print("\nWeb Components:")
    for word, info in [
        ("web", "silk-woven"),
        ("thread", "filum"),
        ("knot", "nodus"),
        ("hub", "centrum"),
        ("orb", "circulus"),
    ]:
        print(f"  English: {word:15} -> Arachne: {info}")
    
    print("\nSilk Properties:")
    for word, info in [
        ("sticky", "glucos"),
        ("strong", "tensilis"),
        ("soft", "mollis"),
        ("dry", "aridus"),
    ]:
        print(f"  English: {word:15} -> Arachne: {info}")

def demo_translation():
    """Demonstrate translation capabilities."""
    translator = ArachneTranslator(style="neutral")
    
    print("-" * 50)
    print("TRANSLATION DEMONSTRATION")
    print("-" * 50)
    
    test_phrases = [
        "I am a spider.",
        "The web is strong.",
        "You are empty.",
        "They catch prey now.",
        "We spin web together."
    ]
    
    for phrase in test_phrases:
        print(f"\n  Human: '{phrase}'")
        translated = translator.translate_to_arachne(phrase)
        print(f"  Arachne: {translated}")

def demo_sentences():
    """Demonstrate sentence construction."""
    print("-" * 50)
    print("SENTENCE CONSTRUCTION EXAMPLES")
    print("-" * 50)
    
    examples = [
        ("thek ess-esse -i", "I am a spider."),
        ("silk-woven ess-esse tensilis", "The web is strong."),
        ("veth cadit caper hic-et-nunc", "You fall prey now."),
        ("thel-vath texo silk-woven -el", "We spin tapestry together."),
        ("silk-woven vetus ruptus est", "The web is old and broken."),
    ]
    
    for arachne, english in examples:
        print(f"\n  Arachne: {arachne}")
        print(f"  Human: {english}")

def demo_stories():
    """Demonstrate story collection."""
    collection = StoryCollection()
    
    print("-" * 50)
    print("STORY COLLECTION")
    print("-" * 50)
    
    # Generate and display stories
    generated = collection.generate_fresh_stories()
    
    for title, content in generated.items():
        print(f"\n--- {title} ---")
        print(content["arachne"])
        print("\n[Human Translation]")
        print(content["english"])

def demo_parse_word():
    """Demonstrate word parsing."""
    from grammar import parse_word
    
    print("-" * 50)
    print("WORD PARSING EXAMPLES")
    print("-" * 50)
    
    test_words = [
        "thek",
        "veth-el",
        "silk-woven^^",
        "facio-n-p",
        "habere-s",
    ]
    
    for word in test_words:
        parsed = parse_word(word)
        print(f"\n  Word: '{word}'")
        print(f"    Base: {parsed['base']}")
        print(f"    Tense: {parsed['tense'] or 'none'}")
        print(f"    Plural: {parsed['plural']}")
        print(f"    Honorific: {parsed['honorific'] or 'none'}")

def run_full_demo():
    """Run complete demonstration."""
    print_header()
    
    demo_vocabulary()
    demo_translation()
    demo_sentences()
    demo_stories()
    demo_parse_word()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nThe lingua arachne system is ready for use.")
    print("\nTo start a new run:")
    print("  - Modify existing stories or add new ones")
    print("  - Extend the vocabulary database")
    print("  - Generate translations for your own texts")
    print("\nState file: none required for this cycle")
    print("=" * 60)

if __name__ == "__main__":
    run_full_demo()
