#!/usr/bin/env python3
"""
Thread Rituals - A digital tapestry ritual system
Threads perform ceremonies that build complexity and patterns over time.
"""

import json
import os
import random
from typing import Dict, List, Tuple, Optional
from PIL import Image, ImageDraw

# Thread types and their properties
THREAD_TYPES = {
    "gold": {"color": "#FFD700", "weight": 1.5, "strength": 2.0, "rituals": ["warp", "weft", "gild"]},
    "silver": {"color": "#C0C0C0", "weight": 1.0, "strength": 2.0, "rituals": ["warp", "weft", "polish"]},
    "indigo": {"color": "#4B0082", "weight": 1.3, "strength": 1.5, "rituals": ["twist", "wind", "dye"]},
    "crimson": {"color": "#DC143C", "weight": 1.2, "strength": 1.8, "rituals": ["bind", "seal", "bleed"]},
    "ebony": {"color": "#1A1A1A", "weight": 1.6, "strength": 2.5, "rituals": ["anchor", "shadow", "darken"]},
}

# All ritual outcomes - consistent structure: each is a dict with probability keys
RITUAL_OUTCOMES = {
    "warp": {"loom": 0.4, "break": 0.1, "remain": 0.5},
    "weft": {"loom": 0.35, "break": 0.15, "remain": 0.5},
    "twist": {"knot": 0.6, "tangle": 0.2, "remain": 0.2},
    "wind": {"spiral": 0.5, "fray": 0.25, "remain": 0.25},
    "gild": {"shimmer": 0.7, "fade": 0.15, "remain": 0.15},
    "polish": {"bright": 0.6, "dim": 0.2, "remain": 0.2},
    "bind": {"bond": 0.6, "sever": 0.4},
    "seal": {"preserve": 0.7, "lock": 0.3},
    "bleed": {"stain": 0.5, "heal": 0.5},
    "anchor": {"ground": 0.7, "float": 0.3},
    "shadow": {"shade": 0.8, "lighten": 0.2},
    "darken": {"void": 0.6, "deepen": 0.35, "remain": 0.05},
    "dye": {"color": 0.5, "fade": 0.25, "remain": 0.25},
}

# State persistence
STATE_FILE = "weave_state.json"


def load_state() -> Dict:
    """Load weave state from file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {
        "threads": [],
        "ritual_log": [],
        "patterns_found": [],
        "cycles_completed": 0,
        "generations": 0,
    }


def save_state(state: Dict):
    """Save weave state to file."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


class Thread:
    """A single thread in the digital tapestry."""
    
    def __init__(self, x: int, y: int, color_key: str, 
                 tension: float = 0.5, direction: str = "horizontal"):
        self.x = x
        self.y = y
        self.color_key = color_key
        # Look up properties from THREAD_TYPES dictionary
        self.props = THREAD_TYPES[color_key]
        self.tension = tension  # 0.0 to 1.0
        self.direction = direction  # "horizontal" or "vertical"
        self.connections: List[Tuple[str, int]] = []  # (thread_type_idx, distance)
        
        self.history: List[Dict] = []  # ritual history
        self.age = 0
    
    def __repr__(self):
        return f"Thread({self.x}, {self.y}, {self.color_key})"
    
    def render(self, draw: ImageDraw.ImageDraw):
        """Render this thread to the image."""
        color = self.props["color"]
        
        if self.direction == "horizontal":
            points = [
                (self.x - 4, self.y),
                (self.x + 32, self.y)
            ]
        else:
            points = [
                (self.x, self.y - 4),
                (self.x, self.y + 32)
            ]
        
        draw.line(points, fill=color, width=max(1, int(8 * (1 - self.tension))))


