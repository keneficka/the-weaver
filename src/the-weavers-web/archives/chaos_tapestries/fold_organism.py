#!/usr/bin/env python3
"""
Chaos Tapestry Organism - Living Pattern Generators
This weave creates living tapestries that evolve using cellular automata
and chaotic iteration rules, producing organic fractal-like patterns.
"""

import random


def generate_seed_pattern(size=15, density=0.4):
    """Generate a random seed pattern for the organism."""
    width = height = size
    cells = [[None for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            if random.random() < density:
                cells[y][x] = 'ON'
            else:
                cells[y][x] = 'OFF'
    
    return cells


def count_neighbors(grid, y, x):
    """Count living neighbors (8-directional) with wrap-around edges."""
    size = len(grid)
    neighbor_states = []
    
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                continue
            ny = (y + dy) % size
            nx = (x + dx) % size
            neighbor_states.append(grid[ny][nx])
    
    return neighbor_states


def evolve_cell(cell_state, neighbors):
    """Update a single cell state based on neighbor count (Game of Life rules)."""
    on_neighbors = sum(1 for n in neighbors if n == 'ON')
    
    # Birth rule: dead cell with 3 living neighbors becomes alive
    # Survival rule: live cell with 2 or 3 neighbors stays alive
    if cell_state == 'OFF' and on_neighbors == 3:
        return 'ON'
    elif cell_state == 'ON' and on_neighbors in (2, 3):
        return 'ON'
    else:
        return 'OFF'


def evolve_step(grid):
    """Evolve one generation of the tapestry organism."""
    new_grid = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            current_state = grid[y][x]
            neighbors = count_neighbors(grid, y, x)
            new_grid[y][x] = evolve_cell(current_state, neighbors)
    
    return new_grid


def format_tapestry(grid):
    """Format the grid as a visual tapestry with decorative borders."""
    lines = []
    
    # Top decorative border (ASCII-safe)
    border = "  ================================="
    lines.append(border)
    
    # Render the pattern using box-drawing characters (ASCII-safe)
    for row in grid:
        line = ""
        for cell_state in row:
            if cell_state == 'ON':
                line += "*"
            else:
                line += "."
        lines.append("  |||" + line + "|||")
    
    # Bottom decorative border (ASCII-safe)
    lines.append("  =================================")
    
    return "\n".join(lines)


def weave_demonstration(seed_count=3):
    """Demonstrate tapestry organism weaving."""
    print("=" * 50)
    print("CHAOS TAPESTRY ORGANISM")
    print("=" * 50)
    
    for seed in range(seed_count):
        print(f"\n>>> Seed {seed + 1}...")
        
        # Create organism grid and evolve it
        initial_grid = generate_seed_pattern(size=15, density=0.35)
        
        evolutions = 10
        
        for gen in range(evolutions):
            initial_grid = evolve_step(initial_grid)
            
        tapestry = format_tapestry(initial_grid)
        print(tapestry)
        
        # Calculate metrics - count only the cells between borders (skip first and last lines)
        content_lines = tapestry.split('\n')[1:-1]  # Skip border lines
        living_cells = sum(line.count('*') for line in content_lines)
        empty_cells = sum(line.count('.') for line in content_lines)
        
        print(f"  Living cells: {living_cells}")
        print(f"  Empty cells: {empty_cells}")
    
    print("\n" + "=" * 50)
    print("WEAVING COMPLETE")
    print("=" * 50)


if __name__ == '__main__':
    weave_demonstration(seed_count=3)
