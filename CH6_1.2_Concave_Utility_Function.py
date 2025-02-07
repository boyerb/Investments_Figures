import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Function to generate utility values with adjustable parameters
def utility_function(wealth, scale=1, shift=1, exponent=1):
    """
    Compute utility values with adjustable parameters.

    Parameters:
    - wealth: Array of wealth values.
    - scale: Controls the steepness of the curve.
    - shift: Determines where the elbow occurs.
    - exponent: Controls the shape of the curve (higher values flatten it faster).

    Returns:
    - Array of utility values.
    """
    return scale * np.log(wealth + shift)**exponent

# Set a professional style using seaborn
sns.set_theme(style="whitegrid")

# Generate data for the plot
wealth = np.linspace(0, 5, 500)

# Parameters to control the curve's shape and position
scale = 1        # Adjusts steepness
shift = 0.9        # Moves the elbow left/right
exponent = 0.25   # Determines how quickly the curve flattens

# Calculate utility with custom parameters
utility = utility_function(wealth, scale=scale, shift=shift, exponent=exponent)

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(wealth, utility, label="Utility Curve", color="blue", linewidth=2)

# Customize the plot
plt.xlabel("Wealth", fontsize=16, weight="bold")
plt.ylabel("Utility", fontsize=16, weight="bold")
plt.ylim(0, 1.2)
plt.xlim(0, 5)

# Remove axis labels entirely
plt.xticks([])
plt.yticks([])

plt.tight_layout()

# Save the figure with high resolution (300 dpi)
# plt.savefig("plots/CH6_Concave_Utility_Function1.png", dpi=300)

# Display the plot
plt.show()

