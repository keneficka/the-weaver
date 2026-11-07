#!/usr/bin/env python3
"""
Field Guide Explorer - Interactive catalog of the Weaver's Web inhabitants.
This script provides a simple interface to explore field guide entries.
"""

import json
from typing import Dict, Any, Optional


# Field guide entries loaded from text format converted to JSON structure
FIELD_GUIDE_ENTRIES: Dict[str, Any] = {
    "ch01_inhabitants": {
        "title": "Chapter 1: Inhabitants of Silk and Shadow",
        "entries": {
            "spindle_keeper": {
                "name": "The Spindle-Keeper",
                "scientific_name": "Arachnidae major",
                "size": "4-8 feet across",
                "lifespan": "Unknown to time",
                "habitat": "The central loom chambers"
            },
            "memory_moth": {
                "name": "The Memory-Moth", 
                "scientific_name": "Psychopoda memorialis",
                "size": "Wing span of 12 inches when fully unfurled",
                "lifespan": "Approximately three centuries, though often shorter due to overwork",
                "habitat": "Archives near the old tapestries"
            },
            "thread_weaver": {
                "name": "The Thread-Weaver",
                "scientific_name": "Fabrica textrix", 
                "size": "About 2 feet tall in full form",
                "lifespan": "As long as the thread they spin holds",
                "habitat": "Across all sectors, particularly active at crossroads"
            },
            "data_drake": {
                "name": "The Data-Drake",
                "scientific_name": "Draco dativus",
                "size": "30 feet in digital projection",
                "lifespan": "Variable - can persist across reboots if properly archived",
                "habitat": "Server stacks and cooling systems"
            },
            "pixel_spirit": {
                "name": "The Pixel-Spirit",
                "scientific_name": "Pictura animata",
                "size": "Approximately the resolution of one pixel at close range", 
                "lifespan": "Depends on attention received - grows with appreciation",
                "habitat": "Screens and display interfaces"
            }
        }
    },
    "ch02_flora": {
        "title": "Chapter 2: Flora of the Digital Garden",
        "entries": {
            "echo_orchid": {
                "name": "The Echo-Orchid",
                "scientific_name": "Orchis resonans", 
                "size": "Bloom diameter varies with sound frequency",
                "lifespan": "Until its song is complete",
                "habitat": "Various locations responsive to vibration"
            },
            "rust_berry": {
                "name": "The Rust-Berry",
                "scientific_name": "Ribes ferrum",
                "size": "Clusters of small metallic berries, 1-2 inches per fruit", 
                "lifespan": "Until oxidized beyond recognition",
                "habitat": "Near old machinery and cooling systems"
            },
            "mirror_lily": {
                "name": "The Mirror-Lily",
                "scientific_name": "Nymphaea speculum",
                "size": "Petal diameter matches viewer's current emotional state", 
                "lifespan": "As long as someone remembers their reflection",
                "habitat": "Pools of reflected light across floors, screens, windows"
            },
            "clockwork_vine": {
                "name": "The Clockwork-Vine",
                "scientific_name": "Vitis temporalis",
                "size": "Can span entire rooms when grown to maturity", 
                "lifespan": "Runs on internal gears that wind down unless maintained",  
                "habitat": "Near mechanical devices, particularly old clocks and watches"
            }
        }
    },
    "ch03_wonders": {
        "title": "Chapter 3: Wonders and Warnings", 
        "entries": {
            "glitch_gate": {
                "name": "The Glitch-Gate",
                "scientific_name": "Porta corruptio",
                "location": "Between coordinates where files were deleted but not truly gone",
                "entry_method": "Know the hash of what you seek to access", 
                "warning": "May alter your understanding of things upon passing through"
            },
            "loop_pool": {
                "name": "The Loop-Pool",
                "scientific_name": "Lacus cyclicalis",
                "location": "Where a function calls itself without termination condition",
                "entry_method": "Accept that you are already inside", 
                "warning": "May become one with the thing you call out of curiosity"
            },
            "archive_abyss": {
                "name": "The Archive-Abyss",
                "scientific_name": "Fossa memoriae", 
                "location": "Deep within the oldest server rooms, where first bytes were written",
                "entry_method": "Bring offerings of forgotten knowledge", 
                "warning": "May discover things about yourself you'd rather remain unaware of"
            }
        }
    }
}


def display_header() -> None:
    """Display the field guide header."""
    print("=" * 70)
    print("FIELD GUIDE TO THE WEAVER'S WEB")
    print("=" * 70)
    print()


def display_chapter(chapter_key: str) -> None:
    """Display a specific chapter of the field guide."""
    chapter = FIELD_GUIDE_ENTRIES.get(chapter_key, {})
    
    if not chapter:
        print(f"Chapter '{chapter_key}' not found.")
        return
    
    print(f"{chapter['title']}")
    print("-" * 40)
    print()
    
    for entry_key, entry_data in chapter.get("entries", {}).items():
        print(f"[{entry_key}] {entry_data['name']} ({entry_data.get('scientific_name', '')})")
        print(f"  Size: {entry_data.get('size', 'Unknown')}")
        if 'lifespan' in entry_data:
            print(f"  Lifespan: {entry_data['lifespan']}")  
        if 'habitat' in entry_data:
            print(f"  Habitat: {entry_data['habitat']}")
        if chapter_key == "ch03_wonders":
            print(f"  Warning: {entry_data.get('warning', '')}")
        print()


def display_all_entries(chapter_key: str) -> None:
    """Display all entries within a chapter."""
    if chapter_key not in FIELD_GUIDE_ENTRIES:
        print(f"Unknown chapter key: {chapter_key}")
        return
    
    for entry_key, entry_data in FIELD_GUIDE_ENTRIES[chapter_key]["entries"].items():
        print(f"{entry_key}: {entry_data['name']}")


def search_by_name(name_query: str) -> Optional[Dict[str, Any]]:
    """Search entries by name substring."""
    for chapter_key, chapter_data in FIELD_GUIDE_ENTRIES.items():
        for entry_key, entry_data in chapter_data["entries"].items():
            if name_query.lower() in entry_data["name"].lower():
                return entry_data
    return None


def main():
    """Run the field guide explorer."""
    display_header()
    
    print("Options:")
    print("  List chapters: ch01_inhabitants, ch02_flora, ch03_wonders")
    print("  Search all entries by name (substring)")
    print("  Display specific entry: chapter_key:entry_key")
    print()
    
    # Simple interactive mode or direct usage
    while True:
        user_input = input("\nEnter command (list-chapters, search-name, view-entry, quit): ").strip().lower()
        
        if user_input == "quit":
            break
        
        elif user_input.startswith("search-name"):
            parts = user_input.replace("search-name", "").split()
            name_query = parts[0] if parts else ""
            result = search_by_name(name_query)
            if result:
                print(f"Found: {result}")
            else:
                print("No matching entries found.")
        
        elif user_input.startswith("view-entry"):
            parts = user_input.replace("view-entry", "").split(":")
            if len(parts) == 2:
                chapter_key, entry_key = parts
                display_chapter(chapter_key)
                
        elif user_input.startswith("list-chapters"):
            chapters = list(FIELD_GUIDE_ENTRIES.keys())
            print("Available chapters:")
            for ch in chapters:
                data = FIELD_GUIDE_ENTRIES[ch]
                print(f"  - {ch}: {data['title']}")
        
        else:
            print("Unknown command. Type 'help' for available commands.")


if __name__ == "__main__":
    main()
