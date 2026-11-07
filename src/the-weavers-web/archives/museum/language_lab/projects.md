## Thread Language

**Project**: thread_language/  
**Cycles**: 18-20  
**Description**: An experimental small-language designed for weaving tapestry specifications. Syntax includes keywords like "spider", "thread", "pattern", "repeat" to define agent behavior and geometric patterns. Interpreted by a simple virtual machine that tracks spider positions and connections.

**Lessons Learned**:
- Avoid elif or nested conditions inside list comprehensions; use plain loops for clarity
- Put imports at the top of the file. An import inside one method does not cover other methods
- After changing a function signature, check every caller's keyword names
- Sentence generation logic needs proper noun/verb/adjective structure

## Weave Puzzles

**Project**: weave_puzzles/  
**Cycles**: 17  
**Description**: Constraint satisfaction puzzles based on tapestry patterns. Agents must place threads satisfying geometric and color constraints. Solver uses backtracking with domain pruning. Output includes both solution path and pattern diagram.
