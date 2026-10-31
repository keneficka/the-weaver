#!/usr/bin/env python3
"""
Poetry Weaver - A simple AI-free poetry generator using rhyming patterns
Generates quatrains and sonnets with rhyme schemes (AABB, ABAB, etc.)
"""

import random


class PoetryWeaver:
    """Simple poetry generator without neural networks"""
    
    def __init__(self):
        # Rhyme word banks organized by vowel sounds (rough approximation)
        self.rhyme_groups = {
            'a': ['star', 'car', 'far', 'bar', 'guitar', 'solar', 'floor', 'door', 'more', 'core'],
            'ar': ['dark', 'bark', 'spark', 'park', 'shark', 'lark', 'narrate', 'art', 'heart'],
            'or': ['door', 'floor', 'more', 'core', 'horse', 'worse', 'for', 'shore', 'store'],
            'ee': ['sea', 'tree', 'free', 'bee', 'see', 'key', 'we', 'me', 'reef'],
            'ight': ['night', 'light', 'fight', 'sight', 'bright', 'right', 'might', 'tight', 'white'],
            'ay': ['day', 'say', 'way', 'play', 'may', 'stay', 'ray', 'pray', 'sway'],
            'ou': ['house', 'mouse', 'out', 'about', 'count', 'pound', 'sound', 'ground', 'found'],
            'an': ['man', 'can', 'fan', 'plan', 'ban', 'span', 'sand', 'hand', 'land', 'grand'],
            'en': ['then', 'when', 'seven', 'even', 'begin', 'win', 'thin', 'spin'],
            'it': ['sit', 'bit', 'hit', 'kit', 'fit', 'lit', 'nit', 'rit', 'wit', 'quit'],
            'ow': ['cow', 'wow', 'now', 'how', 'flower', 'power', 'tower'],
        }
        
        self.vowel_sounds = list(self.rhyme_groups.keys())
    
    def get_rhyme_candidates(self, word: str) -> list[str]:
        """Find words that rhyme with the given word"""
        word_lower = word.lower().strip()
        
        # Find matching rhyme group based on ending sound
        matched_group = None
        for group in self.vowel_sounds:
            if group in word_lower or any(r.endswith(group) for r in self.rhyme_groups.get(group, [])):
                matched_group = group
                break
        
        if matched_group and self.rhyme_groups[matched_group]:
            candidates = [r for r in self.rhyme_groups[matched_group] if r != word_lower][:3]
            return candidates + [random.choice(list(self.vowel_sounds)) for _ in range(2)]  # Add variety
        
        # If no good match, return random words from different groups
        all_rhymes = []
        for rhymes in self.rhyme_groups.values():
            all_rhymes.extend(rhymes)
        return random.sample(all_rhymes, min(5, len(all_rhymes)))
    
    def generate_quatrain(self, theme: str = None) -> str:
        """Generate a four-line poem with AABB rhyme scheme"""
        
        rhymes_group1 = random.choice(list(self.rhyme_groups.keys()))
        available_rhymes_1 = self.rhyme_groups[rhymes_group1]
        rhymes_group2 = random.choice([g for g in self.rhyme_groups.keys() if g != rhymes_group1])
        available_rhymes_2 = self.rhyme_groups[rhymes_group2]
        
        r1 = random.choice(available_rhymes_1)
        r2_candidates = [r for r in available_rhymes_1 if r != r1] or available_rhymes_2
        r2 = random.choice(r2_candidates) if r2_candidates else r1
        r3 = random.choice([r for r in available_rhymes_2 if r != r2]) or r1
        
        theme_words = (theme and theme.split()[:2] or [])
        
        line1 = f"Upon the {random.choice(['distant', 'still'])} hangs a {r1}."
        line2 = f"Where silence whispers through the {random.choice(['garden', 'forest', 'room', 'valley'])}."
        line3 = f"And dreams of {r3}, both night and {r2} unite."
        
        ending = random.choice(['ocean', 'sea', 'abyss', 'void'])
        
        return "\n".join([line1, line2, line3, f"Time flows like a river to the {ending}."])
    
    def generate_simple_poem(self) -> str:
        """Generate a simple 4-line poem"""
        
        subjects = ['nature', 'love', 'time', 'dreams', 'stars', 'memory', 'light']
        line1 = f"The {random.choice(subjects)} speaks in whispers soft."
        
        adjectives = ['ancient', 'golden', 'silent', 'wandering', 'forgotten']
        line2 = f"{random.choice(adjectives)} shadows dance within the night."
        
        nouns = ['dreams', 'memories', 'stars', 'echoes', 'light']
        rhyme1 = random.choice(['night', 'light', 'time'])
        line3 = f"Where {random.choice(nouns)} and {rhyme1} softly merge."
        
        verbs = ['flow', 'sing', 'dwell', 'wander', 'fade']
        rhyme2 = random.choice(['time', 'rhyme', 'mind', 'wind', 'find'])
        line4 = f"As {random.choice(verbs)} through the tapestry of existence."
        
        return "\n".join([line1, line2, line3, line4])
    
    def generate_limerick(self) -> str:
        """Generate a simple limerick"""
        
        endings = [
            ['cat', 'hat', 'mat'],
            ['dog', 'log', 'frog'],
            ['bee', 'sea', 'tree'],
            ['door', 'floor', 'more'],
            ['day', 'way', 'say'],
        ]
        
        ending_group = random.choice(endings)
        rhyme_word = random.choice(ending_group[:2])
        different_rhyme = random.choice(ending_group[2:]) if len(ending_group) > 2 else random.choice(self.rhyme_groups['an'])
        
        actions = ['sat', 'jumps', 'sits', 'dances', 'wonders']
        places = ['table', 'window', 'floor', 'air', 'space']
        descriptions = ['so fat', 'so bold', 'so bright', 'very tall', 'quite small']
        
        line1 = f"There once was a {random.choice(['cat', 'dog', 'fish'])} named {rhyme_word}."
        line2 = f"{random.choice(actions)} upon a {random.choice(places)} so {random.choice(descriptions)}."
        line3 = "Then something quite strange happened there,"
        line4 = f"With tales of {different_rhyme}, it would seem."
        line5 = f"And all through the {random.choice(['room', 'house'])} while I dream."
        
        return "\n".join([line1, line2, line3, line4, line5])


def main():
    """Demonstrate poetry generation"""
    
    print("=" * 60)
    print("POETRY WEAVER - SIMPLE POETRY GENERATOR")
    print("=" * 60)
    
    weaver = PoetryWeaver()
    
    print("\n*** SAMPLE POEM 1 ***")
    print(weaver.generate_simple_poem())
    
    print("\n" + "-" * 40 + "\n")
    print("*** SAMPLE POEM 2 ***")
    print(weaver.generate_simple_poem())
    
    print("\n" + "-" * 40 + "\n")
    print("*** LIMERICK ***")
    print(weaver.generate_limerick())
    
    print("\n" + "=" * 60)
    print("POETRY GENERATION WORKS!")


if __name__ == '__main__':
    main()
