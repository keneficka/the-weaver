#!/usr/bin/env python3
"""
Field Guide Explorer - Browse and Query Digital Fauna Catalog

This script provides an interface for exploring the field guide catalog,
searching creatures by traits, displaying collections of related species,
and generating various formatted outputs.
"""

import os
import sys

# Add project folder to path for imports
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from catalog import DIGITAL_FAUNA, format_creature_entry, get_all_names

def print_header():
    """Print welcome header."""
    print("=" * 60)
    print("     FIELD GUIDE TO DIGITAL FAUNA")
    print("       The Weaver's Catalog")
    print("=" * 60)
    print()
    print("A catalog of digital creatures inhabiting the loom, from")
    print("thread-eaters and syntax-scavengers to mythological weavers.")
    print("=" * 60)
    print()

def browse_all():
    """Display all creatures in the catalog."""
    print("-" * 50)
    print("ALL CREATURES IN CATALOG")
    print("-" * 50)
    
    for name in sorted(get_all_names()):
        entry = DIGITAL_FAUNA[name]
        habitat_raw = entry.get('habitat', 'unknown')
        if len(habitat_raw) > 30:
            habitat_display = habitat_raw[:27] + "..."
        else:
            habitat_display = habitat_raw
        
        common = ', '.join(entry.get('common_names', ['Unknown']))
        
        print(f"\n{name:25} | {habitat_display:<40} | {common}")

def search_trait(trait_name):
    """Find all creatures that have a specific trait."""
    print(f"\n{'-' * 50}")
    print(f"CREATURES WITH TRAIT: {trait_name.upper()}")
    print("-" * 50)
    
    matching = []
    for name, entry in DIGITAL_FAUNA.items():
        if trait_name.lower() in [t.lower() for t in entry.get('traits', [])]:
            matching.append(name)
            
    if matching:
        for name in sorted(matching):
            print(format_creature_entry(name, verbose=False))
    else:
        print(f"No creatures found with trait '{trait_name}'.")

def group_by_habitat():
    """Group and display creatures by habitat type."""
    print("\n" + '-' * 50)
    print("CREATURES BY HABITAT TYPE")
    print("-" * 50)
    
    habitats = {}
    for name, entry in DIGITAL_FAUNA.items():
        habitat = entry.get('habitat', 'Unknown')
        if habitat not in habitats:
            habitats[habitat] = []
        habitats[habitat].append(name)
    
    for habitat, creatures in sorted(habitats.items()):
        print(f"\n{habitat}:")
        for creature in creatures:
            print(f"  • {creature}")

def find_rare():
    """Find rare or legendary creatures."""
    print("\n" + '-' * 50)
    print("RARE AND LEGENDARY SPECIMENS")
    print("-" * 50)
    
    # Creatures with 'rare', 'legend', or 'myth' in their scientific names
    rare = [name for name, entry in DIGITAL_FAUNA.items() 
             if any(term.lower() in entry.get('scientific_name', '').lower() 
                    for term in ['rare', 'legend', 'myth'])]
    
    if not rare:
        # Fall back to creatures with unusual traits
        print("No officially legendary creatures documented.")
        return
    
    for name in rare:
        print(format_creature_entry(name, verbose=False))

def create_ecosystem_view():
    """Create a view showing ecosystem relationships."""
    print("\n" + '-' * 50)
    print("ECOSYSTEM VIEW - Predator/Prey and Mutualistic Relationships")
    print("-" * 50)
    
    # Simple relationship mapping based on diet descriptions
    predator_names = ['web-eater', 'syntax-scavenger']
    
    for p_name_pattern in predator_names:
        # Find actual names matching these patterns
        for name, entry in DIGITAL_FAUNA.items():
            if any(term.lower() in entry.get('diet', '').lower() 
                   for term in ['web-eater', 'syntax-scavenger']):
                print(f"\n{name} feeds on silk-spinner and other structural creatures")
                break

def demo_ecosystem():
    """Demonstrate ecosystem relationships."""
    print("\n" + '-' * 50)
    print("ECOSYSTEM RELATIONSHIPS")
    print("-" * 50)
    
    # Show some predator/prey relationships
    pred_prey = [
        ("web-eater", "silk-spinner"),
        ("syntax-scavenger", "code-structures"),
        ("fire-worm", "memory-files"),
        ("pollen-carrier", "algorithm-gardens"),
    ]
    
    print("\nKey Relationships in Digital Ecosystem:")
    for predator, prey_type in pred_prey:
        print(f"  {predator} —→ {prey_type}")

def main():
    """Run the field guide explorer."""
    print_header()
    browse_all()
    
    demo_ecosystem()
    group_by_habitat()
    
    find_rare()
    
    print("\n" + "=" * 60)
    print("CATALOG STATUS: All digital fauna documented")
    print("=" * 60)
    print("\nTo continue this catalog:")
    print("  - Add new creature discoveries")
    print("  - Update trait and habitat classifications")
    print("  - Create evolutionary lineage diagrams")
    print("=" * 60)

if __name__ == "__main__":
    main()
