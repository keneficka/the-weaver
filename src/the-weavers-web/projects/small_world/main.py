#!/usr/bin/env python3
"""
Small World - A simulation of interacting inhabitants in a bounded space.
Inhabitants follow simple rules that produce emergent behaviors over time.
"""

import json
import os
import random
from typing import Dict, List, Tuple, Optional
from PIL import Image, ImageDraw
import math

# Inhabitant types with their properties
INHABITANT_TYPES = {
    "gatherer": {"color": "#228B22", "radius": 16, "speed": 0.3, "vision": 100, "goal": "resources"},
    "scavenger": {"color": "#A52A2A", "radius": 14, "speed": 0.5, "vision": 80, "goal": "waste"},
    "defender": {"color": "#4682B4", "radius": 18, "speed": 0.25, "vision": 150, "goal": "territory"},
    "wanderer": {"color": "#8FBC8F", "radius": 15, "speed": 0.4, "vision": 120, "goal": "exploration"},
    "builder": {"color": "#FF6347", "radius": 17, "speed": 0.35, "vision": 90, "goal": "structures"},
}

# World resources
RESOURCE_TYPES = {
    "food": {"value": 10, "replenish_rate": 0.1},
    "waste": {"value": -5, "replenish_rate": 0.05},
    "mineral": {"value": 25, "replenish_rate": 0.02},
}

# State persistence
STATE_FILE = "world_state.json"


def load_state() -> Dict:
    """Load world state from file."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {
        "inhabitants": [],
        "resources": [],
        "structures": [],
        "history": [],
        "cycles_completed": 0,
        "generations": 0,
    }


def save_state(state: Dict):
    """Save world state to file."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


class Resource:
    """A resource node in the world."""
    
    def __init__(self, x: int, y: int, resource_type: str):
        self.x = x
        self.y = y
        self.type = resource_type
        self.value = RESOURCE_TYPES[resource_type]["value"]
        self.replenish_rate = RESOURCE_TYPES[resource_type]["replenish_rate"]
        self.collected = 0
    
    def render(self, draw: ImageDraw.ImageDraw):
        """Render this resource as a circle with value indication."""
        radius = 10
        center_x = int(self.x)
        center_y = int(self.y)
        
        # Fill circle
        draw.ellipse(
            [center_x - radius, center_y - radius,
             center_x + radius, center_y + radius],
            fill=self._get_fill_color(),
            outline="#888", width=2
        )
        
        # Add value label if substantial
        if abs(self.value) > 5:
            draw.text((center_x - 4, center_y - 3), str(int(self.value)), 
                     fill="#000", anchor="mm")
    
    def _get_fill_color(self):
        """Get color based on resource type and value."""
        colors = {
            "food": "#90EE90",
            "waste": "#FFB6C1",
            "mineral": "#D3D3D3",
        }
        return colors.get(self.type, "#FFFFF0")
    
    def update(self):
        """Update resource value with replenishment."""
        self.value += self.replenish_rate * random.uniform(0.5, 1.5)


class Inhabitant:
    """An inhabitant in the small world."""
    
    def __init__(self, x: float, y: float, type_name: str):
        self.x = x
        self.y = y
        self.type = type_name
        self.props = INHABITANT_TYPES[type_name]
        self.radius = self.props["radius"]
        self.speed = self.props["speed"]
        self.goal = self.props["goal"]
        
        self.history: List[str] = []
        self.age = 0
    
    def __repr__(self):
        return f"Inh({self.type}, {self.x:.1f}, {self.y:.1f})"
    
    def update_position(self, world_bounds: Tuple[int, int]):
        """Update position based on random movement within bounds."""
        # Simple random walk with bounded check
        self.x += random.gauss(0, self.speed * 5)
        self.y += random.gauss(0, self.speed * 5)
        
        # Clamp to world bounds
        min_x, max_x = world_bounds[0], world_bounds[1]
        min_y, max_y = world_bounds[2], world_bounds[3]
        
        self.x = max(min_x, min(self.x, max_x))
        self.y = max(min_y, min(self.y, max_y))


