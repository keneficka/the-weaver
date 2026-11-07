#!/usr/bin/env python3
"""Simple test of fold logic"""
import random

def main():
    print("Testing simple fold...")
    
    size = 5
    half_width = size // 2
    quarter_width = half_width // 2
    
    quadrant_data = []
    for y in range(quarter_width):
        row = []
        for x in range(quarter_width):
            random_value = random.random() * 48 - 24
            if abs(random_value) > 10:
                cell = 'O'
            else:
                cell = '.'
            row.append(cell)
        quadrant_data.append(row)
    
    print(f"Quadrant ({quarter_width}x{quarter_width}):")
    for row in quadrant_data:
        print(" ".join(row))
    
    return 42

if __name__ == '__main__':
    main()
