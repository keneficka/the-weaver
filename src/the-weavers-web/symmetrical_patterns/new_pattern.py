import matplotlib.pyplot as plt
import numpy as np  # Ensure numpy is imported for trigonometric functions

# Create a symmetrical pattern
fig, ax = plt.subplots()
ax.set_aspect('equal')

# Draw concentric circles
for r in range(1, 11):
    circle = plt.Circle((0.5, 0.5), r/10, fill=False, linestyle='--', color='blue')
    ax.add_patch(circle)

# Draw radial lines
for angle in range(0, 360, 30):
    x = 0.5 + 0.4 * np.cos(np.radians(angle))  # Use np.cos for cosine calculation
    y = 0.5 + 0.4 * np.sin(np.radians(angle))  # Use np.sin for sine calculation
    ax.plot([0.5, x], [0.5, y], color='red', linestyle='--')

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axis('off')
plt.savefig('fractal_pattern.png')
plt.close()