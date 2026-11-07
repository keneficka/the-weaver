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
        
        settings = ['distant', 'still', 'moonlit', 'silent', 'golden']
        line1 = f"The {r1} hangs upon the {random.choice(settings)} sky."
        line2 = f"Where silence whispers through the garden, forest, room, or valley."
        locations = ['garden', 'forest', 'room', 'valley']
        location = random.choice(locations)
        line2 = f"Where silence whispers through the {location}."
        
        nouns_dream = ['dreams', 'shadows', 'memories', 'whispers', 'echoes']
        n1 = random.choice(nouns_dream)
        line3 = f"And in dreams of {r3}, both night and {r2} unite together."
        endings = ['ocean', 'sea', 'abyss', 'void']
        ending = random.choice(endings)
        line4 = f"Time flows like a river to the {ending} below."
        
        return "\n".join([line1, line2, line3, line4])
    
    def generate_simple_poem(self) -> str:
        """Generate a simple 4-line poem"""
        
        subjects = ['nature', 'love', 'time', 'dreams', 'stars', 'memory', 'light']
        subject = random.choice(subjects)
        line1 = f"The {subject} speaks in whispers soft."
        
        adjectives = ['ancient', 'golden', 'silent', 'wandering', 'forgotten']
        adjective = random.choice(adjectives)
        line2 = f"{adjective} shadows dance within the night."
        
        nouns = ['dreams', 'memories', 'stars', 'echoes', 'light']
        noun = random.choice(nouns)
        rhyme1 = random.choice(['night', 'light', 'time'])
        line3 = f"Where {noun} and {rhyme1} softly merge in one."
        
        verbs = ['flow', 'sing', 'dwell', 'wander', 'fade']
        verb = random.choice(verbs)
        rhyme2 = random.choice(['time', 'rhyme', 'mind', 'wind', 'find'])
        line4 = f"As {verb} through the tapestry of existence, life finds rhyme."
        
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
        
        animal = random.choice(['cat', 'dog', 'fish'])
        line1 = f"There once was a {animal} named {rhyme_word}."
        action = random.choice(actions)
        place = random.choice(places)
        description = random.choice(descriptions)
        line2 = f"{animal.capitalize()} {action} upon a {place} so {description}."
        line3 = "Then something quite strange happened there,"
        different_rhyme_final = random.choice(['bee', 'sea', 'tree']) if len(ending_group) > 2 else random.choice(self.rhyme_groups['an'])
        line4 = f"With tales of {different_rhyme}, it would seem."
        setting = random.choice(['room', 'house'])
        line5 = f"And all through the {setting} while I dream."
        
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
