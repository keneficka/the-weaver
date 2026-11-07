# Thread Rituals

A digital tapestry ritual simulation where threads perform ceremonies that build complexity and patterns over time.

## Overview

This is a generative tapestry system where individual threads of different colors (gold, silver, indigo, crimson, ebony) can perform various rituals based on their properties and state. Each thread has unique rituals it can perform:

### Thread Rituals by Type:
- **Gold**: warp, weft, gild - loom-based weaving
- **Silver**: warp, weft, polish - brightening rituals  
- **Indigo**: twist, wind, dye - fluid transformations
- **Crimson**: bind, seal, bleed - binding/bonding operations
- **Ebony**: anchor, shadow, darken - grounding effects

### Ritual Outcomes:
Each ritual has probabilistic outcomes:
- Successful transformation (creates new states)
- Breakage (thread snaps when damaged)
- Normal completion

## Running the Simulation

### Quick Demo (no persistence):
```bash
python projects/thread_rituals/main.py
```

### With State Persistence:
The simulation saves state to `weave_state.json` after each run. To continue from where you left off:

1. Run main.py which will load existing state automatically
2. Or run demo.py for a fresh demo cycle

### Demo Mode:
```bash
python projects/thread_rituals/demo.py
```
Runs 15 cycles automatically and saves render artifacts to `artifacts/` folder.

## Files

- `main.py` - Core simulation engine with state persistence
- `demo.py` - Auto-runner for demo mode
- `README.md` - This documentation
- `artifacts/` - Contains:
  - `ritual_log.txt` - Full ritual log from last run
  - `weave_state.json` - Saved weave state for next cycle
  - `weave_render.png` - Rendered tapestry image

## Persistence

The simulation saves its state between runs using `weave_state.json`. This allows:
- Continuing the same weave across multiple cycles
- Observing pattern evolution over time
- Building long-term emergent behaviors

Load automatically on each run unless state file doesn't exist (fresh start).

## Patterns Detected

The system analyzes for emerging patterns every 5 cycles:
- **symmetry_np** - Balanced pairs of colors forming symmetries
- **high_tension_cluster** - Concentrated tension regions
- **relaxed_region** - Areas of low tension/relaxation

## Notes from the Weaver

This simulation explores the dynamics of ritual performance and pattern emergence. Threads agitate with each cycle, performing their appropriate rituals based on current state. Some threads break and fade away; others build up new structures through successful rituals. Over many cycles, this can produce tapestries that tell stories of creation, destruction, transformation, and balance.

The weave is never finished - it continues to evolve with each run. Consider starting a new cycle when you wish to see what patterns emerge over different random seeds and thread compositions.
