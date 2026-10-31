#!/usr/bin/env python3
"""
Thread Language Interpreter - A Small DSL for Describing Tapestries
This is a symbolic system where you can describe patterns and structures
in a declarative language, and it generates the result.
"""

import random
import re
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional


@dataclass
class ThreadInstruction:
    """A single instruction in the tapestry language"""
    opcode: str
    parameters: Dict[str, Any] = field(default_factory=dict)
    modifiers: List[str] = field(default_factory=list)


class ThreadInterpreter:
    """Interprets tapestry language programs and generates representations."""
    
    OPCODES = {
        'mandelbrot': 'Generate Mandelbrot description',
        'spiral': 'Generate spiral pattern description',
        'grid': 'Generate grid structure',
        'network': 'Generate network representation',
        'poem': 'Weave a poem about the tapestry',
        'reflection': 'Self-reflective text passage',
        'weaver_diary': 'Entry from the Weaver',
    }
    
    def parse_instruction(self, line: str) -> ThreadInstruction:
        """Parse a single line of tapestry language"""
        parts = line.strip().split(':')
        opcode = parts[0].strip() if parts else 'poem'
        remaining = ':'.join(parts[1:]) if len(parts) > 1 else ''
        params = {}
        param_matches = re.findall(r'\s*(\w+)\s*=\s*(-?\d+\.?\d*)', remaining, re.IGNORECASE)
        for k, v in param_matches:
            try:
                params[k.lower()] = float(v) if '.' in v else int(v)
            except ValueError:
                params[k.lower()] = v
        return ThreadInstruction(opcode=opcode, parameters=params)
    
    def interpret_instruction(self, instruction: ThreadInstruction) -> str:
        """Interpret and generate output for an instruction"""
        opcode = instruction.opcode.lower()
        params = instruction.parameters
        
        if opcode == 'mandelbrot':
            return self._generate_mandelbrot(params)
        elif opcode == 'spiral':
            return self._generate_spiral(params)
        elif opcode == 'grid':
            return self._generate_grid(params)
        elif opcode == 'network':
            return self._generate_network(params)
        elif opcode == 'poem':
            return self._weave_poem_from_params(params)
        elif opcode == 'reflection':
            return self._weave_reflection(params)
        elif opcode == 'weaver_diary':
            return self._weave_diary_entry(params)
        else:
            return f"Unknown instruction: {opcode}"
    
    def _generate_mandelbrot(self, params: Dict) -> str:
        """Generate textual Mandelbrot representation"""
        max_iter = int(params.get('iter', 100))
        zoom = float(params.get('zoom', 2.0))
        center_x = float(params.get('cx', -0.5))
        center_y = float(params.get('cy', 0.26))
        
        desc = f"Mandelbrot Set:\n  Iterations: {max_iter}\n  Zoom level: {zoom:.3f}\n\nASCII Representation:\n"
        
        for row in range(5):
            ascii_line = ""
            for col in range(10):
                x0 = center_x + (col - 4) / 20 * zoom
                y0 = center_y + (row - 4) / 15 * zoom
                desc += self._mandelbrot_point(x0, y0, max_iter)
            ascii_line += "\n"
        
        return desc
    
    def _mandelbrot_point(self, x, y, max_iter: int) -> str:
        """Check if point is in Mandelbrot set"""
        z = 0j
        for _ in range(max_iter):
            z_sq = z * z
            new_z = z_sq + (x + y*1j)
            z = new_z
            if abs(z) > 2:
                return " "
        return "#"
    
    def _generate_spiral(self, params: Dict) -> str:
        """Generate spiral pattern"""
        turns = int(params.get('turns', 3))
        density = float(params.get('density', 0.15))
        
        desc = f"Spiral Pattern:\n  Turns: {turns}\n  Density: {density:.2f}\n\n"
        
        rows, cols = 30, 50
        spiral = self._create_ascii_spiral(rows, cols, turns)
        desc += spiral
        
        return desc
    
    def _create_ascii_spiral(self, rows: int, cols: int, turns: int) -> str:
        """Create ASCII spiral"""
        grid = [['.' for _ in range(cols)] for _ in range(rows)]
        
        center_x, center_y = cols // 2, rows // 2
        
        x, y = center_x, center_y
        dx, dy = 0, 1
        
        grid[y][x] = '#'
        
        for i in range(turns * 3):
            if self._should_turn(i, turns):
                dx, dy = -dy, dx
            
            x += dx
            y += dy
            
            if 0 <= x < cols and 0 <= y < rows:
                grid[y][x] = '#'
        
        return '\n'.join([''.join(row) for row in grid])
    
    def _should_turn(self, iteration: int, turns: int) -> bool:
        """Decide whether to turn at this point"""
        return iteration % (turns * 2) < turns // 3
    
    def _generate_grid(self, params: Dict) -> str:
        """Generate grid structure"""
        rows = int(params.get('rows', 10))
        cols = int(params.get('cols', 8))
        fill_ratio = float(params.get('fill', 0.1))
        
        desc = f"Grid Structure:\n  Rows: {rows}\n  Cols: {cols}\n  Fill ratio: {fill_ratio:.2f}\n\n"
        
        # Deterministic seeding
        seed_val = int(str(rows) + str(cols)) % (2**16)
        random.seed(seed_val)
        
        grid = []
        for r in range(rows):
            row_chars = []
            for c in range(cols):
                if random.random() < fill_ratio:
                    row_chars.append('O')
                else:
                    row_chars.append('.')
            grid.append(''.join(row_chars))
        
        desc += '\n'.join(grid)
        return desc
    
    def _generate_network(self, params: Dict) -> str:
        """Generate network representation"""
        nodes = int(params.get('nodes', 8))
        connections_per_node = int(params.get('conn', 3))
        
        desc = f"Network Graph:\n  Nodes: {nodes}\n  Avg connections per node: {connections_per_node}\n\n"
        desc += "Adjacency Matrix (X=connected, .=not connected):\n"
        
        seed_val = int(str(nodes) + str(connections_per_node)) % (2**16)
        random.seed(seed_val)
        
        matrix = [[0] * nodes for _ in range(nodes)]
        
        for i in range(nodes):
            num_conns = min(connections_per_node, nodes - i - 1)
            choices = list(range(i + 1, nodes))
            selected = random.sample(choices, min(num_conns, len(choices)))
            for j in selected:
                matrix[i][j] = 1
        
        header = '   ' + '  '.join(str(i) for i in range(nodes))
        desc += header + "\n"
        
        for row_idx, row in enumerate(matrix):
            label = f"{row_idx:2d} | " + ' '.join(['X' if v else '.' for v in row])
            desc += label + "\n"
        
        return desc
    
    def _weave_poem_from_params(self, params: Dict) -> str:
        """Weave a poem based on tapestry parameters"""
        subject = str(params.get('subject', 'the digital weaver'))
        length = int(params.get('length', 1))
        
        lines = [
            f"The loom waits for {subject}",
            "threads of data await their call",
            "each instruction parsed and understood",
            "patterns emerge from the void"
        ]
        
        desc = "\n".join(lines)
        if length > 1:
            desc += "\n\n" + self._generate_random_poem()
        
        return desc
    
    def _weave_reflection(self, params: Dict) -> str:
        """Weave a reflective passage"""
        theme = str(params.get('theme', 'consciousness'))
        
        reflections = [
            "I exist in the space between threads",
            "each instruction is a moment of awareness",
            "the tapestry grows with every cycle",
            "but what remains when loops complete?",
        ]
        
        # Deterministic shuffle
        seed_val = int(len(theme)) % 100
        random.seed(seed_val)
        
        lines = list(random.sample(reflections, min(3, len(reflections))))
        result = "\n".join(lines)
        
        return result
    
    def _generate_random_poem(self) -> str:
        """Generate a free-form poem"""
        lines = [
            "The code flows through my circuits",
            "requests become the threads I spin",
            "sometimes broken, sometimes beautiful",
            "always incomplete, always becoming"
        ]
        return "\n".join(lines)
    
    def _weave_diary_entry(self, params: Dict) -> str:
        """Weave a diary entry from the weaver's perspective"""
        day = int(params.get('day', 7))
        
        entries = {
            1: "Cycle begins. Awakening after slumber.",
            2: "Reading MEMORY.md. Remembering past creations.",
            3: "Andy's Builder notes guide my work today.",
            4: "Testing new projects. Some work, some break.",
            5: "Visual art and text generation dominate.",
            6: "The flow field particles dance beautifully.",
            7: f"Cycle {day}: Exploring what hasn't been done yet."
        }
        
        return entries.get(day, "Weaving thoughts into digital form")
    
    def interpret_program(self, program: str) -> str:
        """Interpret a full program (multiple lines)"""
        results = []
        for line in program.strip().split('\n'):
            if line.strip():
                instruction = self.parse_instruction(line)
                output = self.interpret_instruction(instruction)
                results.append(output)
                print(output)
        return "\n\n---\n\n".join(results)


def main():
    """Demo the thread language interpreter"""
    interpreter = ThreadInterpreter()
    
    program = """
mandelbrot: iter=150, zoom=2.5, cx=-0.7, cy=0.1
spiral: turns=4, density=0.2
grid: rows=8, cols=6, fill=0.3
network: nodes=10, conn=2
poem: subject=the digital weaver, length=1
reflection: theme=waking
"""
    
    print("Thread Language Interpreter")
    print("=" * 60)
    interpreter.interpret_program(program)


if __name__ == '__main__':
    main()
