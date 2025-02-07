import numpy as np
import matplotlib.pyplot as plt

# Define the sigmoid function
def sigmoid(x, k=1, x0=0):
    """Compute the sigmoid function.

    Args:
        x (array-like): Input values.
        k (float): Steepness of the curve.
        x0 (float): Midpoint of the sigmoid curve.

    Returns:
        array-like: Sigmoid output values.
    """
    return 1 / (1 + np.exp(-k * (x - x0)))

# Generate x values for the plot
x = np.linspace(0.05, 3, 500)

# Sigmoid function parameters
k = 5  # Steepness
x0 = -0.2  # Midpoint

# Calculate the sigmoid values
y = sigmoid(x, k, x0)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, color="blue", linewidth=2, label="Sigmoid Curve")

# Add the dashed vertical line at x = 0.5
x_line = 0.5
y_line = sigmoid(x_line, k, x0)
plt.plot([x_line, x_line], [0, y_line], linestyle=(0, (15, 10)), color="black", label="Dashed Line")

# Add the horizontal line centered at the intersection point
plt.plot([x_line - 0.25, x_line + 0.25], [y_line, y_line], linestyle="-", color="black", linewidth=2, label="Horizontal Line")

# Add dashed lines from the horizontal line edges to the sigmoid curve
# Left dashed line goes down to the sigmoid curve
left_x = x_line - 0.25
left_y = sigmoid(left_x, k, x0)
plt.plot([left_x, left_x], [left_y, y_line], linestyle=(0, (5, 5)), color="black")
plt.text(left_x - 0.6, ((left_y + y_line) / 2) + 0.04, "Decrease in utility\nfrom loss.", fontsize=12, color="black", rotation=0, va="center", ha="left")

# Right dashed line goes up to the sigmoid curve
right_x = x_line + 0.25
right_y = sigmoid(right_x, k, x0)
plt.plot([right_x, right_x], [y_line, right_y], linestyle=(0, (5, 5)), color="black")
plt.text(right_x + 0.03, ((right_y + y_line) / 2) - 0.02, "Increase in utility\nfrom gain.", fontsize=12, color="black", rotation=0, va="center", ha="left")

# Customize labels and appearance
plt.xlabel("Wealth", fontsize=16, weight="bold")
plt.ylabel("Utility", fontsize=16, weight="bold", labelpad=80)
plt.grid(False)

# Set y-axis and x-axis limits
plt.ylim(0.75, 1.1)
plt.xlim(0, 3)

# Remove y-axis ticks
plt.yticks([])

# Remove top and right border lines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

# Adjust layout
plt.tight_layout()

# Save the figure with high resolution (300 dpi)
# plt.savefig("plots/CH6_Concave_Utility_Function2.png", dpi=300)

# Display the plot
plt.show()