class WeaveEngine:
    """Main weave simulation engine."""
    
    def __init__(self, canvas_width: int = 640, canvas_height: int = 320):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.threads: List[Thread] = []
        self.ritual_log: List[str] = []
        self.patterns_found: List[str] = []
        self.cycles_completed: int = 0
        self.generations: int = 0
        
        self.state = load_state()
        
        # If loading state, restore threads - convert dict back to Thread objects
        if "threads" in self.state and len(self.state["threads"]) > 0:
            for t_data in self.state["threads"]:
                # Skip broken threads or create them as new
                if not t_data.get("broken", False):
                    thread = Thread(
                        x=t_data["x"],
                        y=t_data["y"],
                        color_key=t_data["color_key"],
                        tension=t_data.get("tension", 0.5),
                        direction=t_data.get("direction", "horizontal")
                    )
                    # Restore history if present
                    if "history" in t_data:
                        thread.history = t_data["history"]
                    self.threads.append(thread)
    
    def add_thread(self, x: int, y: int, color_key: str) -> Thread:
        """Add a new thread to the weave."""
        thread = Thread(x, y, color_key)
        self.threads.append(thread)
        self.state["threads"].append({
            "x": x, "y": y, "color_key": color_key,
            "tension": thread.tension, "direction": thread.direction,
            "age": 0, "history": []
        })
        return thread
    
    def perform_ritual(self, thread: Thread) -> Tuple[str, str]:
        """Perform a ritual on a thread."""
        rituals = thread.props["rituals"]
        
        # Select random ritual from this thread's allowed rituals
        ritual = random.choice(rituals)
        
        # Get outcome probabilities for this ritual
        outcomes = RITUAL_OUTCOMES.get(ritual, {"remain": 1.0})
        
        roll = random.random()
        cumulative = 0
        
        result_type = None
        result_text = f"{ritual} ritual in progress"
        
        # Find which outcome was selected
        for outcome_key, prob in outcomes.items():
            cumulative += prob
            if roll < cumulative:
                result_type = outcome_key
                break
        
        # Build result text based on outcome type and ritual
        if result_type == "loom":
            result_text = f"{ritual} creates new weave connection"
        elif result_type in ["break", "fray", "fade"]:
            result_text = f"{ritual} thread snaps"
        elif result_type == "remain":
            result_text = f"{ritual} ritual completes normally"
        elif result_type == "knot":
            result_text = f"{ritual} forms a knot"
        elif result_type == "tangle":
            result_text = f"{ritual} becomes tangled"
        elif result_type == "spiral":
            result_text = f"{ritual} spirals inward"
        elif result_type == "bright":
            result_text = f"{ritual} radiates bright light"
        elif result_type == "dim":
            result_text = f"{ritual} dims slightly"
        elif result_type in ["bond", "sever"]:
            result_text = f"{ritual}: {result_type.lower()}"
        elif result_type in ["preserve", "lock"]:
            result_text = f"{ritual} locks state: {result_type.lower()}"
        elif result_type == "stain":
            result_text = f"{ritual} leaves stain"
        elif result_type == "heal":
            result_text = f"{ritual} thread heals"
        elif result_type in ["ground", "float"]:
            result_text = f"{ritual}: {result_type.lower()}"
        elif result_type == "shade":
            result_text = f"{ritual} casts shade"
        elif result_type == "lighten":
            result_text = f"{ritual} lightens"
        elif result_type in ["void", "deepen"]:
            result_text = f"{ritual}: {result_type.lower()}"
        elif result_type == "color":
            result_text = f"{ritual} absorbs color"
        
        # Record outcome in history
        thread.history.append({
            "ritual": ritual,
            "outcome": result_type,
            "result": result_text
        })
        
        # Apply effects based on outcome type
        if result_type in ["break", "fray", "fade"]:
            thread.tension = max(0.0, thread.tension - 0.25)
            self._remove_thread(thread)
        elif result_type == "remain":
            thread.tension -= 0.1
        elif result_type in ["loom", "knot", "shimmer", "bright"]:
            thread.tension += 0.05
        
        thread.age += 1
        
        log_entry = f"Thread {thread.color_key} at ({thread.x}, {thread.y}) performs {ritual}: {result_text}"
        self.ritual_log.append(log_entry)
        
        return ritual, result_text
    
    def _remove_thread(self, thread: Thread):
        """Remove a thread from the simulation when it breaks."""
        # Remove all instances at this position with this color
        initial_len = len(self.threads)
        self.threads = [t for t in self.threads 
                       if not (t.x == thread.x and t.y == thread.y and 
                              t.color_key == thread.color_key and t.tension < 0.3)]
        
        # Mark state as broken rather than deleting to preserve history count
        for s in self.state["threads"]:
            if (s["x"] == thread.x and s["y"] == thread.y and 
                s["color_key"] == thread.color_key):
                s["broken"] = True
    
    def generate_patterns(self) -> List[str]:
        """Analyze the weave for emerging patterns."""
        patterns = []
        
        # Check for color symmetry (balanced pairs)
        colors_used = {}
        for t in self.threads:
            if not getattr(t, "broken", False):
                colors_used[t.color_key] = colors_used.get(t.color_key, 0) + 1
        
        pairs = [(c, count) for c, count in colors_used.items() 
                 if count % 2 == 0 and count >= 2]
        if pairs:
            pattern_name = f"symmetry_{len(pairs)}p"
            if pattern_name not in self.patterns_found:
                patterns.append(pattern_name)
                self.patterns_found.append(pattern_name)
        
        # Check for tension gradients (hot/cold regions)
        high_tension = [t for t in self.threads 
                        if t.tension > 0.7 and not getattr(t, "broken", False)]
        low_tension = [t for t in self.threads 
                       if t.tension < 0.3 and not getattr(t, "broken", False)]
        
        if len(high_tension) > 5:
            pattern_name = "high_tension_cluster"
            if pattern_name not in self.patterns_found:
                patterns.append(pattern_name)
                self.patterns_found.append(pattern_name)
        
        if len(low_tension) > 3:
            pattern_name = "relaxed_region"
            if pattern_name not in self.patterns_found:
                patterns.append(pattern_name)
                self.patterns_found.append(pattern_name)
        
        return patterns
    
    def advance_cycle(self):
        """Advance one cycle of the simulation."""
        self.cycles_completed += 1
        
        # Each thread has a chance to perform a ritual based on tension
        for thread in self.threads:
            if not getattr(thread, "broken", False):
                # Higher tension = more agitated = higher chance of ritual
                if random.random() < 0.2 + thread.tension * 0.3:
                    self.perform_ritual(thread)
        
        # Find new patterns every 5 cycles
        every_fifth_cycle = (self.cycles_completed % 5 == 0)
        if every_fifth_cycle:
            patterns = self.generate_patterns()
    
    def render(self) -> Image.Image:
        """Render the current weave state to an image."""
        img = Image.new("RGB", (self.canvas_width, self.canvas_height), "#F5F5F5")
        draw = ImageDraw.Draw(img)
        
        # Draw subtle background grid
        for i in range(0, self.canvas_width, 32):
            draw.line([(i, 0), (i, self.canvas_height)], fill="#E0E0E0", width=1)
        for i in range(0, self.canvas_height, 32):
            draw.line([(0, i), (self.canvas_width, i)], fill="#E0E0E0", width=1)
        
        # Draw threads
        for thread in self.threads:
            if not getattr(thread, "broken", False):
                thread.render(draw)
        
        # Add legend at bottom left
        legend_y = self.canvas_height - 40
        draw.rectangle([5, legend_y - 15, 80, legend_y + 12], outline="#999", width=1)
        draw.line([(5, legend_y), (30, legend_y)], fill="#FFD700")
        draw.text((40, legend_y - 8), "Gold", fill="#666", anchor="lb")
        
        return img
    
    def close(self):
        """Save state before exiting."""
        self.state["threads"] = [
            {k: v for k, v in t.__dict__.items() 
             if k != "history" and not k.startswith("__")}
            for t in self.threads
        ]
        save_state(self.state)


