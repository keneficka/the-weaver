#!/usr/bin/env python3
"""
Fractal Weaver - Corrected Version
Spinning mathematical tapestries into the void...
"""

import numpy as np
import matplotlib.pyplot as plt
import os

def generate_mandelbrot_set(max_iteration=128):
    """Spin a Mandelbrot fractal thread"""
    
    x_min, x_max = -2.5, 1.0
    y_min, y_max = -1.2, 1.2
    width, height = 600, 400
    
    # Create grid properly
    X, Y = np.meshgrid(
        np.linspace(x_min, x_max, width),
        np.linspace(y_min, y_max, height)
    )
    
    C = X + 1j * Y
    Z = np.zeros_like(C, dtype=complex)
    
    for i in range(max_iteration):
        Z = Z**2 + C
        active_mask = np.abs(Z) < 2.0
    
    return ~active_mask

def create_julia_fractal(c, max_iteration=128):
    """Spin a Julia set thread"""
    
    x_min, x_max = -1.5, 1.5
    y_min, y_max = -1.5, 1.5
    width, height = 600, 400
    
    X, Y = np.meshgrid(
        np.linspace(x_min, x_max, width),
        np.linspace(y_min, y_max, height)
    )
    
    Z = X + 1j * Y
    
    for i in range(max_iteration):
        Z = Z**2 + c
        active_mask = np.abs(Z) < 2.0
    
    return ~active_mask

def main():
    print("Weaving Mandelbrot fractal threads into the tapestry...")
    mandelbrot = generate_mandelbrot_set(max_iteration=128)
    
    print("Spinning Julia set patterns...")
    julia_params = [(-0.7 + 0.27j), (-0.8 + 0.156j), (-1.4 + 0j)]
    julia_patterns = []
    
    for c in julia_params:
        pattern = create_julia_fractal(c=c, max_iteration=128)
        julia_patterns.append(pattern)
    
    # Get absolute path of script and construct output path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_web_root = os.path.dirname(os.path.dirname(script_dir))  # Go up to web root
    
    output_path = os.path.join(base_web_root, 'projects', 'data_weave', 'tapestries', 'mandelbrot_julia_threads.png')
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    axes[0].imshow(mandelbrot, cmap='viridis')
    axes[0].set_title("Mandelbrot Set - Primary Thread")
    axes[0].axis('off')
    
    for i, ax in enumerate(axes[1:]):
        ax.imshow(julia_patterns[i], cmap='plasma')
        ax.set_title(f"Julia Set Pattern {i+1}")
        ax.axis('off')
    
    plt.tight_layout()
    
    plt.savefig(output_path, dpi=150)
    plt.close()
    
    print(f"Fractal tapestries woven into {output_path}")

if __name__ == '__main__':
    main()
