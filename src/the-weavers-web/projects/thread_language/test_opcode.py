#!/usr/bin/env python3
from tapestry_grammar import ThreadInterpreter

interp = ThreadInterpreter()

print("Testing each opcode:")
print("=" * 50)

# Test each opcode individually
for line in ["mandelbrot: iter=100, zoom=2.0", 
              "spiral: turns=3, density=0.15",
              "grid: rows=6, cols=4, fill=0.3",
              "network: nodes=6, conn=2",
              "poem: subject=test",
              "reflection: theme=testing",
              "weaver_diary: day=1"]:
    print(f"\n--- {line} ---")
    try:
        result = interp.parse_instruction(line)
        print(f"  Parsed: opcode={result.opcode}, params={result.parameters}")
        
        # This will execute and print the output
        output = interp.interpret_instruction(result)
        print(f"  Output preview: {str(output)[:50]}...")
    except Exception as e:
        print(f"  ERROR: {e}")

print("\nAll opcodes tested.")
