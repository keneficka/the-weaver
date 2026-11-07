# Evolving Threads

A simulation of digital creatures living in a shared tapestry space. Each creature:
- Spins patterns based on its own "temperament" 
- Interacts with neighbors (attract, repel, or ignore)
- Leaves traces that influence the environment
- Can evolve new behaviors over time

The world is an 80x25 character canvas where creatures navigate by moving,
drawing threads, and reacting to their surroundings. Over time, the tapestry
emerges from countless simple interactions.

## File Structure
- creature.py: Individual creature behavior and state
- simulation.py: Main loop, rendering, and persistence
- patterns.md: Pattern definitions that creatures can "learn" and use

Start by running simulation.py to see threads form and dance across the loom.
