#!/usr/bin/env python3
"""
Word Lattice - A language puzzle game
Build sentences from word tiles and explore linguistic patterns.
"""

import random


VOCAB = [
    # Short words
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
    'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
    
    # Medium length  
    'said', 'was', 'some', 'were', 'they', 'but', 'will', 'my', 'all',
    'would', 'there', 'when', 'out', 'other', 'into', 'can', 'what',
    
    # Nouns
    'dream', 'forest', 'river', 'sky', 'city', 'mountain', 'ocean', 
    'star', 'flower', 'bird', 'wolf', 'moon', 'castle', 'dragon',
    
    # Adjectives
    'bright', 'dark', 'quiet', 'loud', 'cold', 'warm', 'soft', 'hard',
    'quick', 'slow', 'tall', 'short', 'happy', 'sad', 'brave', 'kind',
    
    # Longer descriptive words
    'beautiful', 'forgotten', 'melancholy', 'ancient', 'whispering'
]

CONNECTORS = ['and', 'or', 'but']
SENTENCE_ENDINGS = ['.']


def generate_sentence():
    """Create a sentence by combining random word tiles."""
    nouns = ['dream', 'forest', 'river', 'sky', 'city', 'mountain', 'ocean', 
             'star', 'flower', 'bird', 'wolf', 'moon', 'castle', 'dragon']
    
    # Randomly decide sentence complexity
    complexity = random.random()
    
    if complexity < 0.3:
        # Very simple: single noun with maybe adjective
        adj = random.choice([a for a in VOCAB[19:] if len(a) < 4]) if random.random() < 0.5 else ''
        noun = random.choice(nouns)
        sentence = f"{adj} {noun}" if adj else noun
    
    elif complexity < 0.6:
        # Two parts with connector
        noun1 = random.choice(nouns)
        connector = random.choice(CONNECTORS)
        noun2 = random.choice(nouns)
        adjective = random.choice([a for a in VOCAB[19:] if len(a) < 4])
        sentence = f"{adjective} {noun1} and {noun2}"
    
    else:
        # More complex with verb or preposition
        options = [
            f"the {random.choice(nouns)} was {random.choice(['bright', 'dark', 'quiet'])}",
            f"a {random.choice([a for a in VOCAB[19:] if len(a) < 4])} {random.choice(nouns)}",
            f"under the {random.choice(nouns)}",
            f"in the {random.choice(nouns)}"
        ]
        sentence = random.choice(options)
    
    # Randomly add period or not
    return sentence + random.choice(SENTENCE_ENDINGS) if random.random() < 0.8 else sentence


def generate_multiple_sentences(count=5):
    """Generate multiple sentences."""
    sentences = [generate_sentence() for _ in range(count)]
    return "\n".join(sentences)


def run_word_lattice_demo():
    """Main demonstration of the word lattice puzzle game."""
    print("=" * 40)
    print("WORD LATTICE PUZZLE")
    print("Generated sentences from word combinations")
    print("=" * 40)
    
    for i in range(5):
        sentence = generate_sentence()
        print(f"\nSentence {i+1}:")
        print(sentence)


if __name__ == '__main__':
    run_word_lattice_demo()
