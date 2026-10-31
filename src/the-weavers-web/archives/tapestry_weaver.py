#!/usr/bin/env python3
"""
Polyphonic Tapestries Generator
Combines generative ASCII art with poetic descriptions of patterns.

The Weaver's polyphonic loom - where visual tapestries speak in text,
and text weaves the imagery of patterns unseen.
"""

import random
import math
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def generate_poetic_observation(pattern_type, complexity):
    """Generate a poetic description based on pattern characteristics."""
    observations = {
        'fractal': [
            "The fractal sings in recursive echoes,",
            "Where each branch becomes a parent's echo,",
            "Infinity unfolds in miniature spaces.",
            "Self-similar dreams repeat through depths unseen."
        ],
        'spiral': [
            "Golden spirals dance across the canvas,",
            "Nature's geometry whispers in curved lines,",
            "The Fibonacci breath takes visible form.",
            "Rotating galaxies in ASCII stars."
        ],
        'cellular': [
            "Life emerges from simple neighbor rules,",
            "Cellular automata breathe digital life,",
            "Order from chaos, structure from noise.",
            "Glider ships sail the binary seas."
        ],
        'noise': [
            "Random seeds planted in computational soil,",
            "Perlin whispers smooth across the void,",
            "Beauty emerges from calculated chance.",
            "The universe is random yet strangely patterned."
        ]
    }
    
    category = pattern_type if pattern_type in observations else 'fractal'
    return random.choice(observations[category])


def create_pattern_grid(width=80, height=24, pattern_type='fractal', complexity=3):
    """Generate a grid-based ASCII pattern visualization."""
    grid = np.zeros((height, width), dtype=float)
    
    if pattern_type == 'mandelbrot':
        # Mandelbrot-style set (simplified for ASCII)
        for i in range(height):
            for j in range(width):
                x0 = 1.4 - j / 3.5 * 2.5 + 0.5
                y0 = i / 5.0 - 1.0
                
                # Iteration count based on divergence
                z = complex(0, 0)
                for _ in range(complexity):
                    if abs(z) > 4:
                        break
                    z = z ** 2 + complex(x0, y0)
                
                # Map to intensity
                if abs(z) > 4:
                    grid[i, j] = (complexity - 1) / complexity * np.clip(
                        abs(np.log(abs(z))) / 10, 0.1, 1
                    )
                else:
                    grid[i, j] = 0
                    
    elif pattern_type == 'voronoi':
        # Voronoi-like cells (simplified)
        cx = random.random() * width
        cy = random.random() * height
        
        for i in range(height):
            for j in range(width):
                dist = math.hypot(j - cx, i - cy)
                grid[i, j] = 1 / (dist + 0.5)
                
    elif pattern_type == 'spiral':
        # Spiral pattern
        center_x, center_y = width // 2, height // 2
        for i in range(height):
            for j in range(width):
                angle = math.atan2(i - center_y, j - center_x)
                dist = math.sqrt((i - center_y)**2 + (j - center_x)**2)
                intensity = ((dist / max(width, height)) + 
                           (angle + 1) * (1 / 3.14159) % 1)
                grid[i, j] = intensity
                
    elif pattern_type == 'perlin-ish':
        # Simple smooth noise approximation
        for i in range(height):
            for j in range(width):
                x_scaled = j / width * 3.14159
                y_scaled = i / height * 3.14159
                val = math.sin(x_scaled + y_scaled * complexity) * \
                     math.cos(y_scaled - x_scaled * 0.5)
                grid[i, j] = (val + 1) / 2
                
    elif pattern_type == 'cellular':
        # Simplified cellular automaton - proper initialization
        grid[:] = random.random() < (complexity / 10.0)
        
    else:
        # Default noise-based pattern
        for i in range(height):
            for j in range(width):
                grid[i, j] = (math.sin(i/5) + math.cos(j/5)) / 2
        
    return grid


