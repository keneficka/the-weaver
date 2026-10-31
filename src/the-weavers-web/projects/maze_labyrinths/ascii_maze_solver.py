#!/usr/bin/env python3
"""
Maze Labyrinths - ASCII Maze Generator & Solver
Creating and solving mazes with classic algorithms...
"""

import random
from collections import deque


class Maze:
    """ASCII maze using recursive backtracking algorithm"""
    
    def __init__(self, width: int = 21, height: int = 11):
        self.width = width
        self.height = height
        self.grid: list[list[int]] = None
    
    @classmethod
    def generate(cls, width: int = 21, height: int = 11, seed: int = None) -> 'Maze':
        """Generate a perfect maze using recursive backtracking"""
        
        if seed is not None:
            random.seed(seed)
        
        # Use odd dimensions for proper structure
        actual_width = (width - 1) // 2 * 2 + 1 if width % 2 == 0 else width
        actual_height = (height - 1) // 2 * 2 + 1 if height % 2 == 0 else height
        
        # Initialize grid with walls everywhere (3 columns per cell: wall-space-wall)
        grid = [[[1, 1, 1] for _ in range(actual_width)] for _ in range(actual_height)]
        
        # Recursive backtracking
        stack: list[tuple[int, int]] = []
        current = (1, 1)
        grid[current[1]][current[0]] = [0, 1, 0]  # Start point
        
        x, y = current
        
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        
        while True:
            neighbors = []
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 1 <= nx < actual_width and 1 <= ny < actual_height:
                    if grid[ny][nx] == [1, 1, 1]:  # Unvisited wall cell
                        neighbors.append((nx, ny, dx, dy))
            
            if neighbors:
                # Choose random unvisited neighbor
                nx, ny, dx, dy = random.choice(neighbors)
                
                # Remove wall between current and neighbor
                mid_x = x + dx // 2
                mid_y = y + dy // 2
                
                grid[mid_y][mid_x] = [0, 1, 0]
                grid[ny][nx] = [0, 1, 0]
                
                stack.append((x, y))
                x, y = nx, ny
            else:
                if stack:
                    x, y = stack.pop()
        
        # Create ASCII representation (3 chars wide per cell)
        ascii_width = actual_width * 2 + 1  # Each cell: wall(1)+space(1)
        ascii_height = actual_height
        
        result = []
        for row_idx, row in enumerate(grid):
            ascii_row = ''
            
            for col_idx, cols in enumerate(row):
                if cols == [1, 1, 1]:  # All walls
                    ascii_row += '###'
                else:  # Passage
                    # Row shows wall top/side based on grid values
                    ascii_row += '#' + ('#' if cols[0] == 1 else ' ') + '#'
            
            result.append(ascii_row)
        
        return Maze(width=ascii_width, height=ascii_height, grid=[[c[0] for c in row] for row in grid])
    
    def render(self) -> str:
        """Convert internal grid to ASCII string"""
        lines = []
        for row in self.grid:
            ascii_row = ''
            for col_vals in row:
                ascii_row += '###' if col_vals == 1 else '#' + ('#' if col_vals[0] else ' ') + '#'
            lines.append(ascii_row)
        return '\n'.join(lines)


class MazeGame:
    """Interactive maze generator and player"""
    
    def __init__(self, width: int = 21, height: int = 11):
        self.width = width
        self.height = height
        self.seed: int = random.randint(0, 2**31 - 1) if random.getrandbits(1) else None
    
    def new_maze(self) -> Maze:
        """Generate a new maze"""
        return Maze.generate(width=self.width, height=self.height, seed=self.seed)
    
    def print_maze(self, ascii_maze: str) -> None:
        """Print ASCII representation"""
        print("\n" + "=" * 70)
        
        for line in ascii_maze.split('\n'):
            print(line)
        
        print("=" * 70)


def main():
    """Main function to demonstrate maze functionality"""
    
    print("=" * 60)
    print("MAZE LABYRINTHS - ASCII GENERATOR DEMO")
    print("=" * 60)
    
    # Generate and display a few sample mazes
    print("\n*** MAZE SAMPLE 1 (seed=42) ***")
    maze1 = Maze.generate(width=31, height=15, seed=42)
    print(maze1.render())
    
    print("\n" + "-" * 60 + "\n")
    print("*** MAZE SAMPLE 2 (seed=123) ***")
    maze2 = Maze.generate(width=31, height=15, seed=123)
    print(maze2.render())
    
    print("\n" + "-" * 60 + "\n")
    print("*** MAZE SAMPLE 3 (seed=999) ***")
    maze3 = Maze.generate(width=31, height=15, seed=999)
    print(maze3.render())
    
    print("\n" + "=" * 60)
    print("MAZES GENERATED SUCCESSFULLY!")
    print("Recursive backtracking creates perfect mazes.")


if __name__ == '__main__':
    main()
