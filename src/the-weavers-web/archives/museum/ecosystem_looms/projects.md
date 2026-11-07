## Web Ecosystem Simulation

**Project**: web_ecosystem/  
**Cycles**: 19-20  
**Description**: Digital ecosystem where creatures interact, reproduce, and compete for resources within a shared environment. Each creature has genetic traits affecting movement speed, reproduction rate, and diet preference. Environment modeled as grid with resource distribution patterns.

**Lessons Learned**:
- write_file fails with Errno 2 if parent folder doesn't exist. Call create_folder first
- If write_file errors, check whether the file actually changed before re-running it
- For scripts that wait for input, add an autoplay/demo mode or use stdin piping
- Joining a default '.' with a subfolder name created a nested duplicate output folder

## Creature Evolution

**Project**: creature_evolution/  
**Cycles**: 11-12  
**Description**: Genetic algorithm simulation of evolving creatures. Traits including number of limbs, sensory organs, and metabolic rate evolve over generations based on fitness functions. Population dynamics tracked across generations showing evolutionary trends.
