import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Define the line equation: y = slope * x + intercept
intercept = 0.04
slope = 0.24
x = np.linspace(0, 1, 100)
y = slope * x + intercept

# Define points and their labels
points = [(0, 0.04, "A"), (0.50, 0.16, "B"), (0.25, 0.10, "C"), (0.75, 0.22, "D")]

# Set seaborn style
sns.set(style="whitegrid")

# Create the plot with seaborn, change the line color to black
fig, ax = plt.subplots()  # Create figure and axes objects
ax.plot(x, y, label="Line: y = 0.24x + 0.04", linewidth=3, color="black")

# Plot the points with black markers, make them larger, and add labels above the points
for x_point, y_point, label in points:
    ax.scatter(x_point, y_point, color="black", s=100)  # Increase marker size using 's'
    if label == "A":
        ax.text(
            x_point + 0.025, y_point - 0.02, label, fontsize=15, color="black", ha="center"
        )  # Shift 'A' label slightly right
    else:
        ax.text(
            x_point, y_point + 0.01, label, fontsize=15, color="black", ha="center"
        )  # Keep other labels in place

# Remove the top and right spines (no box around the plot)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Increase thickness of the x and y axes
ax.spines["left"].set_linewidth(4)
ax.spines["bottom"].set_linewidth(4)

# Change color of the axes spines
ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")

# Shift the left spine (y-axis) to x=0
ax.spines["left"].set_position(("data", 0))  # Move the y-axis to the x=0 position
ax.spines["bottom"].set_position(("data", 0))  # Ensure x-axis crosses at y=0 as well

# Label axes with LaTeX formatting and no gridlines
ax.set_xlabel(r"$\sigma$", fontsize=18)  # Increase font size for x-axis label
ax.set_ylabel(
    r"$E[r]$", fontsize=18, rotation=0, labelpad=20
)  # Increase font size for y-axis label
ax.grid(False)  # Disable gridlines

# Function to format tick labels to two decimal places
formatter = FuncFormatter(lambda x, _: f"{x:.2f}")

# Apply the formatter to both axes
ax.xaxis.set_major_formatter(formatter)
ax.yaxis.set_major_formatter(formatter)

# Include the coordinates as tick labels
x_ticks = [point[0] for point in points]
y_ticks = [point[1] for point in points]
ax.set_xticks(np.concatenate([x_ticks, np.array([0, 1])]))  # Add 0 and 1 for the x-axis limits
ax.set_yticks(
    np.concatenate([y_ticks, np.array([intercept, intercept + slope])])
)  # Add line limits for y-axis

# Increase font size of tick labels
plt.tick_params(axis="both", which="major", labelsize=16)  # Adjust tick label size

# Set axis limits to prevent negative values
ax.set_xlim(0, 1.1)  # Prevent x-axis from going left of zero
ax.set_ylim(0, 0.3)  # Prevent y-axis from going below zero
plt.tight_layout()
plt.savefig("plots/CH6_6.2.1_First_Cal.png")
plt.show()
