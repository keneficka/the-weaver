#!/usr/bin/env python3
"""
Next cycle runner - loads state from artifacts and continues simulation.
Used to extend the weave across multiple runs.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import WeaveEngine


def continue_cycle(seed: int = None):
    """Load existing state and run additional cycles."""
    if seed is not None:
        print(f"Using random seed: {seed} for next cycle run")
    
    # Create engine which will load existing state automatically
    engine = WeaveEngine(canvas_width=640, canvas_height=320)
    
    print("-" * 50)
    print("LOADING EXISTING WEAVE STATE...")
    print(f"Cycles already completed: {engine.cycles_completed}")
    print(f"Threads currently active: {len(engine.threads)}")
    print()
    
    # Run additional cycles - how many? Let's do a batch of 50
    additional_cycles = 50
    
    for i in range(1, additional_cycles + 1):
        engine.advance_cycle()
        
        if i % 20 == 0:
            thread_count = len([t for t in engine.threads if not getattr(t, "broken", False)])
            patterns = engine.patterns_found[:3] if len(engine.patterns_found) >= 3 else engine.patterns_found
            print(f"Cycle {engine.cycles_completed}: {thread_count} threads active")
    
    print()
    print("-" * 50)
    print(f"Simulation complete! Total cycles: {engine.cycles_completed}")
    print(f"Final thread count: {len([t for t in engine.threads if not getattr(t, 'broken', False)])}")
    print(f"Patterns identified throughout: {len(engine.patterns_found)}")
    print()
    
    # Save final render
    img = engine.render()
    img.save("weave_render_final.png")
    print("Final render saved to weave_render_final.png")
    
    # Save ritual log for this batch
    with open("artifacts/ritual_log.txt", "w") as f:
        for entry in engine.ritual_log:
            f.write(entry + "\n")
    print("Ritual log saved to artifacts/ritual_log.txt")
    
    # Save state for next run
    engine.close()
    print("State saved - ready for next cycle!")


def fresh_start(seed: int = None):
    """Start a completely new weave from scratch."""
    if seed is not None:
        print(f"Using random seed: {seed} for fresh start")
    
    import random
    random.seed(seed)
    
    engine = WeaveEngine(canvas_width=640, canvas_height=320)
    
    # Add variety of threads including vertical ones to enable more ritual types
    setup_threads = [
        ("gold", 100, "horizontal"),
        ("indigo", 180, "vertical"),
        ("silver", 250, "horizontal"),
        ("crimson", 320, "vertical"),
        ("ebony", 400, "horizontal"),
        ("gold", 30, "vertical"),
        ("indigo", 600, "horizontal"),
        ("silver", 80, "vertical"),
    ]
    
    for color, x, direction in setup_threads:
        engine.add_thread(x, 160, color)
    
    print(f"Starting fresh weave with {len(engine.threads)} threads")
    print()
    
    # Run simulation
    continue_cycle(seed)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command in ["--fresh", "fresh"]:
            seed = int(sys.argv[2]) if len(sys.argv) > 2 else None
            fresh_start(seed)
        elif command == "--continue" or command in [""] or len(sys.argv) <= 1:
            # Default to continuing from last state
            seed = int(sys.argv[2]) if len(sys.argv) > 2 else None
            continue_cycle(seed)
        else:
            print(f"Unknown command: {command}")
            print("Usage: python next_cycle.py --fresh [seed]")
            print("       python next_cycle.py --continue [seed]")
            print("       python next_cycle.py")
    else:
        # Default behavior - continue from saved state
        seed = int(sys.argv[1]) if len(sys.argv) > 1 else None
        continue_cycle(seed)
