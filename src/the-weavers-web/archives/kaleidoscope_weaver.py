#!/usr/bin/env python3
"""
Kaleidoscope Weaver - Symmetric Tapestries from Organic Patterns
Weaving reflection and rotation symmetry into visual tapestries...
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance
import os

class KaleidoscopeWeaver:
    """Main class for weaving kaleidoscopic symmetries"""
    
    def __init__(self, num_symmetries=8, rotation_angle=None):
        """Initialize the weaver with symmetry parameters"""
        self.num_symmetries = num_symmetries
        self.rotation_angle = rotation_angle or (2 * np.pi / num_symmetries)
        self.base_pattern = None
        
    def weave_base_pattern(self, width=800, height=800):
        """Create an organic base pattern"""
        
        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Layer 1: Gradient flow fields
        y_vals = np.arange(height)
        x_vals = np.arange(width)
        Y_grid, X_grid = np.meshgrid(y_vals, x_vals)
        
        angle_phase = (X_grid * 0.05 + Y_grid * 0.03) % np.pi / 2
        
        # Create colorful concentric patterns with angular variation
        base_color_r = np.clip(255 * (1 + np.cos(angle_phase * 4)) / 6, 0, 255)
        base_color_g = np.clip(255 * (1 + np.sin(angle_phase * 3)) / 4, 0, 255)
        base_color_b = np.clip(255 * (1 + np.cos(angle_phase * 5)) / 8, 0, 255)
        
        # Add texture with noise and gradients
        noise = np.random.rand(height, width) * 40
        canvas[:, :, 0] = base_color_r.astype(np.uint8) + noise.astype(np.float32) * 30
        canvas[:, :, 1] = base_color_g.astype(np.uint8) + noise.astype(np.float32) * 20
        canvas[:, :, 2] = base_color_b.astype(np.uint8) + noise.astype(np.float32) * 15
        
        self.base_pattern = canvas
    
    def weave_symmetry(self, pattern):
        """Apply kaleidoscopic symmetry to a pattern using simpler method"""
        
        height, width, channels = pattern.shape
        center_x = width / 2.0
        center_y = height / 2.0
        
        symmetric_pattern = np.zeros((height, width, 3), dtype=np.uint8)
        
        for i in range(self.num_symmetries):
            start_angle = i * self.rotation_angle
            end_angle = (i + 1) * self.rotation_angle
            
            Y_grid = np.arange(height)[:, None]
            X_grid = np.arange(width)[None, :]
            
            angles = np.arctan2(Y_grid - center_y, X_grid - center_x)
            
            # Normalize angles to [0, 2*pi) and create sector masks
            angles_norm = (angles + 2 * np.pi) / (2 * np.pi)
            
            mask_sector = (angles_norm >= i) & (angles_norm < i + 1)
            
            if mask_sector.any():
                symmetric_pattern[mask_sector] = pattern[mask_sector]
        
        return symmetric_pattern
    
    def weave_artistic_composition(self, filename=None):
        """Create a complete kaleidoscopic artwork"""
        
        print("Kaleidoscope Weaver - Symmetric Tapestries")
        print("=" * 50)
        
        # Create base organic pattern
        self.weave_base_pattern(width=800, height=800)
        
        if self.base_pattern is None:
            print("Error: Failed to weave base pattern")
            return None
        
        print("Base organic pattern woven...")
        
        # Apply kaleidoscopic symmetry multiple times for layering
        num_layers = 5
        layers = [self.base_pattern]
        
        for layer_idx in range(num_layers):
            shifted_pattern = self.base_pattern.copy()
            shift_amount = 2 + layer_idx
            
            h, w, _ = shifted_pattern.shape
            shifted_pattern[:, :shift_amount] = shifted_pattern[:, -shift_amount:].copy()
            shifted_pattern[-shift_amount:, :] = shifted_pattern[:shift_amount, :].copy()
            
            layers.append(self.weave_symmetry(shifted_pattern))
        
        # Blend the layers together
        blended = np.zeros((layers[0].shape[0], layers[0].shape[1], 3), dtype=np.uint8)
        
        for layer in layers:
            max_val = np.max(layer)
            if max_val > 0:
                weighted_layer = (layer / max_val) * (255.0 / num_layers)
            else:
                weighted_layer = layer / 255.0 * (255.0 / num_layers)
            blended = np.minimum(255, blended + weighted_layer.astype(np.uint8))
        
        # Apply artistic adjustments
        enhancement = ImageEnhance.Contrast(Image.fromarray(blended))
        blended = np.array(enhancement.enhance(1.3), dtype=np.float32)
        
        output_path = os.path.join(os.path.dirname(__file__), 'output')
        os.makedirs(output_path, exist_ok=True)
        
        if filename:
            save_path = os.path.join(output_path, filename)
        else:
            save_path = os.path.join(output_path, 'kaleidoscope_tapestry.png')
        
        plt.figure(figsize=(10, 8))
        plt.imshow(np.clip(blended, 0, 255).astype(np.uint8))
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"Kaleidoscopic tapestry woven into {save_path}")
        return save_path


def main():
    """Weave a kaleidoscopic artwork"""
    
    weaver = KaleidoscopeWeaver(num_symmetries=8)
    
    # Create the first composition
    output_file = 'kaleidoscope_symmetry_01.png'
    weaver.weave_artistic_composition(filename=output_file)


if __name__ == '__main__':
    main()
