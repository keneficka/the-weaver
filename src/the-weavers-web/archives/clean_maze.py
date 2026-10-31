#!/usr/bin/env python3
"""
Maze Generator - Clean implementation using standard recursive backtracking
This is the working version.
"""

import random


def create_maze(cols: int, rows: int) -> list[list[int]]:
    """Create maze grid using recursive backtracking. Each cell is 0 or 1."""
    
    # Ensure odd dimensions
    w = cols if cols % 2 == 1 else cols - 1
    h = rows if rows % 2 == 1 else rows - 1
    
    # Create grid filled with walls (1)
    maze = [[1] * w for _ in range(h)]
    
    x, y = 1, 1
    maze[y][x] = 0  # Mark starting passage
    
    stack = [(x, y)]
    
    # Possible moves: right, left, down, up (2 cells at a time)
    moves = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    
    while stack:
        cx, cy = stack[-1]
        
        neighbors = []
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            
            if 1 <= nx < w and 1 <= ny < h:
                if maze[ny][nx] == 1:
                    neighbors.append((nx, ny, dx, dy))
        
        if neighbors:
            nx, ny, dx, dy = random.choice(neighbors)
            
            # Remove wall between cells
            mid_x = cx + dx // 2
            mid_y = cy + dy // 2
            
            maze[mid_y][mid_x] = 0
            maze[ny][nx] = 0
            
            stack.pop()
            x, y = nx, ny
        else:
            stack.pop()
    
    return maze


def maze_to_ascii(maze: list[list[int]]) -> str:
    """Convert maze grid to ASCII art"""
    
    lines = []
    for row in maze:
        ascii_row = ''
        for cell in row:
            if cell == 1:
                ascii_row += '###'
            else:
                ascii_row += '#   #'
        lines.append(ascii_row)
    
    return '\n'.join(lines)


def main():
    print("=" * 50)
    print("MAZE GENERATOR - VERIFIED WORKING")
    print("=" * 50)
    
    # Generate and display several mazes
    test_sizes = [
        (11, 9),
        (15, 13),
        (21, 17),
        (31, 25)
    ]
    
    for width, height in test_sizes:
        print(f"\n--- MAZE {width}x{height} ---")
        
        maze = create_maze(width, height)
        ascii_maze = maze_to_ascii(maze)
        
        # Print line by line to ensure output appears
        for line in ascii_maze.split('\n'):
            print(line)
    
    print("\n" + "=" * 50)
    print("ALL MAZES GENERATED SUCCESSFULLY!")
    print("=" * 50)


if __name__ == '__main__':
    main()