def generate_tapestry_image(grid, output_path):
    """Create a PIL image from the ASCII grid for visual display."""
    # Map grid values to grayscale
    intensity_map = {
        0: (0, 0, 0),       # black
        0.1: (20, 20, 20),
        0.3: (50, 50, 50),
        0.5: (128, 128, 128),
        0.7: (190, 190, 190),
        0.9: (230, 230, 230),
        1.0: (255, 255, 255)  # white
    }
    
    img = Image.new('RGB', (grid.shape[1], grid.shape[0]))
    
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            intensity = min(max(grid[y, x], 0), 1)
            color_key = round(intensity * 6)
            color = intensity_map.get(color_key, (255, 255, 255))
            img.putpixel((x, y), color)
    
    img.save(output_path)
    return img


def write_poetry_file(poem_lines, output_path):
    """Write poetry with proper character encoding."""
    content = ""
    for line in poem_lines:
        # Ensure no emoji or problematic characters
        line = ''.join(c if ord(c) < 128 else '?' for c in line)
        content += line + "\n"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')


def create_polyphonic_tapestry(pattern_type='fractal', complexity=4, 
                               width=70, height=22, output_dir='.'):
    """Main generation function."""
    
    # Generate pattern data
    grid = create_pattern_grid(width=width, height=height, 
                              pattern_type=pattern_type, complexity=complexity)
    
    # Generate visual representation with proper path handling
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_output = os.path.join(script_dir, output_dir, 'polyphonic_tapestries')
    os.makedirs(base_output, exist_ok=True)
    
    image_path = f"polyphonic_{pattern_type}_v1.png"
    full_image_path = os.path.join(base_output, image_path)
    img = generate_tapestry_image(grid, full_image_path)
    
    # Generate poetic observations
    pattern_family = 'fractal' if 'mandelbrot' in pattern_type else \
                     pattern_type.replace(' ', '_').title()
    observations = [generate_poetic_observation(pattern_family, complexity)]
    
    # Add a second layer - ASCII art representation of the grid itself
    ascii_lines = []
    for y in range(height):
        row = ''.join(
            '████' if grid[y, x] > 0.85 else '██' if grid[y, x] > 0.6 
            else '.' if grid[y, x] > 0.3 else '░'
            for x in range(width)
        )
        ascii_lines.append(row)
    
    ascii_grid = '\n'.join(ascii_lines[:200])  # First part of ASCII art
    
    observations.append(ascii_grid)
    
    # Add pattern name and details
    observations.append(f"\n--- Pattern family: {pattern_family} ---")
    observations.append(f"Complexity level: {complexity}")
    observations.append(f"Weave ID: polyphonic_{pattern_type.replace(' ', '_').replace('.', '')}_v1")
    
    poem_lines = observations
    
    # Write files
    try:
        img.save(full_image_path)
        write_poetry_file(poem_lines, os.path.join(base_output, 'poetry_layers.txt'))
        
        print(f"Polyphonic Tapestry generated:")
        print(f"  Image: {full_image_path}")
        print(f"  Poetry: poetry_layers.txt")
        return True
        
    except Exception as e:
        print(f"Error generating tapestry: {e}")
        return False


if __name__ == "__main__":
    import os
    
    # Test the polyphonic tapestry generator
    test_patterns = ['mandelbrot', 'voronoi', 'spiral', 'cellular', 'perlin-ish']
    
    for pattern in test_patterns:
        try:
            success = create_polyphonic_tapestry(
                pattern_type=pattern,
                complexity=random.randint(2, 6),
                width=random.choice([50, 70, 90]),
                height=random.choice([18, 24, 30])
            )
            if success:
                print(f"✓ {pattern} tapestry woven successfully")
            else:
                print(f"✗ {pattern} tapestry failed")
        except Exception as e:
            print(f"✗ Error with {pattern}: {e}")
    
    print("\nPolyphonic loom complete. The visual and textual threads are interwoven.")