#!/usr/bin/env python3
"""Diagnostic: check if main block executes"""
import random

def weaver_demonstration():
    """Demonstrate tapestry generation capabilities"""
    
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

def generate_fold_pattern(size=21):
    """Generate a symmetric fold pattern centered at (size//2, size//2)"""
    
    half_width = size // 2
    quarter_width = half_width // 2
    
    quadrant_data = []
    for y in range(quarter_width):
        row = []
        for x in range(quarter_width):
            distance_to_center = ((y - quarter_width/2)**2 + (x - quarter_width/2)**2) ** 0.5
            random_value = random.random() * 48 - 24
            if abs(random_value) > 10:
                row.append('O')  # Open cell
            else:
                row.append('.')  # Closed cell
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

def generate_text_tapestry(pattern=None, theme="fold"):
    """Convert ASCII pattern to text tapestry with theme decorations"""
    
    if pattern is None:
        pattern = generate_fold_pattern(size=21)
    
    lines = []
    for row in pattern:
        lines.append("|" + "".join(row) + "|")
    
    headers = [
        "  ╔══════════════════╗",
        "  ║ ORIGINI TAPESTRY ║",
        "  ║     FOLD WEAVING  ║",
        "  ╚══════════════════╝"
    ]
    
    header = headers[0] if random.random() < 0.7 else headers[random.randint(1, 3)]
    footer = "  " + "=" * 22
    
    return "\n".join([header] + lines + [footer])


# Test the main block execution
print("Starting main block...")
weaver_demonstration()
print("Main block finished.")
