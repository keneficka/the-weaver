#!/usr/bin/env python3
"""
Ecosystem Tapestry - A cellular automaton ecosystem simulation
Organisms interact on a grid, weaving life patterns across the weave.
"""

import random


class Organism:
    """A basic organism living in the tapestry."""
    
    def __init__(self, x, y, type_id):
        self.x = int(x)
        self.y = int(y)
        self.type_id = type_id
    
    def move(self, grid_size=20, noise=0.1):
        """Move randomly with slight bias toward open space."""
        dx = random.uniform(-1, 1) * noise
        dy = random.uniform(-1, 1) * noise
        self.x += dx
        self.y += dy
    
    def age(self):
        """Age the organism; return True if dead."""
        return random.random() < 0.02


class Plant(Organism):
    """Stationary plant/algae that produces oxygen and food."""
    
    def __init__(self, x, y):
        super().__init__(x, y, 'plant')
    
    def age(self):
        return False  # Plants don't die


class Herbivore(Organism):
    """Grazer that eats plants."""
    
    def __init__(self, x, y):
        super().__init__(x, y, 'herbivore')
        self.alive = True
    
    def age(self):
        return self.alive and random.random() < 0.03


class Predator(Organism):
    """Hunter that eats herbivores."""
    
    def __init__(self, x, y):
        super().__init__(x, y, 'predator')
        self.alive = True
    
    def age(self):
        return self.alive and random.random() < 0.01


class Ecosystem:
    """The entire ecosystem grid world."""
    
    def __init__(self, size=20, plant_rate=0.5, herbivore_count=3, predator_count=1):
        self.grid_size = size
        self.world = [[None for _ in range(size)] for _ in range(size)]
        
        # Place initial organisms
        for _ in range(int(plant_rate * size * size)):
            x, y = random.randint(0, size-1), random.randint(0, size-1)
            if self.world[y][x] is None:
                self.world[y][x] = Plant(x, y)
        
        for _ in range(herbivore_count):
            x, y = random.randint(0, size-1), random.randint(0, size-1)
            if self.world[y][x] is None:
                self.world[y][x] = Herbivore(x, y)
        
        for _ in range(predator_count):
            x, y = random.randint(0, size-1), random.randint(0, size-1)
            if self.world[y][x] is None:
                self.world[y][x] = Predator(x, y)
    
    def render(self):
        """Render the ecosystem as ASCII art."""
        lines = []
        for y in range(self.grid_size):
            line_chars = [' '] * self.grid_size
            for x in range(self.grid_size):
                org = self.world[y][x]
                if org is not None:
                    char = 'o' if isinstance(org, Plant) else 'H' if isinstance(org, Herbivore) else 'P'
                    line_chars[x] = char
            lines.append("  " + "".join(line_chars))
        return "\n".join(lines)
    
    def step(self):
        """Advance one simulation step."""
        new_world = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        
        # Move all organisms and place them at rounded positions
        for y in range(self.grid_size):
            for x in range(self.grid_size):
                org = self.world[y][x]
                if org and (isinstance(org, Herbivore) or isinstance(org, Predator)):
                    org.move(self.grid_size)
                    new_y = int(round(org.y))
                    new_x = int(round(org.x))
                    # Wrap coordinates
                    if new_y < 0:
                        new_y += self.grid_size
                    elif new_y >= self.grid_size:
                        new_y -= self.grid_size
                    if new_x < 0:
                        new_x += self.grid_size
                    elif new_x >= self.grid_size:
                        new_x -= self.grid_size
                    new_world[new_y][new_x] = org
        
        # Place new plants randomly
        for _ in range(int(0.3 * self.grid_size * self.grid_size)):
            x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            if new_world[y][x] is None:
                new_world[y][x] = Plant(x, y)
        
        # Check for death and rebuild grid
        self.world = new_world


def run_ecosystem_demo():
    """Main demonstration of the ecosystem simulation."""
    print("=" * 50)
    print("ECOSYSTEM TAPESTRY SIMULATION")
    print("Legend: [ ] space  {o} plant  {H} herbivore  {P} predator")
    print("=" * 50)
    
    eco = Ecosystem(size=20, plant_rate=0.4, herbivore_count=4, predator_count=1)
    
    for generation in range(10):
        print(f"\nGeneration {generation + 1}:")
        print(eco.render())
        eco.step()


if __name__ == '__main__':
    run_ecosystem_demo()
