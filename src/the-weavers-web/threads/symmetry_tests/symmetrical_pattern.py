import math

def generate_symmetrical_pattern(radius, num_points, symmetry_axis):
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
    return points

# Example usage:
if __name__ == '__main__':
    pattern = generate_symmetrical_pattern(10, 12, 'y')
    print("Symmetrical Points:")
    for point in pattern:
        print(point)