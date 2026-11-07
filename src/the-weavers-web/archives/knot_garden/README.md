# Knot Garden

A strategy puzzle game about weaving threads through garden plots.

## The Game

You are a gardener tasked with tending to knot-pattern gardens. Each garden plot starts with scattered thread segments that must be woven together into beautiful floral arrangements.

### Basic Mechanics

- **Strands**: Thread segments of various lengths and colors
- **Operations**: Connect strands at endpoints, form loops, trim excess
- **Goal Patterns**: Target configurations marked by flower motifs
- **Trap Knots**: Misshapen patterns that cause the garden to wither (game over)

### Scoring

- +5 points for each completed goal pattern
- -2 points per strand left unused
- -10 points if a trap knot is formed
- Bonus for achieving patterns in minimum moves

## Files

- `main.py` - Game engine and play loop
- `patterns.json` - Goal pattern definitions
- `traps.json` - Forbidden configuration data
