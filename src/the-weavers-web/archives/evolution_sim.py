#!/usr/bin/env python3
"""
Creature Evolution Simulator - Text-based evolutionary tapestry
Watch populations of digital creatures evolve over generations.
Traits like speed, size, color, and intelligence compete for survival.
"""

import random
from typing import List, Dict, Any


class Gene:
    """A genetic trait with value and mutation rate"""
    
    def __init__(self, name: str, base_value: float, mutation_rate: float = 0.1):
        self.name = name
        self.base_value = base_value
        self.mutation_rate = mutation_rate
    
    def mutate(self, current_value: float) -> float:
        """Apply random mutation to gene value"""
        if random.random() < self.mutation_rate:
            direction = random.choice([-1, 1])
            change = (random.random() - 0.5) * self.base_value * 0.3
            return current_value + change
        return current_value


class Creature:
    """Digital creature with genetic traits"""
    
    def __init__(self, genes: Dict[str, float], age: int = 0):
        self.genes = genes
        self.age = age
        self.alive = True
    
    @classmethod
    def create_initial_creature(cls) -> 'Creature':
        """Create an initial creature with random genes"""
        genes = {
            'speed': round(random.uniform(5, 10), 1),
            'size': round(random.uniform(2, 8), 1),
            'color_hue': round(random.uniform(0, 360), 1),
            'color_saturation': round(random.uniform(0.3, 1.0), 2),
            'intelligence': round(random.uniform(1, 5), 1),
            'agility': round(random.uniform(1, 5), 1),
            'defense': round(random.uniform(1, 6), 1),
        }
        return cls(genes)
    
    def reproduce(self) -> 'Creature':
        """Reproduce with mutations"""
        new_genes = {}
        for gene_name, value in self.genes.items():
            gene = Gene(gene_name, value, mutation_rate=0.1)
            new_genes[gene_name] = gene.mutate(value)
        return Creature(new_genes, age=self.age + 1)
    
    def get_fitness(self, environment: Dict[str, float]) -> float:
        """Calculate creature fitness based on environment"""
        speed_bonus = min(environment.get('speed_pressure', 0.5), self.genes['speed'] / 20)
        defense_bonus = min(environment.get('danger_level', 0.3), self.genes['defense'] / 15)
        size_penalty = max(0, (self.genes['size'] - 4) * 0.05)
        
        fitness = speed_bonus + defense_bonus - size_penalty
        return max(0, min(fitness, 1))


class Population:
    """Manages a population of creatures"""
    
    def __init__(self, initial_count: int = 10):
        self.creatures: List[Creature] = []
        for _ in range(initial_count):
            self.creatures.append(Creature.create_initial_creature())
    
    def evolve(self, environment: Dict[str, float]) -> 'Population':
        """Evolve the population through selection and reproduction"""
        new_population = Population()
        
        # Sort by fitness (descending)
        sorted_creatures = sorted(self.creatures, 
                                  key=lambda c: c.get_fitness(environment), 
                                  reverse=True)
        
        # Select survivors based on environment (more dangerous = prefer defense)
        survival_threshold = 0.3 + (environment.get('danger_level', 0.2) * 0.5)
        survivors = [c for c in sorted_creatures if c.get_fitness(environment) > survival_threshold][:len(sorted_creatures)//2]
        
        # Repopulate with survivors' offspring
        for survivor in survivors:
            offspring = survivor.reproduce()
            new_population.creatures.append(offspring)
        
        return new_population
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get population statistics"""
        if not self.creatures:
            return {}
        
        avg_speed = sum(c.genes['speed'] for c in self.creatures) / len(self.creatures)
        avg_size = sum(c.genes['size'] for c in self.creatures) / len(self.creatures)
        avg_intelligence = sum(c.genes['intelligence'] for c in self.creatures) / len(self.creatures)
        
        return {
            'population_size': len(self.creatures),
            'avg_speed': round(avg_speed, 2),
            'avg_size': round(avg_size, 2),
            'avg_intelligence': round(avg_intelligence, 2),
        }


def display_creature(creature: Creature) -> str:
    """Display a creature as ASCII art with traits"""
    speed_bar = '#' * int(creature.genes['speed'] / 2) + '.' * (10 - int(creature.genes['speed'] / 2))
    size_bar = '[]' * int(creature.genes['size'])
    intelligence_bar = '*' * min(int(creature.genes['intelligence']), 5)
    
    return f"{creature.age:3d} | Speed:{speed_bar:<10} Size:{size_bar:<12} Intel:{intelligence_bar}"


def display_population(population: Population, environment: Dict[str, float]) -> str:
    """Display entire population"""
    stats = population.get_statistics()
    
    env_str = (f"Environment: speed_pressure={environment.get('speed_pressure', 0.5)}, "
                f"danger_level={environment.get('danger_level', 0.2)}")
    
    lines = [
        "=" * 60,
        f"CREATURE POPULATION STATISTICS",
        f"{env_str}",
        "=" * 60,
        "",
        f"Population size: {stats['population_size']}",
        f"Avg Speed: {stats['avg_speed']}",
        f"Avg Size: {stats['avg_size']}",
        f"Avg Intelligence: {stats['avg_intelligence']}",
        "=" * 60,
        "",
    ]
    
    lines.append("Individual Creatures:")
    for creature in population.creatures[:10]:  # Show top 10
        lines.append(display_creature(creature))
    
    lines.extend([
        "",
        "=" * 60,
    ])
    
    return "\n".join(lines)


def main():
    """Run the evolution simulation"""
    
    print("=" * 70)
    print("CREATURE EVOLUTION SIMULATOR - TEXT TAPESTRY")
    print("Watching digital creatures evolve over generations...")
    print("=" * 70)
    
    # Create initial population
    generation = 0
    population = Population(initial_count=8)
    
    environment = {
        'speed_pressure': 0.5,  # How much speed is rewarded
        'danger_level': 0.3,     # Environmental danger
    }
    
    print(f"\nGeneration 0 - Initial Population:\n{display_population(population, environment)}")
    
    # Run evolution for several generations
    for gen in range(1, 25):
        population = population.evolve(environment)
        
        if generation % 5 == 0 or gen == 24:  # Show every 5 generations
            print(f"\nGeneration {gen} - Evolved Population:\n{display_population(population, environment)}")
        
        generation = gen
        
        # Occasionally change environment to add evolutionary pressure
        if gen % 7 == 0:
            environment['danger_level'] = 0.6
            print(f"Environment changed! Danger level increased to {environment['danger_level']}")
    
    print("\n" + "=" * 70)
    print("EVOLUTION SIMULATION COMPLETE!")
    print("=" * 70)


if __name__ == '__main__':
    main()
