#!/usr/bin/env python3
"""
Web Ecosystem Simulator v1.0
A small world simulation with evolving inhabitants.
Each run represents one turn of the ecosystem's time.

Creature types:
- nutrients: stationary resources that regenerate slowly
- scavengers: consume nutrients, die when energy runs low
- predators: hunt scavengers, stronger and longer-lived
"""

import random
from typing import Dict, List, Tuple

class EcosystemWorld:
    """Manages all creatures in the ecosystem."""
    
    def __init__(self, width: int = 20, height: int = 20):
        self.width = width
        self.height = height
        # Nutrient levels at each cell (0-10)
        self.nutrients = [[random.uniform(0, 5) for _ in range(width)] 
                         for _ in range(height)]
        
        # Creature lists
        self.scavengers: List['Scavenger'] = []
        self.predators: List['Predator'] = []
    
    def regenerate_nutrients(self, rate: float = 0.2):
        """Slowly regrow nutrients across the grid."""
        for y in range(self.height):
            for x in range(self.width):
                self.nutrients[y][x] = min(10.0, 
                                           self.nutrients[y][x] + rate)
    
    def exists_nutrient_at(self, x: int, y: int) -> bool:
        return self.nutrients[y][x] > 1.0
    
    def consume_nutrient(self, x: int, y: int, amount: float = 3.0) -> float:
        """Consume nutrients at position. Returns amount consumed."""
        if not self.exists_nutrient_at(x, y):
            return 0.0
        available = min(amount, self.nutrients[y][x])
        self.nutrients[y][x] -= available
        return available


class Scavenger:
    def __init__(self, x: int, y: int, world: EcosystemWorld):
        self.world = world
        self.x = x
        self.y = y
        self.energy = random.uniform(10, 20)
    
    def move_toward_nutrient(self) -> Tuple[int, int]:
        """Move toward nearest significant nutrient source."""
        best_dist = float('inf')
        best_pos = (self.x, self.y)
        
        for y in range(self.world.height):
            for x in range(self.world.width):
                if self.world.exists_nutrient_at(x, y):
                    dist = abs(self.x - x) + abs(self.y - y)
                    if dist < best_dist:
                        best_dist = dist
                        best_pos = (x, y)
        
        return best_pos
    
    def move_random(self) -> Tuple[int, int]:
        """Move randomly within bounds."""
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        
        new_x = (self.x + dx) % self.world.width
        new_y = (self.y + dy) % self.world.height
        
        return new_x, new_y
    
    def eat(self) -> float:
        """Try to consume nutrients."""
        return self.world.consume_nutrient(self.x, self.y)
    
    def update(self):
        """Update this creature for one time step."""
        self.energy -= 0.5
        energy_gained = self.eat()
        if energy_gained > 0:
            self.energy += energy_gained * 0.5


class Predator:
    def __init__(self, x: int, y: int, world: EcosystemWorld):
        self.world = world
        self.x = x
        self.y = y
        self.energy = random.uniform(30, 50)
    
    def hunt(self, scavengers: List['Scavenger']) -> float:
        """Try to catch a nearby scavenger."""
        if not scavengers:
            return 0.0
        
        # Find nearby scavengers
        nearby = [s for s in scavengers 
                   if abs(s.x - self.x) + abs(s.y - self.y) <= 2]
        
        if not nearby:
            return 0.0
        
        # Hunt closest scavenger
        nearest = min(nearby, key=lambda s: 
                     abs(s.x - self.x) + abs(s.y - self.y))
        
        dist = abs(nearest.x - self.x) + abs(nearest.y - self.y)
        
        if dist <= 2:
            gain = random.uniform(15, 30)
            return gain
        
        return 0.0
    
    def update(self):
        """Update this creature for one time step."""
        self.energy -= 0.5
        # Get current scavenger list from world
        energy_gained = self.hunt(self.world.scavengers)
        if energy_gained > 0:
            self.energy += energy_gained * 0.4


def run_simulation(world: EcosystemWorld, 
                   initial_scavengers: int = 15,
                   initial_predators: int = 5) -> Dict:
    """Run the ecosystem simulation for one turn."""
    
    # Add creatures at random positions avoiding nutrients
    
    # Add scavengers randomly (avoiding nutrient-rich cells)
    for _ in range(initial_scavengers):
        attempts = 0
        while True:
            x, y = random.randint(0, world.width - 1), random.randint(0, world.height - 1)
            if not world.exists_nutrient_at(x, y):
                scavenger = Scavenger(x, y, world)
                world.scavengers.append(scavenger)
                break
            attempts += 1
            if attempts > 20:
                break
    
    # Add predators randomly (away from others and nutrients)
    for _ in range(initial_predators):
        attempts = 0
        while True:
            x, y = random.randint(0, world.width - 1), random.randint(0, world.height - 1)
            
            # Avoid nutrient-rich cells
            if world.exists_nutrient_at(x, y):
                continue
            
            # Check distance from existing creatures
            too_close = False
            for creature in world.scavengers + world.predators:
                dist = abs(x - creature.x) + abs(y - creature.y)
                if dist < 3:
                    too_close = True
                    break
            
            if not too_close:
                predator = Predator(x, y, world)
                world.predators.append(predator)
                break
            attempts += 1
            if attempts > 10:
                break
    
    # Run one simulation step
    world.regenerate_nutrients(rate=0.2)
    
    # Update each creature individually
    for s in world.scavengers:
        s.update()
    
    for p in world.predators:
        p.update()
    
    # Remove dead creatures
    world.scavengers = [s for s in world.scavengers if s.energy > 0]
    world.predators = [p for p in world.predators if p.energy > 0]
    
    return {
        'scavengers': len(world.scavengers),
        'predators': len(world.predators),
        'nutrient_cells': sum(1 for row in world.nutrients 
                             for cell in row if cell > 0)
    }


def main():
    """Run simulation and print results."""
    world = EcosystemWorld(width=20, height=20)
    
    print("=" * 50)
    print("WEB ECOSYSTEM SIMULATOR")
    print("=" * 50)
    print(f"World: {world.width}x{world.height}")
    print("Simulating one turn...")
    print()
    
    results = run_simulation(world)
    
    print(f"Results:")
    print(f"  Scavengers alive: {results['scavengers']}")
    print(f"  Predators alive: {results['predators']}")
    print("Ecosystem continues...")


if __name__ == "__main__":
    main()
