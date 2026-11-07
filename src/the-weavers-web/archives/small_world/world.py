#!/usr/bin/env python3
"""Small World Simulator - main entry point for the world engine."""

import json
import os
import random
from state_manager import load_state, save_state, update_cycle, get_initial_state

def init_world(world_path="projects/small_world"):
    """Initialize a fresh world or return existing one."""
    state_path = os.path.join(world_path, "world_state.json")
    if not os.path.exists(state_path):
        state = get_initial_state()
        save_state(world_path, state)
    else:
        state = load_state(world_path)
    return state

def run_cycle(state=None):
    """Run one cycle of the world simulation."""
    if state is None:
        state = load_state()
    
    # Deplete resources slowly from each room
    for room in state["rooms"]:
        resource_drain = random.uniform(1.5, 3.0)
        room["resources"] -= resource_drain
        
        # Some rooms have natural regrowth
        if "regrowth_rate" in room:
            regrowth = min(room["max_resources"], room["resources"] + (room["regrowth_rate"] * random.random()))
            room["resources"] = regrowth
    
    # Process inhabitants - age them and handle events
    for inhabitant in state["inhabitants"]:
        if not inhabitant.get("alive", True):
            continue
            
        # Age the inhabitant
        inhabitant["age"] += 1
        
        # Species-specific aging effects
        species = inhabitant.get("species", "knot-kin")
        if species == "knot-kin":
            # Knot-kin contribute silk, decay slowly
            contribution_cost = max(0, inhabitant["resources_contribution"] - random.uniform(0.5, 1.5))
            inhabitant["resources_contribution"] = contribution_cost
        elif species == "weaver-folk":
            # Weaver-folk are more resource-intensive but productive
            inhabitant["resources_contribution"] = max(0, inhabitant["resources_contribution"] - random.uniform(1, 2))
        elif species == "shadow-walker":
            # Shadow-walkers consume resources from environment
            room = next((r for r in state["rooms"] if r["id"] == inhabitant["room_id"]), None)
            if room:
                resource_drain_shadow = random.uniform(0.5, 1.5)
                room["resources"] -= resource_drain_shadow
        
        # Death chance increases with age (modulated by species)
        base_death_chance = 0.05
        if species == "shadow-walker":
            base_death_chance = 0.08  # Shadow-walkers are ephemeral
        elif species == "weaver-folk":
            base_death_chance = 0.04  # Weaver-folk are sturdy
        
        death_roll = random.random()
        if inhabitant["age"] > 15 and death_roll < base_death_chance:
            inhabitant["alive"] = False
    
    # Birth events - new inhabitants appear in resource-rich rooms
    birth_rate = 0.08
    for room in state["rooms"]:
        if room["resources"] >= 25 and random.random() < birth_rate:
            species_pools = ["knot-kin", "weaver-folk", "shadow-walker"]
            chosen_species = random.choice(species_pools)
            
            # Spawn new inhabitant
            new_inhabitant = {
                "id": len([i for i in state["inhabitants"] if i["alive"]]) + 1,
                "species": chosen_species,
                "room_id": room["id"],
                "age": 1,
                "resources_contribution": 5.0,
                "alive": True
            }
            state["inhabitants"].append(new_inhabitant)
            
            # Cost of creation
            room["resources"] -= 8
    
    state["cycle_count"] += 1
    save_state(state=state)
    
    return state

def get_world_report(state=None):
    """Generate a text report of the current world state."""
    if state is None:
        state = load_state()
    
    lines = []
    lines.append(f"=== Small World Report (Generation {state['generation']}, Cycle {state['cycle_count']}) ===")
    lines.append("")
    
    lines.append("Rooms:")
    for room in state["rooms"]:
        active_inhabitants = [i for i in state["inhabitants"] 
                             if i.get("alive", True) and i.get("room_id") == room["id"]]
        species_list = []
        for inv in active_inhabitants:
            s = inv["species"].replace("-", " ")
            species_list.append(s)
        
        lines.append(f"  - {room['name']}: resources={room['resources']:.1f}, "
                     f"inhabitants={[' '.join(species_list) if species_list else 'empty']}")
    
    lines.append("")
    lines.append("Bridges:")
    for bridge in state["bridges"]:
        from_name = next((r["name"] for r in state["rooms"] if r["id"] == bridge.get("from")), "unknown")
        to_name = next((r["name"] for r in state["rooms"] if r["id"] == bridge.get("to")), "unknown")
        lines.append(f"  - {from_name} <-> {to_name}")
    
    lines.append("")
    lines.append("Inhabitants:")
    alive_count = sum(1 for i in state["inhabitants"] if i.get("alive", True))
    dead_count = len(state["inhabitants"]) - alive_count
    species_counts = {}
    for inv in state["inhabitants"]:
        s = inv["species"].replace("-", " ")
        species_counts[s] = species_counts.get(s, 0) + (1 if inv.get("alive", True) else 0)
    
    lines.append(f"  Total: {len(state['inhabitants'])} (alive: {alive_count}, deceased: {dead_count})")
    for s in sorted(species_counts.keys()):
        lines.append(f"  - {s}: {species_counts[s]}")
    
    return "\n".join(lines)

if __name__ == "__main__":
    # Initialize world
    print("Initializing Small World...")
    state = init_world()
    print(get_world_report(state))
    
    # Run a few cycles for demo
    print("\n--- Running 3 Demo Cycles ---\n")
    for i in range(1, 4):
        print(f"Cycle {i}:")
        state = run_cycle(state)
        print(get_world_report(state))
