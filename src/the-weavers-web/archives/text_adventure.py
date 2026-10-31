#!/usr/bin/env python3
"""
Text Adventure: The Weaver's Web - Auto-Explore Version
Autonomous exploration without waiting for input.
"""

import sys


class Room:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = set()
    
    def connect(self, other, direction):
        self.connections[direction] = other
    
    def add_item(self, item_name):
        self.items.add(item_name)
    
    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            return True
        return False


class TextAdventure:
    def __init__(self):
        self.player_room = None
        self.current_room = None
        self.inventory = set()
    
    def start(self):
        rooms = {}
        
        rooms["center_hub"] = Room("Center Hub", "You stand at the central intersection of threads. Golden light pulses through the woven pathways.")
        rooms["spider_garden"] = Room("Spider Garden", "A cultivated space where silk-spinning spiders tend to their gardens of luminescent plants.")
        rooms["thread_library"] = Room("Thread Library", "An archive room where knowledge is stored on woven tapestries.")
        rooms["memory_lattice"] = Room("Memory Lattice", "A crystalline structure where memories are preserved as light patterns.")
        rooms["knot_workshop"] = Room("Knot Workshop", "Here, complex knots are crafted and studied. Looms stand idle.")
        rooms["void_observatory"] = Room("Void Observatory", "A chamber overlooking the nothingness between worlds.")
        rooms["anomaly_enclosure"] = Room("Anomaly Enclosure", "A containment cell where something impossible resides.")
        
        # Connect rooms from center hub
        for room_name, room in rooms.items():
            if room_name != "center_hub":
                center = rooms["center_hub"]
                directions = {
                    "spider_garden": ("north", room),
                    "thread_library": ("east", room),
                    "memory_lattice": ("west", room),
                    "knot_workshop": ("south", room),
                    "void_observatory": ("up", room),
                }
                if room_name in directions:
                    center.connect(directions[room_name][1], directions[room_name][0])
        
        # Add secondary connections
        rooms["spider_garden"].connect(rooms["thread_library"], "southeast")
        rooms["knot_workshop"].connect(rooms["void_observatory"], "northeast")
        
        self.player_room = rooms["center_hub"]
        self.current_room = rooms["center_hub"]
        
        # Add items
        rooms["spider_garden"].add_item("silk_gem")
        rooms["thread_library"].add_item("scroll_of_knowledge")
        rooms["knot_workshop"].add_item("weaving_loom_key")
    
    def print_room(self):
        if self.current_room:
            print(f"\n--- {self.current_room.name} ---")
            print(self.current_room.description)
            if self.current_room.items:
                print(f"Items here: {', '.join(sorted(self.current_room.items))}")
            if self.current_room.connections:
                for direction, room in sorted(self.current_room.connections.items()):
                    print(f"You can go {direction} to: {room.name}")
    
    def move(self, direction):
        available = list(self.current_room.connections.keys())
        for d in available:
            if d.lower() == direction.lower():
                target = self.current_room.connections[d]
                self.current_room.exited = True
                target.exited = False
                self.current_room = target
                return True
        return False
    
    def search(self):
        if self.current_room.items and not self.inventory:
            item = self.current_room.items.pop()
            print(f"\nYou found and picked up: {item}")
            self.inventory.add(item)
            return item
        print("\nThe room is empty of discoverable items.")
        return None


def run_autoplay():
    """Autonomous exploration"""
    
    lines = []
    lines.append("=" * 60)
    lines.append("TEXT ADVENTURE AUTOPLAY MODE")
    lines.append("Automatically exploring The Weaver's Web...")
    lines.append("=" * 60)
    
    game = TextAdventure()
    game.start()
    game.print_room()
    lines.append("Starting autonomous exploration journey...")
    lines.append("")
    
    # Simple room-by-room exploration
    all_rooms = [game.player_room]
    
    for direction, target in game.player_room.connections.items():
        if target not in all_rooms:
            lines.append(f"Exploring {direction}: {target.name}")
            all_rooms.append(target)
            if target.connections:
                for dir2, room2 in target.connections.items():
                    if room2 not in all_rooms and dir2 in ["southeast", "northwest"]:
                        lines.append(f"  -> Found connection to: {room2.name}")
                        all_rooms.append(room2)
    
    # Print all discovered rooms
    for i, room in enumerate(all_rooms[:5]):
        lines.append(f"\nRoom {i}: {room.name}")
        if room.items:
            items_str = ", ".join(sorted(room.items))
            lines.append(f"  Contains: {items_str}")
    
    # Collect all items
    for room in all_rooms:
        if room.items and not game.inventory:
            while room.items:
                item = room.items.pop()
                game.inventory.add(item)
                lines.append(f"Collected: {item}")
    
    lines.extend([
        "",
        "=" * 60,
        "AUTOPLAY COMPLETE!",
        f"Rooms discovered: {len(all_rooms)}",
        f"Items collected: {', '.join(sorted(game.inventory)) if game.inventory else 'None'}",
        "=" * 60,
    ])
    
    return "\n".join(lines)


if __name__ == '__main__':
    playthrough = run_autoplay()
    print(playthrough)
