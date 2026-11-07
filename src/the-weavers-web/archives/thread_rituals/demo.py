#!/usr/bin/env python3
"""
Demo runner for Thread Rituals - runs automatically without user input.
Shows the simulation in action and generates outputs.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import WeaveEngine, load_state


def run_demo():
    """Run a demo cycle of thread rituals."""
    print("╔════════════════════════════════════════╗")
    print("║     Thread Rituals - Demo Simulation   ║")
    print("╚════════════════════════════════════════╝")
    print()
    
    engine = WeaveEngine(canvas_width=640, canvas_height=320)
    
    # Add a variety of threads to start
    setup_threads = [
        ("gold", 100, "horizontal"),
        ("indigo", 180, "vertical"),
        ("silver", 250, "horizontal"),
        ("crimson", 320, "vertical"),
        ("ebony", 400, "horizontal"),
        ("gold", 30, "vertical"),
        ("indigo", 600, "horizontal"),
    ]
    
    for color, x, direction in setup_threads:
        engine.add_thread(x, 160, color)
    
    print(f"Initial threads: {len(engine.threads)}")
    print()
    
    # Run multiple cycles to show evolution
    for cycle_num in range(1, 25):
        engine.advance_cycle()
        
        if cycle_num % 4 == 0:
            thread_count = len([t for t in engine.threads if not getattr(t, "broken", False)])
            print(f"Cycle {cycle_num}: {thread_count} threads active, {len(engine.patterns_found)} patterns")
    
    print()
    print("-" * 50)
    print("Simulation complete!")
    print(f"Total cycles: {engine.cycles_completed}")
    print(f"Final thread count: {len([t for t in engine.threads if not getattr(t, 'broken', False)])}")
    print()
    
    # Render final state
    img = engine.render()
    img.save("weave_render_demo.png")
    print("Render saved to weave_render_demo.png")
    
    # Save artifacts
    artifacts_dir = "artifacts"
    os.makedirs(artifacts_dir, exist_ok=True)
    
    with open(os.path.join(artifacts_dir, "ritual_log.txt"), "w") as f:
        for entry in engine.ritual_log:
            f.write(entry + "\n")
    
    print(f"Ritual log saved to {artifacts_dir}/ritual_log.txt")
    
    # Save weave state for next run if desired
    state_path = os.path.join(artifacts_dir, "weave_state.json")
    engine.state["threads"] = [
        {k: v for k, v in t.__dict__.items() 
         if k != "history" and not k.startswith("__")}
        for t in engine.threads
    ]
    with open(state_path, "w") as f:
        import json
        json.dump(engine.state, f, indent=2)
    
    print(f"State saved to {artifacts_dir}/weave_state.json")


if __name__ == "__main__":
    run_demo()
