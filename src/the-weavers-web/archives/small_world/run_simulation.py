#!/usr/bin/env python3
"""Run the small world simulation for a demo duration."""

import sys
from world import init_world, run_cycle, get_world_report

def main():
    if len(sys.argv) > 1:
        cycles = int(sys.argv[1])
    else:
        cycles = 50
    
    print(f"Small World Simulation - {cycles} Cycles\n")
    print("=" * 60)
    
    state = init_world()
    
    for cycle in range(cycles):
        state = run_cycle(state)
        
        # Print brief status every 5 cycles
        if (cycle + 1) % 5 == 0 or cycle < 3:
            report = get_world_report(state)
            print(f"\n--- Cycle {cycle + 1} ---")
            for line in report.split("\n"):
                if "inhabitants=" in line.lower() or "total:" in line.lower():
                    print(line)
    
    print(f"\n--- Final State (Cycle {cycles}) ---")
    print(get_world_report(state))

if __name__ == "__main__":
    main()
