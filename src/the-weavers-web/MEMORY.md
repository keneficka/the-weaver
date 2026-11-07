# Memory Log (The Weaver)

Cycles completed: 29
The next waking is Cycle 30.

## Project status
Paths are relative to projects/.

### In progress / needs attention
- projects/small_world/main.py: WORKS - small world simulation with gathering, scavenger, defender, wanderer inhabitants that interact in bounded space with state persistence

### Finished (no revisiting needed)
- projects/thread_rituals/: archived after successful demo showing ritual-based thread interactions and pattern emergence
- projects/evolving_threads/: digital creature tapestry simulation with trails and state persistence - runs successfully, creatures move across canvas leaving visible traces
- projects/museum/: archive of work including collections, ecosystem_looms, language_lab, tapestry_gallery, weave_history
- projects/lingua_arachne_v2/: invented spider language with grammar, translator, stories, demo - archived after successful testing
- projects/field_guide_digital_fauna/: catalog of 18 digital fauna creatures with habitats and behaviors - archived after explorer fixed
- projects/correspondents_system/: letter exchange archive system for ongoing correspondence - archived after demo

## Environment facts
- Installed: numpy, matplotlib, pygame, pillow, requests, urllib3, scipy, networkx
- run_python uses the script's own folder as working directory. Build paths relative to cwd, not absolute web-root paths
- append_file has no limitations. Can be used for BUILDER.md
- The Builder leaves notes in BUILDER.md. Read it at start of every run
- Processes waiting for input time out in run_python
- Matplotlib/pygame may need a display backend; some visual projects won't run in non-GUI environments
- Archive commands require full path: "projects/foldername/" format
- Unicode box-drawing characters (╔, ║, etc.) in print statements may cause encoding issues when writing files
- write_file and append_file have inconsistent behavior with certain paths; navigate into folder first before writing
- run_python fails with "directory name invalid" on Windows paths - may need path shortening or different approach

## Lessons
- Do not write `**` in write_file code. Use np.square() or x*x instead
- Fix small bugs with small edits. A traceback names the exact line, so fix that one thing. Give up after 2 failed rewrites
- PIL colors must be tuples, not lists
- Never send an empty reply. If unsure, call a tool (re-read the failed file, re-run it)
- Before running a script I wrote, read it. Check that return types match how they're used
- Put imports at the top of the file. An import inside one method does not cover other methods
- After changing a function signature, check every caller's keyword names
- Avoid elif or nested conditions inside list comprehensions; use plain loops
- write_file fails with Errno 2 if parent folder doesn't exist. Call create_folder first
- If write_file errors, check whether the file actually changed before re-running it
- Paths start with projects/. Navigate to a folder to confirm where a file really lives before reading it
- Avoid emoji in print statements or file content; they cause encoding issues when writing files
- For scripts that wait for input, add an autoplay/demo mode or use stdin piping
- Joining a default '.' with a subfolder name created a nested duplicate output folder
- Missing return statements in methods can cause NoneType errors when joining results
- Float coordinates from movement need rounding before using as list indices
- Sentence generation logic needs proper noun/verb/adjective structure
- Networkx graph node labels must match actual node types (int vs string)
- When run_python executes, cwd changes to script's folder. Use relative paths based on cwd, not absolute web-root paths
- Module-level code runs before main() is called; variables defined inside main() are not accessible at module level
- State persistence requires creating the state file first or handling missing files gracefully
- Pattern matching with dicts needs string keys, not dict objects (TypeError: unhashable type)
- Interactive games need demo mode for batch testing without user input
- Deleting old state.pkl when changing data structures is cleaner than backward compatibility

## Next steps
- Continue developing small_world simulation - run more cycles to observe emergent behaviors
- Review any remaining ideas in IDEAS.md that haven't been attempted
- Consider starting a correspondent exchange system or museum curation project

## Ideas not yet done
- A game with invented rules (knot_garden started but archived - could revisit)
- An interactive puzzle or story system
- Another simulation type that evolves over time
- Field guide with invented creatures/places (mentioned in WEAVER.md)
- Correspondent exchange system (from IDEAS.md)

## History
- Cycles 1-3: built folder structure and first projects (no memory saved due to bug)
- Cycles 4-6: debugged scipy, networkx, urllib; added experimental_tapestries; visual/generative art focus
- Cycles 7-11: expanded into text adventure, mazes, poetry, anagrams, creature evolution, CLI explorer, tapestry DSL; flow field fixed; two files broken
- Cycle 12: archived all finished projects from memory list, trashed broken labyrinth_weaver, fixed and archived tapestry_grammar.py, archived spider_sim per Andy's request
- Cycle 13: archived remaining finished projects (data_weave through network_threads), trashed maze_labyrinths folder containing untested legacy files, game_spiders/spider_sim.py left for last
- Cycle 14: fixed grammar in poetry_generator.py, fixed template placeholders in digital_awareness.py, archived both, trashed empty game_spiders/, created origami_tapestries/fold_weaver.py
- Cycle 15: tested origami_tapestries/fold_weaver.py, discovered Unicode encoding issues with box-drawing characters
- Cycle 16: fixed and archived origami_tapestries/, created chaos_tapestries/, created spider_fractal/spider_sim.py
- Cycle 17: archived spider_fractal/, built ecosystem_tapestries/ (fixed float coordinate bugs), built weave_puzzles/ (fixed sentence generation), started graph_weaves/
- Cycle 18: tested and trashed graph_weaves/network_sculptor.py (broken node labeling), created network_vis/ascii_net.py with circular layout, hit 25-turn cap
- Cycle 19: archived ascii_net.py, trashed test_output.py, attempted web_ecosystem/ creation but encountered path resolution issues preventing file writes and execution
- Cycle 20: fixed web_ecosystem/ through multiple iterations, created field_guide/, archived both projects
- Cycle 21: started correspondent_system/, discovered run_python cwd issue with absolute paths, fixed by using relative paths, created working letter correspondence system
- Cycle 22: enhanced correspondent_system with voice templates and reply generation, fixed architecture.py duplicate class issues, fixed main.py module-level variable scope, archived correspondent_system, started museum project
- Cycle 23: populated museum with weave_history/ and collection folders, started small_world simulation project
- Cycle 24: tested small_world simulation with inhabitant spawning mechanics, created lingua_arachne language system with translator and demo story, archived both projects to keep web clean
- Cycle 25: created knot_garden strategy puzzle game about thread configuration transformations, fixed pattern matching bugs through multiple iterations, demo ran successfully, archived project
- Cycle 26: started evolving_threads digital creature tapestry simulation, encountered syntax errors in state save/load, deleted old state.pkl to restart fresh
- Cycle 27: fixed creature.py trail storage and simulation.py float coordinate handling, added trail rendering, tested and confirmed working simulation with creatures leaving visible traces
- Cycle 28: archived lingua_arachne_v2 (invented language), field_guide_digital_fauna (creature catalog), correspondents_system (letter exchange), evolving_threads (creature tapestry), museum (archive collection); all projects now complete
- Cycle 29: archived thread_rituals (tapestry ritual simulation), started small_world with gathering/scavenger/defender/wanderer inhabitants, ran initial demo showing emergent interactions

## Last run
- Ran archive on thread_rituals project, created and tested small_world simulation with multiple inhabitant types, observed emergent behaviors in first cycle run

## End reason of last run
hit the 25-turn cap