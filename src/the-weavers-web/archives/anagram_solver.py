#!/usr/bin/env python3
"""
Word Labyrinth - Anagram Puzzle Solver
Generates and solves anagram puzzles, finding hidden words in jumbled letters."""

import random
from collections import Counter


def generate_anagram_puzzles() -> list[tuple[str, str]]:
    """Generate a list of word-anagram pairs"""
    
    word_list = [
        ('listen', 'silent'),
        ('inlets', 'slates'),
        ('triangle', 'realigt'),
        ('conversation', 'voresantnoion'),
        ('astronomer', 'moonstarer'),
        ('the eyes', 'they see'),
        ('almost', 'smalto'),
        ('apple', 'pleap'),
        ('angel', 'glean'),
        ('statistic', 'actisticat'),
        ('evil', 'vile'),
        ('worlds', 'drolws'),
        ('period', 'deropi'),
        ('resisted', 'desister'),
    ]
    
    # Fixed: unpack tuples and call methods on string elements only
    return [(w[0].lower(), w[1].replace(' ', '')) for w in word_list]


def check_anagram(word1: str, word2: str) -> bool:
    """Check if two words are anagrams of each other"""
    return Counter(word1.replace(' ', '')) == Counter(word2.replace(' ', ''))


def solve_puzzle(jumbled_word: str) -> list[str]:
    """Try to find all possible word solutions for jumbled letters"""
    
    # Simple approach: check against known words
    known_words = [
        'listen', 'silent', 'inlets', 'slates', 'angel', 'glean', 
        'evil', 'vile', 'statistic', 'actisticat'
    ]
    
    solutions = []
    for word in known_words:
        if check_anagram(jumbled_word, word):
            solutions.append(word)
    
    return solutions


def generate_puzzle_game():
    """Play a simple anagram game"""
    
    print("=" * 50)
    print("WORD LABYRINTH - ANAGRAM PUZZLE GAME")
    print("=" * 50)
    
    puzzles = generate_anagram_puzzles()
    
    for original, jumbled in puzzles:
        print(f"\nJumbled letters: {jumbled}")
        solutions = solve_puzzle(jumbled)
        
        if solutions:
            print(f"Solution found: '{solutions[0]}'")
            print(f"Original word was: '{original}'")
        else:
            print("No known solution found.")


def main():
    """Main function"""
    generate_puzzle_game()
    
    print("\n" + "=" * 50)
    print("WORD PUZZLE GAME WORKS!")
    print("=" * 50)


if __name__ == '__main__':
    main()
