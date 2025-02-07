# Let's create a plot similar to the one provided in the uploaded image using Matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# Data for the plot
std_dev = [0.06, 0.12, 0.18]  # Standard deviations (x-axis)
expected_return = [0.06, 0.08, 0.10]  # Expected returns (y-axis)
labels = ['C', 'B', 'D']  # Labels for the points

# Linear line (Capital Market Line)
slope = (expected_return[-1] - 0.04) / (std_dev[-1])  # Slope of the line
intercept = 0.04  # Risk-free rate (y-intercept)
line_x = np.linspace(0, 0.2, 100)
line_y = slope * line_x + intercept

# Initialize the plot
plt.figure(figsize=(8, 6))

# Plot the line
plt.plot(line_x, line_y, linestyle='--', color='black', linewidth=1)

# Plot the points
plt.scatter([0] + std_dev, [0.04] + expected_return, color='black', zorder=5)
plt.text(0.002, 0.041, 'A', fontsize=12, ha='center', va='bottom', fontweight='bold')

# Add labels to points
for i, (x, y) in enumerate(zip(std_dev, expected_return)):
    plt.text(x, y + 0.002, labels[i], fontsize=12, ha='center', va='bottom', fontweight='bold')

# Customize axes
plt.xticks([0.06, 0.12, 0.18], ['.06', '.12', '.18'], fontsize=12)
plt.yticks([0.04, 0.06, 0.08, 0.10], ['4%', '6%', '8%', '10%'], fontsize=12)
plt.xlabel(r'$\sigma_p$', fontsize=16, fontweight='bold')
plt.ylabel(r'$E[r_p]$', fontsize=16, fontweight='bold', rotation=0, labelpad=20)

# Add grid and adjust limits
plt.xlim(0, 0.2)
plt.ylim(0, 0.25)

# Show the plot
plt.tight_layout()
plt.show()
