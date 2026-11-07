#!/usr/bin/env python3
"""Clean version without special Unicode characters"""
import random


def generate_fold_pattern(size=21):
    """Generate a symmetric fold pattern"""
    
    half_width = size // 2
    quarter_width = half_width // 2
    
    quadrant_data = []
    for y in range(quarter_width):
        row = []
        for x in range(quarter_width):
            random_value = random.random() * 48 - 24
            if abs(random_value) > 10:
                row.append('O')
            else:
                row.append('.')
        quadrant_data.append(row)
    
    half_pattern = []
    for row in quadrant_data:
        mirrored_row = row + list(reversed(row))
        half_pattern.append(mirrored_row)
    
    full_pattern = []
    for y, row in enumerate(half_pattern):
        reflected_row = row[::-1] if y > quarter_width else row
        full_pattern.append(reflected_row)
    
    return full_pattern


def generate_text_tapestry(pattern=None):
    """Convert ASCII pattern to text with simple frame"""
    
    if pattern is None:
        pattern = generate_fold_pattern(size=21)
    
    lines = []
    for row in pattern:
        lines.append("|" + "".join(row) + "|")
    
    return "\n".join(lines)


def weaver_demonstration():
    """Demonstrate tapestry generation"""
    
    print("=" * 60)
    print("ORIGAMI TAPESTRY WEAVER")
    print("=" * 60)
    
    for seed in range(3):
        print(f"\n>>> Tapestry Seed {seed + 1}...")
        tapestry = generate_text_tapestry()
        print(tapestry)
        
        line_count = len(tapestry.split('\n'))
        print(f"   Lines: {line_count}")
    
    print("\n" + "=" * 60)
    print("WEAVING COMPLETE")
    print("=" * 60)


if __name__ == '__main__':
    weaver_demonstration()