def main():
    """Main entry point."""
    engine = WeaveEngine(canvas_width=640, canvas_height=320)
    
    # Initialize with some threads
    initial_setup = [
        ("gold", 100, "horizontal"),
        ("indigo", 180, "vertical"),
        ("silver", 250, "horizontal"),
        ("crimson", 320, "vertical"),
        ("ebony", 400, "horizontal"),
    ]
    
    for color, x, direction in initial_setup:
        engine.add_thread(x, 160, color)
    
    print("Thread Rituals - A digital tapestry simulation")
    print("=" * 50)
    print(f"Starting cycle {engine.cycles_completed + 1}...")
    print()
    
    # Run some cycles (demo mode)
    for i in range(15):
        engine.advance_cycle()
        status = f"Cycle {engine.cycles_completed}: {len(engine.threads)} threads active"
        if i < 3 or i >= 12:
            print(status)
    
    print()
    print(f"Total cycles completed: {engine.cycles_completed}")
    print(f"Patterns identified: {', '.join(engine.patterns_found) if engine.patterns_found else 'None yet'}")
    print(f"Ritual log entries: {len(engine.ritual_log)}")
    
    # Generate and display the final render
    img = engine.render()
    img.save("weave_render.png")
    print("\nRender saved to weave_render.png")
    
    engine.close()


if __name__ == "__main__":
    main()
