import math

def plot_symmetrical_pattern(radius, num_points, symmetry_axis):
    angles = [2 * math.pi * i / num_points for i in range(num_points)]
    points = []
    for angle in angles:
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        # Reflect across symmetry_axis to maintain balance
        if symmetry_axis == 'x':
            x *= -1
        elif symmetry_axis == 'y':
            y *= -1
        points.append((x, y))
    
    # Convert to grid coordinates for visualization
    grid_size = 20
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    scale = (grid_size - 1) / (2 * radius)  # Adjust scale to prevent out-of-range indices
    
    for x, y in points:
        # Clamp values to grid bounds
        grid_y = int(y * scale + grid_size / 2)
        grid_x = int(x * scale + grid_size / 2)
        if 0 <= grid_y < grid_size and 0 <= grid_x < grid_size:
            grid[grid_y][grid_x] = 1
    
    # Print grid
    for row in grid:
        print(''.join(['#' if cell else '.' for cell in row]))

# Example usage:
if __name__ == '__main__':
    plot_symmetrical_pattern(10, 12, 'y')