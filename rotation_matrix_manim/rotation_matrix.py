import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axes
fig, ax = plt.subplots()

# Define vector coordinates
x = [0, 2]
y = [0, 1]

# Plot the vector
ax.quiver(x[0], y[0], x[1]-x[0], y[1]-y[0], angles='xy', scale_units='xy', scale=1)

# Set axis limits and labels
ax.set_xlim([-1, 3])
ax.set_ylim([-1, 2])
ax.set_xlabel('x')
ax.set_ylabel('y')

# Add annotations
ax.annotate('a', (1, 0.5), fontsize=12)
ax.annotate('b', (1.5, 1.2), fontsize=12)

# Show the plot
plt.grid(True)
plt.show()