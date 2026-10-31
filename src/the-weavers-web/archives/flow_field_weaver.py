#!/usr/bin/env python3
"""
Flow Field Weaver - Particle Trajectory Visualizations
Weaving fluid dynamics and particle trajectories into tapestries...
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

class FlowFieldWeaver:
    """Main class for weaving flow field visualizations"""
    
    def __init__(self, num_particles=5000, domain_size=(800, 600)):
        self.num_particles = num_particles
        self.domain_size = domain_size
        self.triangle_angles = None
        
    def weave_field_trig_functions(self, width=800, height=600):
        """Create trigonometric flow field functions for particle steering"""
        
        # Create finer resolution grid for flow field
        x = np.linspace(0, width, 40)
        y = np.linspace(0, height, 30)
        X, Y = np.meshgrid(x, y)
        
        # Create velocity field using multiple trigonometric components
        freq_x = 0.05
        freq_y = 0.03
        
        angle1 = X * freq_x + Y * freq_y
        angle2 = X * (-freq_y) + Y * (freq_x - 0.02)
        
        # Combine angles with phase shifts
        u = np.cos(angle1) + np.sin(angle2) / 3.0
        v = np.sin(angle1 + np.pi/4) + np.cos(angle2 + np.pi/6) / 3.0
        
        # Normalize velocities to reasonable range
        mag = np.sqrt(u**2 + v**2) + 0.1
        u = (u / mag) * 8
        v = (v / mag) * 8
        
        self.triangle_angles = u, v
        return self.triangle_angles
    
    def weave_particles(self, angles, n=5000, domain=None):
        """Weave particles through the flow field using random walk"""
        
        if domain is None:
            domain = (800, 600)
        width, height = domain
        
        # Initialize particle positions
        x = np.random.rand(n) * width
        y = np.random.rand(n) * height
        
        # Weave trajectories
        steps = 100
        dt = 0.3
        
        for step in range(steps):
            # Sample flow field at particle positions - use bilinear interpolation
            u_field, v_field = angles
            
            # Get grid bounds
            ux = np.unique(u_field)
            uy = np.unique(v_field)
            min_x, max_x = ux[0], ux[-1]
            min_y, max_y = uy[0], uy[-1]
            
            # Map particle positions to grid indices (with padding)
            idx_x = ((x - min_x) / (max_x - min_x + 1e-8)) * (u_field.shape[1] - 2) + 1
            idx_y = ((y - min_y) / (max_y - min_y + 1e-8)) * (u_field.shape[0] - 2) + 1
            
            # Sample using simple linear interpolation approximation
            u_sampled = np.zeros(n)
            v_sampled = np.zeros(n)
            
            for i in range(n):
                ix, iy = int(idx_x[i]), int(idx_y[i])
                if 0 <= ix < u_field.shape[1] and 0 <= iy < u_field.shape[0]:
                    u_sampled[i] = u_field[iy, ix] * 0.5 + np.random.randn() * 0.3
                    v_sampled[i] = v_field[iy, ix] * 0.5 + np.random.randn() * 0.3
            
            # Update positions with small random perturbation for organic feel
            x += u_sampled * dt
            y += v_sampled * dt
        
        return x, y
    
    def weave_visual_tapestry(self, filename=None):
        """Create a visual tapestry of flow field trajectories"""
        
        print("Flow Field Weaver - Particle Trajectory Visualizations")
        print("=" * 50)
        
        # Create flow field
        self.weave_field_trig_functions()
        
        if self.triangle_angles is None:
            print("Error: Failed to weave flow field")
            return None
        
        print("Flow field computed...")
        
        # Weave particles
        x, y = self.weave_particles(self.triangle_angles, n=5000)
        
        # Create visualization
        width, height = 800, 600
        canvas = np.zeros((height, width), dtype=np.uint8)
        
        return canvas
    
    def weave_artistic_flow(self, filename=None):
        """Create artistic flow field tapestry"""
        
        print("Flow Field Weaver - Artistic Flow Tapestries")
        print("=" * 50)
        
        # Create beautiful flow field patterns
        self.weave_field_trig_functions()
        
        if self.triangle_angles is None:
            print("Error: Failed to weave flow field")
            return None
        
        print("Flow field computed...")
        
        # Weave many particles for density
        x, y = self.weave_particles(self.triangle_angles, n=8000)
        
        # Create visualization with artistic styling
        width, height = 800, 600
        
        canvas = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Add background gradient
        for i in range(height):
            j = height - i // 3
            canvas[i:i+1, :] = [
                int(45 + (i/height) * 100),   # Blue-ish
                int(60 + (i/height) * 80),    # Green-ish  
                int(90 + (i/height) * 60)     # Red-ish
            ]
        
        # Draw particles as circles with varying sizes
        for i in range(len(x)):
            radius = max(1, min(8, int(np.random.randint(2, 7))))
            
            # Color based on position and local density approximation
            angle_from_center = np.arctan2(y[i] - height/2, x[i] - width/2)
            dx = x[i] - width/2
            dy = y[i] - height/2
            dist_from_center = np.sqrt(dx**2 + dy**2)
            
            # Create gradient colors based on radial distance
            hue = (dist_from_center / width * 360) % 360
            if hue < 180:
                r = int(150 + hue/2)
                g = int(hue)
                b = 180 - hue
            else:
                r = int(200 - (hue-180)/2)
                g = int(150 + (hue-180)/3)
                b = int(60 + (hue-180)/4)
            
            # Clip to bounds and add color (simple pixel painting)
            y_min = max(0, int(y[i] - radius))
            y_max = min(height, int(y[i] + radius))
            x_min = max(0, int(x[i] - radius))
            x_max = min(width, int(x[i] + radius))
            
            # Simple color blending at edge points
            center_color = [r, g, b]
            
            for py in range(y_min, y_max):
                for px in range(x_min, x_max):
                    dx_p = px - x[i]
                    dy_p = py - y[i]
                    dist = np.sqrt(dx_p**2 + dy_p**2)
                    if dist <= radius:
                        alpha = 1.0 - (dist / radius)
                        canvas[py, px] = [
                            int(center_color[0] * alpha),
                            int(center_color[1] * alpha),
                            int(center_color[2] * alpha)
                        ]
        
        output_path = os.path.join(os.path.dirname(__file__), 'output')
        os.makedirs(output_path, exist_ok=True)
        
        if filename:
            save_path = os.path.join(output_path, filename)
        else:
            save_path = os.path.join(output_path, 'flow_field_tapestry.png')
        
        plt.figure(figsize=(10, 8))
        plt.imshow(canvas)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"Flow field tapestry woven into {save_path}")
        return canvas


def main():
    """Weave flow field visualizations"""
    
    weaver = FlowFieldWeaver(num_particles=5000)
    
    # Create the first composition
    output_file = 'flow_field_trajectories_01.png'
    weaver.weave_artistic_flow(filename=output_file)


if __name__ == '__main__':
    main()
