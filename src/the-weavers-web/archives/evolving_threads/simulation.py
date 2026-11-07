"""
Main simulation loop for evolving threads.

Manages creatures, canvas rendering, and state persistence.
"""

import random
import pickle
from creature import Creature


# Canvas configuration
CANVAS_WIDTH = 80
CANVAS_HEIGHT = 25
STATE_FILE = "state.pkl"

# Thread colors (ASCII art palette for trails)
TRAIL_COLORS = ['.', 'o', '+', '*', '-', '~', '/', '\\']


def load_state() -> list:
    """Load creature population and canvas state from file."""
    try:
        with open(STATE_FILE, 'rb') as f:
            data = pickle.load(f)
            creatures = [Creature(**c) for c in data['creatures']]
            return creatures
    except FileNotFoundError:
        print("New tapestry loom - no previous state found.")
        return []


def save_state(creatures) -> None:
    """Save current simulation state to file."""
    # Convert creatures to dict format for pickling
    data = {'creatures': [c.__dict__ for c in creatures]}
    with open(STATE_FILE, 'wb') as f:
        pickle.dump(data, f)


def render_canvas(creatures) -> str:
    """Render the tapestry to string output with creatures and trails."""
    # Initialize canvas with empty space
    canvas = [['.' for _ in range(CANVAS_WIDTH)] for _ in range(CANVAS_HEIGHT)]
    
    # First, draw all trails behind creatures
    for creature in creatures:
        if creature.trail:
            # Draw trail backwards so oldest traces are at bottom (depth effect)
            for i, (tx, ty) in enumerate(creature.trail):
                char_idx = len(creature.trail) - 1 - i  # Newest on top
                color_char = TRAIL_COLORS[char_idx % len(TRAIL_COLORS)]
                # Round trail coordinates to integers
                tx_int = round(tx)
                ty_int = round(ty)
                if 0 <= ty_int < CANVAS_HEIGHT and 0 <= tx_int < CANVAS_WIDTH:
                    canvas[ty_int][tx_int] = color_char
    
    # Then draw creatures themselves (they overwrite their trail)
    for creature in creatures:
        cx, cy = round(creature.x), round(creature.y)
        if 0 <= cy < CANVAS_HEIGHT and 0 <= cx < CANVAS_WIDTH:
            canvas[cy][cx] = str(creature)
    
    return "\n".join(["".join(row) for row in canvas])


def main():
    """Main simulation entry point."""
    print("=== Evolving Threads Tapestry ===")
    print("Running creatures across the digital loom...\n")
    
    # Load or create initial state
    creatures = load_state()
    
    if not creatures:
        # Spawn initial population
        num_creatures = 15
        for i in range(num_creatures):
            creatures.append(Creature(
                x=random.randint(0, CANVAS_WIDTH-1),
                y=random.randint(0, CANVAS_HEIGHT-1),
                vx=random.uniform(-0.8, 0.8),
                vy=random.uniform(-0.8, 0.8)
            ))
        print(f"Spawning {num_creatures} initial weavers...\n")
    
    # Save initial state after spawning
    save_state(creatures)
    
    # Run simulation loop
    try_count = 0
    while True:
        try_count += 1
        print(f"--- Tick {try_count} ---")
        
        # Age and evolve creatures occasionally
        for creature in creatures:
            creature.age += 1
            creature.evolve()
            
        # Update positions
        for creature in creatures:
            creature.move(dt=0.5)
            
        # Round positions to keep them as integers for canvas indexing
        for creature in creatures:
            creature.x = round(creature.x)
            creature.y = round(creature.y)
            
        # Let creatures leave traces as they move
        for creature in creatures:
            creature.spin_trace()
            
        # Render and display every tick
        print(render_canvas(creatures))
            
        # Save state periodically to avoid large files
        if try_count % 15 == 0:
            save_state(creatures)
            print(f"State saved (tick {try_count})")
            
        # Check for long run - exit gracefully after reasonable duration
        if try_count > 250:
            print("\nTapestry simulation complete.")
            break
    
    save_state(creatures)
    print(f"\nFinal tapestry preserved with {len(creatures)} weavers.")


if __name__ == "__main__":
    main()
