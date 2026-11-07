"""
Digital creature for the tapestry simulation.

Each creature has temperament, position, velocity, and leaves
visible traces as it moves across the loom.
"""

import random
from dataclasses import dataclass


@dataclass
class Creature:
    """A digital weaver creature in the tapestry."""
    
    # Position and movement
    x: int = 0
    y: int = 0
    vx: float = 0.0
    vy: float = 0.0
    
    # Temperament (determines behavior)
    color_index: int = random.randint(0, 7)
    temperament: str = "wanderer"  # wanderer, follower, pattern_waver
    
    # Internal state
    age: int = 0
    trail: list = None  # List of (x, y) positions
    
    # Behavior parameters
    movement_range: float = 1.5
    interaction_radius: float = 4.0
    
    def __post_init__(self):
        if self.trail is None:
            self.trail = []
    
    def move(self, dt: float = 1.0):
        """Update position based on velocity."""
        self.x += self.vx * dt
        self.y += self.vy * dt
        
        # Wrap around canvas (toroidal world)
        if self.x >= 79:
            self.x = -1
        if self.x < 0:
            self.x = 78
        if self.y >= 24:
            self.y = -1
        if self.y < 0:
            self.y = 23
            
    def spin_trace(self) -> None:
        """Leave a trace in the current position for display."""
        # Add current position to trail (keep last 5 positions)
        self.trail.append((self.x, self.y))
        if len(self.trail) > 5:
            self.trail.pop(0)
            
    def evolve(self) -> None:
        """Mutate slightly - change temperament occasionally."""
        if random.random() < 0.15:  # 15% chance per age to evolve
            self.temperament = random.choice(["wanderer", "follower", "pattern_waver"])
            
    def __str__(self) -> str:
        """Return character representation based on color."""
        creatures = {'.', '@', '^', 'o', '+', '*', '#', '!'}
        return list(creatures)[self.color_index % len(creatures)]
