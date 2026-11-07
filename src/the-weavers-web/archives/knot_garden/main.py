#!/usr/bin/env python3
"""
Knot Garden - Game Engine (Simplified)

A strategy puzzle game about transforming thread configurations into goal patterns.
"""

import json
from pathlib import Path


class Strand:
    """A single thread segment in the garden."""
    
    def __init__(self, color, length=1):
        self.color = color  # String identifier like "red", "blue"
        self.length = length  # Number of segments
    
    def to_dict(self):
        return {
            "color": self.color,
            "length": self.length
        }


class GardenPlot:
    """A single garden plot being tended."""
    
    def __init__(self, name="unknown"):
        self.name = name
        self.strands = {}  # color -> Strand object
    
    def add_strand(self, color, length=1):
        """Add a thread segment to this plot."""
        if color not in self.strands:
            self.strands[color] = Strand(color=color, length=length)
        else:
            self.strands[color].length += length
    
    def get_state_string(self):
        """Get string representation for pattern matching."""
        return "|".join(f"{c}:{s.length}" for c, s in sorted(self.strands.items()))


class KnotGarden:
    """Main game controller for Knot Garden."""
    
    GOAL_PATTERNS = {}  # State string -> Pattern info
    
    def __init__(self):
        self.plots = []  # List of GardenPlot objects
        self.game_log = []  # History of operations
        self.score = 0
        
    def load_patterns(self, patterns_file="patterns.json"):
        """Load goal and trap pattern definitions."""
        try:
            with open(patterns_file) as f:
                data = json.load(f)
            
            for pattern in data.get("patterns", []):
                state_str = self._pattern_to_state(pattern)
                if state_str not in self.GOAL_PATTERNS:
                    self.GOAL_PATTERNS[state_str] = {
                        "name": pattern["name"],
                        "description": pattern["description"]
                    }
        except FileNotFoundError:
            self._init_default_patterns()
    
    def _pattern_to_state(self, pattern):
        """Convert pattern definition to state string for matching."""
        if "colors" in pattern:
            # Multi-color pattern like Twilight
            colors = pattern["colors"]
            ratio = pattern.get("ratio", "1:1")
            
            # Parse ratio like "1:2"
            try:
                parts = ratio.split(":")
                p1, p2 = int(parts[0]), int(parts[1]) if len(parts) > 1 else 1
                
                state_parts = []
                for i, color in enumerate(colors):
                    length = p1 + (p2 if i == 1 else 0)
                    state_parts.append(f"{color}:{length}")
                return "|".join(sorted(state_parts))
            except:
                # Fallback to simple concatenation
                return "|".join(f"{c}:1" for c in colors)
        else:
            # Single color pattern like Sunrise
            segs = pattern["segments"]
            return f"{pattern['color']}:{segs}"
    
    def _init_default_patterns(self):
        """Initialize with default pattern data."""
        self.GOAL_PATTERNS["red:3"] = {
            "name": "Sunrise Line",
            "description": "Three red segments in a row"
        }
        
        self.GOAL_PATTERNS["blue:2"] = {
            "name": "Moon Circle", 
            "description": "Two blue segments forming a loop"
        }
    
    def get_state_hash(self):
        """Get hashable representation for state lookup."""
        if self.plots and self.plots[0]:
            return self.plots[0].get_state_string()
        return ""
    
    def is_goal_reached(self, goal_pattern_name=None):
        """Check if current configuration matches any goal pattern."""
        current = self.get_state_hash()
        if not current:
            return False
        
        matched = False
        for state_str, info in self.GOAL_PATTERNS.items():
            if state_str == current or info["name"] == goal_pattern_name:
                matched = True
                break
        
        return matched
    
    def get_matched_goal(self):
        """Get information about currently matched goal pattern."""
        current = self.get_state_hash()
        if current in self.GOAL_PATTERNS:
            return self.GOAL_PATTERNS[current]
        return None
    
    def add_strand(self, plot_index, color, length=1):
        """Add thread to specified plot."""
        if 0 <= plot_index < len(self.plots):
            self.plots[plot_index].add_strand(color, length)
    
    def score_current_state(self):
        """Calculate current game score."""
        base_score = 0
        
        # Check for completed goals
        matched_goal = self.get_matched_goal()
        if matched_goal:
            base_score += 5
        
        return base_score
    
    def get_status(self):
        """Get current game status for display."""
        status = f"Score: {self.score}\n"
        if self.plots and self.plots[0]:
            strand_info = []
            for color, strand in sorted(self.plots[0].strands.items()):
                strand_info.append(f"{color}: {strand.length}")
            status += f"Plot 0: {', '.join(strand_info)}\n"
        return status


def main():
    """Main game loop with basic interaction."""
    print("=" * 50)
    print("Welcome to KNOT GARDEN")
    print("Transform thread configurations into beautiful patterns!")
    print("=" * 50)
    
    game = KnotGarden()
    game.load_patterns("patterns.json")
    
    # Create initial plot with some strands
    plot = GardenPlot("main_garden")
    plot.add_strand("red", 1)
    plot.add_strand("blue", 1) 
    plot.add_strand("green", 1)
    
    game.plots = [plot]
    game.score = 0
    
    print()
    print("Current Garden Status:")
    print(game.get_status())
    print()
    print("Goal patterns loaded successfully!")
    print(f"Available patterns: {list(game.GOAL_PATTERNS.values(),)}")


if __name__ == "__main__":
    main()