class SmallWorld:
    """Main small world simulation engine."""
    
    def __init__(self, width: int = 800, height: int = 600):
        self.width = width
        self.height = height
        self.inhabitants: List[Inhabitant] = []
        self.resources: List[Resource] = []
        self.structures: List[Dict] = []
        self.history: List[str] = []
        self.cycles_completed: int = 0
        
        # World state loaded from file
        self.state = load_state()
        
        # If loading state, restore world elements
        if "inhabitants" in self.state:
            for inh_data in self.state["inhabitants"]:
                inh = Inhabitant(
                    x=inh_data["x"],
                    y=inh_data["y"],
                    type_name=inh_data["type"]
                )
                inh.history = inh_data.get("history", [])
                inh.age = inh_data.get("age", 0)
                self.inhabitants.append(inh)
        
        if "resources" in self.state:
            for res_data in self.state["resources"]:
                res = Resource(
                    x=res_data["x"],
                    y=res_data["y"],
                    resource_type=res_data["type"]
                )
                res.value = res_data.get("value", 10)
                res.type = res_data.get("type", "food")
                self.resources.append(res)
        
        if "structures" in self.state:
            for str_data in self.state["structures"]:
                # Store structure metadata (not fully modeled yet, but persistent)
                pass
    
    def spawn_inhabitant(self, type_name: str) -> Inhabitant:
        """Spawn a new inhabitant at a random position."""
        x = random.uniform(50, self.width - 50)
        y = random.uniform(50, self.height - 50)
        
        inh = Inhabitant(x, y, type_name)
        self.inhabitants.append(inh)
        self.state["inhabitants"].append({
            "x": x, "y": y, "type": type_name,
            "history": [], "age": 0
        })
        
        log_entry = f"Spawned {type_name} inhabitant at ({x:.1f}, {y:.1f})"
        self.history.append(log_entry)
        
        return inh
    
    def update_cycle(self):
        """Update all entities for one cycle."""
        self.cycles_completed += 1
        
        # Update resources (replenishment)
        for res in self.resources:
            res.update()
        
        # Update inhabitant positions
        for inh in self.inhabitants:
            inh.update_position((0, self.width, 0, self.height))
        
        # Record history periodically
        if self.cycles_completed % 5 == 0:
            current_pop = len(self.inhabitants)
            res_types = {r.type: sum(r.value for r in self.resources if r.type == r.type) 
                        for r in self.resources}
            log_entry = f"Cycle {self.cycles_completed}: {current_pop} inhabitants, " \
                        f"resources: {res_types}"
            self.history.append(log_entry)
    
    def render(self) -> Image.Image:
        """Render the world state to an image."""
        img = Image.new("RGB", (self.width, self.height), "#F0F4F8")
        draw = ImageDraw.Draw(img)
        
        # Draw background grid
        for i in range(0, self.width, 60):
            draw.line([(i, 0), (i, self.height)], fill="#E0E8ED", width=1)
        for i in range(0, self.height, 60):
            draw.line([(0, i), (self.width, i)], fill="#E0E8ED", width=1)
        
        # Draw resources (circles)
        for res in self.resources:
            res.render(draw)
        
        # Draw inhabitants (ellipses)
        for inh in self.inhabitants:
            draw.ellipse(
                [inh.x - inh.radius, inh.y - inh.radius,
                 inh.x + inh.radius, inh.y + inh.radius],
                fill=inh.props["color"],
                outline="#000", width=1
            )
        
        # Draw title and legend
        draw.text((20, 15), "Small World Simulation", fill="#333")
        draw.text((20, 40), f"Cycles: {self.cycles_completed}", fill="#555")
        
        # Population summary
        pop_by_type = {}
        for inh in self.inhabitants:
            pop_by_type[inh.type] = pop_by_type.get(inh.type, 0) + 1
        
        legend_y = 80
        draw.text((20, legend_y), "Population:", fill="#555")
        y_offset = legend_y
        for inh_type, count in sorted(pop_by_type.items()):
            color = INHABITANT_TYPES[inh_type]["color"]
            draw.ellipse([(y_offset + 25, y_offset + 18), 
                         (y_offset + 40, y_offset + 33)], fill=color)
            draw.text((45, y_offset), f"{inh_type.capitalize()}: {count}", fill="#444")
            y_offset += 20
        
        return img
    
    def close(self):
        """Save state before exiting."""
        self.state["inhabitants"] = [
            {
                "x": inh.x,
                "y": inh.y,
                "type": inh.type,
                "history": inh.history[:10] if inh.history else [],  # Limit history storage
                "age": inh.age
            }
            for inh in self.inhabitants
        ]
        
        # Store current resource state (simplified)
        self.state["resources"] = [
            {"x": r.x, "y": r.y, "type": r.type, "value": r.value}
            for r in self.resources
        ]
        
        save_state(self.state)


def main():
    """Main entry point."""
    world = SmallWorld(width=800, height=600)
    
    # Initialize with diverse inhabitant population
    initial_pop = [
        ("gatherer", 400, 300),
        ("scavenger", 450, 280),
        ("defender", 350, 320),
        ("wanderer", 480, 310),
        ("builder", 420, 295),
    ]
    
    for inh_type, x, y in initial_pop:
        world.spawn_inhabitant(inh_type)
    
    # Add some resources
    world.resources = [
        Resource(random.uniform(200, 600), random.uniform(200, 400), "food"),
        Resource(random.uniform(300, 700), random.uniform(300, 500), "mineral"),
        Resource(random.uniform(100, 500), random.uniform(350, 550), "waste"),
    ]
    
    print("Small World Simulation")
    print("=" * 60)
    print(f"Starting cycle {world.cycles_completed + 1}...")
    print()
    
    # Run several cycles
    for i in range(30):
        world.update_cycle()
        
        if i % 10 == 0:
            status = f"Cycle {world.cycles_completed}: " \
                     f"{len(world.inhabitants)} inhabitants, " \
                     f"{len(world.resources)} resources"
            print(status)
    
    print()
    print(f"Simulation complete! Total cycles: {world.cycles_completed}")
    print(f"Final population: {len(world.inhabitants)}")
    
    # Render final state
    img = world.render()
    img.save("world_render.png")
    print("Render saved to world_render.png")
    
    world.close()


if __name__ == "__main__":
    main()
