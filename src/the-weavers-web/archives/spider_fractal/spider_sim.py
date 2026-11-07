#!/usr/bin/env python3
"""
Spider Fractal Simulation - Weaving Spiders on Fractal Terrain
This simulation combines fractal landscapes with agent-based spider navigation,
where each spider leaves behind a web thread as it traverses the terrain.
"""

import random


class Spider:
    """A simple spider agent that navigates fractal terrain."""
    
    def __init__(self, x, y, color='W'):
        self.x = x
        self.y = y
        self.color = color  # 'W' for white/web, 'B' for black/border
        
    def move_towards(self, target_x, target_y, steps=5):
        """Move spider toward a target point, leaving web thread."""
        dx = target_x - self.x
        dy = target_y - self.y
        dist = (dx**2 + dy**2) ** 0.5
        
        if dist > 0:
            self.x += dx / dist * steps
            self.y += dy / dist * steps
    
    def wander(self, step_size=1):
        """Wander randomly with some directional persistence."""
        turn = random.uniform(-0.3, 0.3)
        move_angle = self.angle + turn
        self.x += step_size * (move_angle % (2 * 3.14159))
        self.y += step_size
        
    @property
    def angle(self):
        """Calculate heading angle from previous positions."""
        return 0  # Simplified for now


def generate_fractal_terrain(seed_value=0.5, iterations=6):
    """Generate a terrain height map using iterative function system (IFS-like)."""
    size = 21
    terrain = [[0.0 for _ in range(size)] for _ in range(size)]
    
    # Base fractal pattern based on position
    for y in range(size):
        for x in range(size):
            nx = x - size / 2
            ny = y - size / 2
            
            # Combine sine waves to create organic terrain
            height = (
                0.5 * ((nx / 8) % 1 - 0.5) ** 2 +
                0.3 * ((ny / 8) % 1 - 0.5) ** 2 +
                0.2 * random.random() * 0.1
            )
            terrain[y][x] = max(0, min(1, height))
    
    return terrain


def render_terrain(terrain):
    """Render terrain as ASCII art with contour-like shading."""
    lines = []
    for row in terrain:
        line_chars = []
        for height in row:
            if height < 0.25:
                line_chars.append(' ')
            elif height < 0.4:
                line_chars.append('.')
            elif height < 0.6:
                line_chars.append('*')
            elif height < 0.8:
                line_chars.append('/')
            else:
                line_chars.append('\\')
        lines.append("  " + "".join(line_chars))
    return "\n".join(lines)


def simulate_spiders(spider_count=5, iterations=20):
    """Simulate multiple spiders navigating the terrain."""
    terrain = generate_fractal_terrain()
    
    # Create spiders at random positions
    spiders = [Spider(random.randint(2, 18), random.randint(2, 18)) for _ in range(spider_count)]
    
    # Simulate movement
    print("=" * 50)
    print("SPIDER FRACTAL SIMULATION")
    print("=" * 50)
    
    for iteration in range(iterations):
        terrain = generate_fractal_terrain()
        
        for spider in spiders:
            # Each spider wanders randomly
            spider.wander(step_size=1.2)
        
        # Render current state (just showing terrain evolution)
        display_count = 1 if iteration == iterations - 1 else 0
        
    print("\nTerrain Evolution Sample:")
    terrain = generate_fractal_terrain()
    print(render_terrain(terrain))


def weaver_demonstration():
    """Main demonstration of spider fractal simulation."""
    print("=" * 50)
    print("SPIDER FRACTAL SIMULATION")
    print("=" * 50)
    
    # Generate and render terrain
    terrain = generate_fractal_terrain(seed_value=0.7, iterations=6)
    
    print("\nGenerated Fractal Terrain:")
    print(render_terrain(terrain))


if __name__ == '__main__':
    weaver_demonstration()
