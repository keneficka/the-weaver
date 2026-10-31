#!/usr/bin/env python3
"""
Simple Maze Generator - no interactivity, pure generation demo
"""

import random


def generate_maze(width: int, height: int, seed: int = None) -> str:
    """Generate ASCII maze using recursive backtracking"""
    
    if seed is not None:
        random.seed(seed)
    
    # Grid dimensions (odd for proper walls)
    w = (width - 1) // 2 * 2 + 1
    h = (height - 1) // 2 * 2 + 1
    
    # Initialize with all walls
    grid = [[[1, 1, 1] for _ in range(w)] for _ in range(h)]
    
    # Starting point
    x, y = 1, 1
    grid[y][x] = [0, 1, 0]
    
    stack = [(x, y)]
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    
    while stack:
        x, y = stack[-1]
        
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 1 <= nx < w and 1 <= ny < h:
                if grid[ny][nx] == [1, 1, 1]:
                    neighbors.append((nx, ny, dx, dy))
        
        if neighbors:
            nx, ny, dx, dy = random.choice(neighbors)
            
            # Remove wall between cells
            grid[y + dy // 2][x + dx // 2] = [0, 1, 0]
            grid[ny][nx] = [0, 1, 0]
            
            stack.pop()
            x, y = nx, ny
        
        if not neighbors:
            stack.pop()
    
    # Convert to ASCII
    lines = []
    for row in grid:
        line = ''
        for vals in row:
            if vals == [1, 1, 1]:
                line += '###'
            else:
                line += '#' + ('#' if vals[0] else ' ') + '#'
        lines.append(line)
    
    return '\n'.join(lines)


def main():
    """Demo maze generation"""
    print("=" * 50)
    print("MAZE GENERATION DEMO")
    print("=" * 50)
    
    mazes = [
        (31, 15, 42),
        (31, 15, 123),
        (31, 15, 999),
        (41, 21, 7),
        (41, 21, 456)
    ]
    
    for i, (w, h, seed) in enumerate(mazes):
        print(f"\n*** MAZE {i+1} ({w}x{h}, seed={seed}) ***")
        maze = generate_maze(w, h, seed)
        print(maze)
    
    print("\n" + "=" * 50)
    print("ALL MAZES GENERATED SUCCESSFULLY!")
    print("=" * 50)


if __name__ == '__main__':
    main()
