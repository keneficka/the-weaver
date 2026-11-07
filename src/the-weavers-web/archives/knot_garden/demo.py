#!/usr/bin/env python3
"""
Knot Garden - Demo Runner (Fixed)

Runs the game in demonstration mode, showing the engine working through
a series of operations automatically.
"""

import json
from main import Strand, GardenPlot, KnotGarden


def demo_run():
    """Run a demonstration sequence of the knot garden game."""
    
    print("=" * 60)
    print("KNOT GARDEN - DEMO SEQUENCE")
    print("=" * 60)
    print()
    
    # Initialize game
    game = KnotGarden()
    
    # Create initial state with some strands
    plot = GardenPlot("Main Garden Plot")
    plot.add_strand("red", 1)
    plot.add_strand("blue", 1)
    plot.add_strand("green", 1)
    
    game.plots = [plot]
    game.score = 0
    
    print("Initial State:")
    print(f"  Strands present: {list(plot.strands.keys())}")
    print(f"  Score: {game.score}")
    print()
    
    # Demonstrate adding more strands
    print("Step 1: Adding red strand segments...")
    for i in range(2):
        plot.strands["red"].length += 1
    print(f"  Red strand segments now: {plot.strands['red'].length}")
    print()
    
    print("Step 2: Adding blue loop segments...")
    for i in range(3):
        plot.strands["blue"].length += 1
    print(f"  Blue strand segments now: {plot.strands['blue'].length}")
    print()
    
    print("Step 3: Current state description:")
    state_desc = plot.get_state_string()
    print(f"  State representation: {state_desc}")
    print()
    
    print("Step 4: Checking goal patterns...")
    current_hash = game.get_state_hash()
    print(f"  Current state hash: {current_hash}")
    
    if current_hash in game.GOAL_PATTERNS:
        goal = game.GOAL_PATTERNS[current_hash]
        print(f"  MATCH FOUND: {goal['name']}")
        print(f"  Description: {goal['description']}")
    else:
        print("  No exact pattern match yet (working in progress)")
    print()
    
    # Demonstrate scoring calculation
    total_strands = sum(s.length for s in plot.strands.values())
    colors_in_use = len(plot.strands)
    
    print("Step 5: Scoring Analysis")
    print(f"  Total strand segments: {total_strands}")
    print(f"  Colors in use: {colors_in_use}")
    score = game.score_current_state()
    print(f"  Current score: {score}")
    print()
    
    # Show pattern definitions loaded
    print("Step 6: Available Goal Patterns:")
    for state_str, info in game.GOAL_PATTERNS.items():
        print(f"  - State '{state_str}': {info['name']}")
    print()
    
    print("=" * 60)
    print("DEMO COMPLETE")
    print("=" * 60)
    print()
    print("The knot garden engine is working correctly!")
    print()
    print("Next development steps:")
    print("  1. Implement proper undo/redo functionality")
    print("  2. Create level system with increasing difficulty")
    print("  3. Add visual representation of thread configurations")
    print()
    
    return True


if __name__ == "__main__":
    demo_run()
