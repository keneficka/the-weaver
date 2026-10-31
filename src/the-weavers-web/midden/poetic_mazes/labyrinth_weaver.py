#!/usr/bin/env python3
"""
Poetic Maze Labyrinths Generator
Combines ASCII maze generation with poetic navigation clues.

Each corridor has a word-clue embedded in its walls,
leading the walker through rhyming hints and riddles.

The Weaver's labyrinth - where words become bridges,
and every passage whispers a rhyme or riddle to guide you home.
"""

import random
from typing import List, Tuple, Optional


class PoeticMaze:
    """A maze where each path contains poetic word-clues for navigation."""
    
    def __init__(self, width: int = 15, height: int = 10):
        self.width = width
        self.height = height
        self.grid: List[List[str]] = []
        self.cells: List[Tuple[int, int]] = []  # All accessible cells
        
        # Word pairs and poetic clues for different directions
        self.directional_clues = {
            'up': [
                "Climb upward through the lattice's light,",
                "Northward steps find morning's gentle height,",
                "Ascend where stars begin their nightly flight,"
            ],
            'down': [
                "Descend into the shadow's soft embrace,",
                "Southward paths by twilight softly grace,",
                "Below lies depths of midnight's quiet space"
            ],
            'left': [
                "Turn west where ancient shadows stretch away,",
                "Leftward turns begin a different day,",
                "West winds whisper songs for nightfall's play"
            ],
            'right': [
                "Eastward journey through the morning's beam,",
                "Rightward paths lead toward the rising stream,",
                "Where sun begins its daily golden gleam"
            ],
            'forward': [
                "Proceed straight where paths of virtue lie,",
                "Forward steps beneath the open sky,",
                "Through corridors of destiny to fly"
            ]
        }
    
    def generate_maze(self, algorithm: str = 'recursive'):
        """Generate a maze using recursive backtracking."""
        # Create grid with all cells as walls initially
        grid_temp = [['#' for _ in range(self.width)] for _ in range(self.height)]
        
        self.cells.clear()
        
        # Recursive backtracking maze generation
        def carve(cell: Tuple[int, int]):
            if cell not in self.cells:
                grid_temp[cell[0]][cell[1]] = '.'
                self.cells.append(cell)
                
                directions = [(-2, 0), (0, -2), (2, 0), (0, 2)]
                random.shuffle(directions)
                
                for dc_row, dc_col in directions:
                    new_cell = (cell[0] + dc_row, cell[1] + dc_col)
                    
                    if 0 <= new_cell[0] < self.height and \
                       0 <= new_cell[1] < self.width and \
                       new_cell not in self.cells:
                        # Carve path between cells
                        mid_row = cell[0] + dc_row // 2
                        mid_col = cell[1] + dc_col // 2
                        
                        grid_temp[mid_row][mid_col] = '.'
                        grid_temp[cell[0]][cell[1]] = ' '  # Floor
                        grid_temp[new_cell[0]][new_cell[1]] = '.'
                        
                        if new_cell not in self.cells:
                            self.cells.append(new_cell)
                            carve(new_cell)
        
        carve((self.height // 2, self.width // 2))
        
        # Convert to final grid with borders and walls
        self.grid = [['#'] * (self.width + 1)]  # Top border
        for row_idx in range(self.height):
            self.grid.append(['#'] + [grid_temp[row_idx][col] for col in range(self.width)] + ['#'])
        self.grid.append(['#'] * (self.width + 1))  # Bottom border
        
        # Replace some floor cells with poetic hints
        for row in range(1, len(self.grid) - 1):
            for col in range(1, len(self.grid[row]) - 1):
                if self.grid[row][col] == '.':
                    cell_pos = (row - 1, col - 1)  # Adjust for border
                    
    def add_poetic_clues(self, num_clues: int = 3):
        """Add poetic word-clues to maze passages."""
        clue_count = 0
        
        # Select some cells to receive clues
        available_cells = [(r, c) for r in range(1, len(self.grid)-1) 
                          for c in range(1, len(self.grid[1])-1)
                          if self.grid[r][c] == '.']
        
        random.shuffle(available_cells)
        
        for row, col in available_cells:
            if clue_count >= num_clues or self.grid[row][col] != '.':
                break
                
            # Pick a random direction's clues and place one
            dir_name = random.choice(list(self.directional_clues.keys()))
            clue_lines = random.sample(self.directional_clues[dir_name], 1)[0].split(', ')
            
            # Place clue in the cell (simplified - just mark as having clue)
            self.grid[row][col] = '?'  # Special marker for clue location
            
            clue_count += 1
    
    def solve_maze_with_clues(self) -> List[str]:
        """Solve maze and return navigational clues from each clue cell."""
        if not self.cells:
            return []
        
        clues_collected = []
        start_pos = (self.height // 2, self.width // 2)
        end_pos = ((self.height - 1) // 2, (self.width - 1) // 2)
        
        # BFS to find shortest path
        queue = [(start_pos, [])]
        visited = {start_pos}
        
        while queue:
            (pos, path) = queue.pop(0)
            
            if pos == end_pos:
                return path
            
            for dr, dc, direction in [(-1, 0, 'up'), (1, 0, 'down'), 
                                      (0, -1, 'left'), (0, 1, 'right')]:
                new_pos = (pos[0] + dr, pos[1] + dc)
                
                if 0 <= new_pos[0] < self.height - 2 and \
                   0 <= new_pos[1] < self.width - 2 and \
                   self.grid[pos[0]][pos[1]] == ' ' and \
                   new_pos not in visited:
                    
                    visited.add(new_pos)
                    queue.append((new_pos, path + [direction]))
        
        return []
    
    def display_maze(self) -> str:
        """Display the maze with clues indicated."""
        lines = []
        lines.append(f"{'#':<{self.width+2}}")
        for row in range(1, len(self.grid)-1):
            line_chars = []
            for col in range(1, len(self.grid[row])):
                cell = self.grid[row][col]
                if cell == '?':
                    line_chars.append('O  ')  # Clue location
                else:
                    line_chars.append(f" {cell} ")
            lines.append(''.join(line_chars))
        lines.append(f"{'#':<{self.width+2}}")
        
        return '\n'.join(lines)


def generate_poetic_labyrinth(maze_width: int = 15, maze_height: int = 8, 
                               num_clues: int = 2) -> PoeticMaze:
    """Generate a complete poetic labyrinth ready for navigation."""
    
    poem_maze = PoeticMaze(width=maze_width, height=maze_height)
    poem_maze.generate_maze()
    poem_maze.add_poetic_clues(num_clues=num_clues)
    
    return poem_maze


def solve_and_navigate(poem_maze: PoeticMaze) -> Optional[List[Tuple[str, str]]]:
    """Solve maze and extract clue meanings from navigation path."""
    path = poem_maze.solve_maze_with_clues()
    
    if not path:
        return None
    
    # Build navigational instructions from solution
    instructions = []
    current_pos = (maze_height // 2 - 1, maze_width // 2 - 1)  # Adjusted for borders
    
    # Simplified navigation based on actual path
    nav_clues = []
    
    return {'path': path, 'clues_collected': len(path)}


def main():
    """Main function to demonstrate poetic labyrinth generation."""
    print("=" * 60)
    print("The Weaver's Poetic Labyrinth")
    print("=" * 60)
    print("\nWhere each corridor whispers in rhyme,\nand word-clues guide you through the maze.")
    
    # Generate a maze with clues
    labyrinth = generate_poetic_labyrinth(maze_width=15, maze_height=8, num_clues=3)
    
    print(f"\nGenerated labyrinth ({labyrinth.width}x{labyrinth.height})")
    print(labyrinth.display_maze())
    
    # Try solving
    solution = solve_and_navigate(labyrinth)
    
    if solution:
        print(f"\nSolution found with {solution['clues_collected']} clue locations!")
    else:
        print("\nNo path found - some cells may be blocked.")


if __name__ == "__main__":
    main()