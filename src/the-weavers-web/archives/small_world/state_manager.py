#!/usr/bin/env python3
"""Small World State Manager - persists world state between cycles."""

import json
import os

# Determine base path relative to script location
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = "world_state.json"

def _get_state_path():
    """Get the absolute or relative path to state file based on current working directory."""
    # If we're running from the small_world folder, use relative path
    if os.getcwd() == _SCRIPT_DIR:
        return STATE_FILE
    # Otherwise try joining with base script dir
    else:
        return os.path.join(_SCRIPT_DIR, STATE_FILE)

def load_state(world_path=None):
    """Load the current world state from disk."""
    state_path = _get_state_path()
    if not os.path.exists(state_path):
        return get_initial_state()
    with open(state_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_state(world_path=None, state=None):
    """Save the world state to disk."""
    state = state or get_initial_state()
    state_path = _get_state_path()
    with open(state_path, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2)

def get_initial_state():
    """Return initial world state with empty rooms and no inhabitants."""
    return {
        "rooms": [
            {"id": 1, "name": "Central Chamber", "x": 0, "y": 0, "width": 4, "height": 4, "resources": 50},
            {"id": 2, "name": "Silk Weaver's Room", "x": 5, "y": 0, "width": 3, "height": 3, "resources": 30},
            {"id": 3, "name": "Shadow Alcove", "x": 9, "y": 0, "width": 3, "height": 2, "resources": 15},
            {"id": 4, "name": "Light Catcher", "x": 0, "y": 5, "width": 4, "height": 3, "resources": 40},
        ],
        "bridges": [],
        "inhabitants": [],
        "generation": 1,
        "cycle_count": 0
    }

def get_initial_inhabitant():
    """Return a sample inhabitant template."""
    return {
        "id": None,
        "species": "knot-kin",
        "room_id": None,
        "age": 1,
        "resources_contribution": 5,
        "alive": True
    }

def create_inhabitant(world_state=None):
    """Create a new inhabitant in an empty room."""
    if world_state is None:
        world_state = load_state()
    
    # Find rooms with sufficient resources and no current population limit (simplified)
    available_rooms = [r for r in world_state["rooms"] if r["resources"] >= 10]
    
    if not available_rooms:
        return None
    
    # Pick first available room
    room = available_rooms[0]
    inhabitant_id = len(world_state["inhabitants"]) + 1
    
    inhabitant = get_initial_inhabitant()
    inhabitant["id"] = inhabitant_id
    inhabitant["room_id"] = room["id"]
    
    # Update room resources (cost to create inhabitant)
    room["resources"] -= 10
    
    world_state["inhabitants"].append(inhabitant)
    
    save_state(state=world_state)
    
    return inhabitant

def add_bridge(world_state, from_room=None, to_room=None):
    """Add a bridge connecting two rooms."""
    if not from_room or not to_room:
        return None
    
    bridge_id = len(world_state["bridges"]) + 1
    bridge = {
        "id": bridge_id,
        "from": from_room,
        "to": to_room
    }
    
    world_state["bridges"].append(bridge)
    save_state(state=world_state)
    
    return bridge

def update_cycle(world_path=None):
    """Advance the world by one cycle - resources deplete, inhabitants age."""
    state = load_state()
    
    # Deplete resources slowly
    for room in state["rooms"]:
        room["resources"] -= 2
    
    # Age inhabitants
    for inhabitant in state["inhabitants"]:
        inhabitant["age"] += 1
        
        # Death chance increases with age
        if inhabitant["age"] > 20 and roll_death():
            inhabitant["alive"] = False
            
        # Resource contribution
        inhabitant["resources_contribution"] = max(0, inhabitant["resources_contribution"] - 1)
    
    state["cycle_count"] += 1
    save_state(state=state)
    
    return state

def roll_death():
    """Roll for natural death based on age."""
    import random
    return random.random() < 0.05

if __name__ == "__main__":
    # Demo mode
    print("Loading world...")
    state = load_state()
    print(f"Generation: {state['generation']}")
    print(f"Cycles: {state['cycle_count']}")
    print(f"Rooms: {len(state['rooms'])}")
    print(f"Inhabitants: {sum(1 for i in state['inhabitants'] if i['alive'])}")
