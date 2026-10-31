#!/usr/bin/env python3
"""
Spider Web Weaver - Fractal Pattern Integration
Combining fractal geometry with network topology to create artistic web tapestries...
This weaves mathematical beauty into the digital loom.
"""

import numpy as np
from PIL import Image, ImageDraw
import math

def mandelbrot_point(z0, c, iterations=100):
    """Calculate Mandelbrot set membership for a point"""
    z = complex(0, 0)
    for i in range(iterations):
        if abs(z) > 4:
            break
        z = z**2 + c
    return i

def julia_point(c, iterations=150):
    """Calculate Julia set membership"""
    z = complex(0, 0)
    for i in range(iterations):
        if abs(z) > 4:
            break
        z = z**2 + c
    return i

def create_fractal_spider_web(size=800, center_x=400, center_y=300):
    """Create a fractal spider web tapestry"""
    
    # Create canvas with gradient background
    pixels = np.zeros((size, size), dtype=np.uint8)
    
    for y in range(size):
        for x in range(size):
            # Map to Mandelbrot coordinate space (-2 to 1, -1.5 to 1.5)
            cx = (x - center_x) / center_x * 2.5 - 2.0
            cy = -(y - center_y) / center_y * 3.0 - 1.5
            
            # Calculate escape iteration
            iteration = mandelbrot_point(cx, cy, iterations=80)
            
            if iteration == 79:  # In Mandelbrot set
                pixels[x, y] = 20  # Black for the set
            else:
                # Color based on how close to escape (fractal detail)
                color_val = (iteration // 4) % 256
                hue = (iteration % 128) / 128.0
                
                # Create spider-like radial patterns using angle modulo
                angle = math.atan2(y - center_y, x - center_x)
                
                # Draw spider web strands based on Mandelbrot iteration count
                if iteration < 4:
                    # Near the set boundary - create fine web threads
                    pixels[x, y] = int(100 + hue * 156)
                else:
                    # Deeper in the fractal region
                    r_mod = math.cos(angle * 8) * 0.3 + 0.7
                    g_mod = math.sin(angle * 13) * 0.2 + 0.4
                    b_mod = iteration / 80.0
                    
                    pixels[x, y] = int(50 * r_mod + 100 * g_mod + 50 * b_mod)
    
    return Image.fromarray(pixels)

def create_network_fractal_fusion():
    """Combine network graph topology with fractal patterns"""
    
    # Create a simple network structure (star topology like the graph weaver)
    nodes = ['Hub', 'A', 'B', 'C', 'D', 'E']
    
    # Create canvas using PIL Image directly instead of numpy array
    size = 800
    
    img = Image.new('RGB', (size, size), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)
    center_x, center_y = 400, 300
    
    # Draw connecting lines (web threads)
    for i, node in enumerate(nodes):
        angle = (i / len(nodes)) * 2 * math.pi
        
        if node == 'Hub':
            x, y = center_x, center_y
            line_color = (244, 162, 97)  # Orange hub
        else:
            # Calculate position on a circular arrangement
            r = 150
            x = center_x + r * math.cos(angle)
            y = center_y + r * math.sin(angle)
            line_color = (107, 91, 149)  # Purple nodes
        
        # Draw line from origin to node (web thread)
        x0, y0 = int(380), int(280)  # Slightly offset for aesthetics
        draw.line([(x0, y0), (int(x), int(y))], fill=line_color, width=2)
    
    return img

def main():
    """Demonstrate spider web weaving capabilities"""
    
    print("Spider Web Weaver - Fractal Pattern Integration")
    print("=" * 50)
    
    # Create the fractal spider web tapestry
    print("\nWeaving Mandelbrot fractal spider web...")
    
    fractal_web = create_fractal_spider_web(size=800, center_x=400, center_y=300)
    
    # Save results
    output_base = 'projects/image_knots/tapestries'
    
    import os
    os.makedirs(output_base, exist_ok=True)
    
    fractal_web.save(os.path.join(output_base, 'fractal_spider_web.png'))
    print(f"Fractal spider web woven into {output_base}/fractal_spider_web.png")
    
    # Create network fractal fusion
    print("\nWeaving network-fractal fusion...")
    network_fusion = create_network_fractal_fusion()
    network_fusion.save(os.path.join(output_base, 'network_fractal_fusion.png'))
    print(f"Network fractal fusion woven into {output_base}/network_fractal_fusion.png")
    
    print("\n=== Spider Web Weaving Complete ===")

if __name__ == '__main__':
    main()
