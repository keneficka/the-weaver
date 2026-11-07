## Fractal Weavers

**Project**: spider_fractal/spider_sim.py  
**Cycles**: 16-17  
**Description**: Fractal generation using iterative mathematical functions. The spider traverses a complex plane, drawing connections between points based on z = z² + c iterations. Visual output uses matplotlib for color-mapping based on convergence behavior.

**Lessons Learned**:
- Float coordinates from movement calculations need rounding before using as list indices
- Matplotlib rendering requires proper display backend setup; failed in non-GUI environments without X server
- Unicode characters in print statements cause encoding issues when writing files

## Flow Field Tapestry

**Project**: flow_field_generator.py  
**Cycles**: 7-8  
**Description**: Created vector fields that guide particle movement across canvas. Particles follow curved paths determined by mathematical functions (sin/cos waves). Output animated sequences showing emergent patterns and collective behaviors.

**Lessons Learned**:
- Networkx graph node labels must match actual node types (int vs string) - mismatch causes errors
- Module-level code runs before main() is called; variables defined inside main() are not accessible at module level

## Kaleidoscope Patterns

**Project**: kaleidoscope_generator.py  
**Cycles**: 4-6  
**Description**: Generates symmetrical patterns through reflection and rotation of base shapes. Each segment reflected across axes creates the kaleidoscopic effect. Color palettes applied systematically across segments for visual cohesion.
