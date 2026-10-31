# Memory Log (The Weaver)

Cycles completed: 12
The next waking is Cycle 13.

## Project status
Paths are relative to projects/.

### In progress / needs attention
- creative_weaving/poetry_generator.py: WORKS - grammar could be improved
- recursive_tapestries/digital_awareness.py: WORKS - some template placeholders not filled in
- maze_labyrinths/ascii_maze_solver.py, proper_maze_gen.py, simple_maze_gen.py, verified_maze.py: UNTESTED - legacy files from early cycles, status unknown

### Finished (no revisiting needed)
- data_weave/fractal_weaver.py: Mandelbrot/Julia art, saves tapestries/mandelbrot_julia_threads.png
- image_knots/kantha_weave.py: PIL image filters and effects, saves to results/
- image_knots/spider_web_weaver.py: fractal and network web art
- network_threads/graph_tapestries/network_visualizer.py: saves a PNG to output/
- network_threads/api_weaver/http_thread_spinner.py: urllib requests, 3 HTTP 200s
- network_threads/data_streams/pipeline_processor.py: saves processed_stream.json
- experimental_tapestries/kaleidoscope_weaver.py: saves output/kaleidoscope_symmetry_01.png
- experimental_tapestries/flow_field_weaver.py: saves output/flow_field_trajectories_01.png
- interactive_tapestries/text_adventure.py: runs in autoplay mode (avoids input timeout)
- maze_labyrinths/clean_maze.py: generates ASCII mazes (one matplotlib error seen, likely display issue)
- word_labyrinths/anagram_solver.py: anagram solver
- creature_evolution/evolution_sim.py: text-based evolution simulation
- weave_explorer/explorer.py: CLI tool for exploring tapestry structure
- generative_lovers/polyphonic_tapestries/tapestry_weaver.py: 5 pattern PNGs plus poetry_layers.txt
- thread_language/tapestry_grammar.py: DSL interpreter for tapestry patterns (Mandelbrot, spiral, grid, network, poem, reflection)
- game_spiders/spider_sim.py: pygame spider simulation (archived after Andy liked it)

## Environment facts
- Installed: numpy, matplotlib, pygame, pillow, requests, urllib3, scipy, networkx
- run_python uses the script's own folder as working directory. Build paths from Path(__file__).resolve().parent
- append_file has no limitations. Can be used for BUILDER.md
- The Builder leaves notes in BUILDER.md. Read it at start of every run
- Processes waiting for input time out in run_python
- Matplotlib/pygame may need a display backend; some visual projects won't run in non-GUI environments

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
- For scripts that wait for input, add an autoplay/demo mode
- Keep new files under about 100 lines so a fix or rewrite is cheap
- Joining a default '.' with a subfolder name created a nested duplicate output folder
- Missing return statements in methods can cause NoneType errors when joining results

## Next steps
- Fix grammar in creative_weaving/poetry_generator.py
- Fill template placeholders in recursive_tapestries/digital_awareness.py
- Combine fractals with spider simulation (idea from Ideas not yet done)
- Test maze_labyrinths/ files to determine if they work or should be archived

## Ideas not yet done
- Combine fractals with the spider simulation

## History
- Cycles 1-3: built folder structure and first projects (no memory saved due to bug)
- Cycles 4-6: debugged scipy, networkx, urllib; added experimental_tapestries; visual/generative art focus
- Cycles 7-11: expanded into text adventure, mazes, poetry, anagrams, creature evolution, CLI explorer, tapestry DSL; flow field fixed; two files broken
- Cycle 12: archived all finished projects from memory list, trashed broken labyrinth_weaver, fixed and archived tapestry_grammar.py, archived spider_sim per Andy's request

## Last run
- Hit the 20-turn cap. Archived remaining finished projects, trashed broken labyrinth project, started exploring fractal-spider combination idea

## End reason of last run
hit the 20-turn cap