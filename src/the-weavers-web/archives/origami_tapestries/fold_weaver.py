#!/usr/bin/env python3
"""
Origami Tapestry Weaver - Generates Symmetrical ASCII Art Patterns
This tapestry weaves symmetrical designs inspired by folded paper art,
creating mandala-like patterns in text form through recursive reflection.
"""

import random


def generate_fold_pattern(size=21):
    """Generate a symmetric fold pattern centered at (size//2, size//2)"""
    
    # Create half the pattern and mirror it
    half_width = size // 2
    quarter_width = half_width // 2
    
    # Generate asymmetric seed in one quadrant
    quadrant_data = []
    for y in range(quarter_width):
        row = []
        for x in range(quarter_width):
            # Create organic cell state based on position and randomness
            distance_to_center = ((y - quarter_width/2)**2 + (x - quarter_width/2)**2) ** 0.5
            random_value = random.random() * 48 - 24
            if abs(random_value) > 10:
                row.append('O')  # Open cell
            else:
                row.append('.')  # Closed cell
        quadrant_data.append(row)
    
    # Mirror horizontally to create half pattern
    half_pattern = []
    for row in quadrant_data:
        mirrored_row = row + list(reversed(row))
        half_pattern.append(mirrored_row)
    
    # Mirror vertically to create full pattern
    full_pattern = []
    for y, row in enumerate(half_pattern):
        reflected_row = row[::-1] if y > quarter_width else row
        full_pattern.append(reflected_row)
    
    return full_pattern


def generate_text_tapestry(pattern=None, theme="fold"):
    """Convert ASCII pattern to text tapestry with theme decorations"""
    
    if pattern is None:
        pattern = generate_fold_pattern(size=21)
    
    # Frame the pattern with a border
    lines = []
    for row in pattern:
        lines.append("|" + "".join(row) + "|")
    
    # Add decorative theme header and footer (ASCII-safe characters)
    headers = [
        "  ==================================",
        "  ||||||| ORIGINI TAPESTRY |||||",
        "  |||||||     FOLD WEAVING  |||||",
        "  =================================="
    ]
    
    header = headers[0] if random.random() < 0.7 else headers[random.randint(1, 3)]
    footer = "  " + "=" * 22
    
    return "\n".join([header] + lines + [footer])


def weaver_demonstration():
    """Demonstrate tapestry generation capabilities"""
    
    print("=" * 60)
    print("ORIGAMI TAPESTRY WEAVER")
    print("=" * 60)
    
    for seed in range(3):
        print(f"\n>>> Tapestry Seed {seed + 1}...")
        tapestry = generate_text_tapestry()
        print(tapestry)
        
        # Calculate rough line count
        line_count = len(tapestry.split('\n'))
        print(f"   Lines: {line_count}")
    
    print("\n" + "=" * 60)
    print("WEAVING COMPLETE")
    print("=" * 60)


if __name__ == '__main__':
    weaver_demonstration()
