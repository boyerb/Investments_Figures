import matplotlib.pyplot as plt
import numpy as np

# Define x values from 0 to 100
x = np.linspace(0, 100, 1000)
y = np.log(x + 1)

# Points of interest (excluding the middle one)
points_xlabel = [f"\$500k", f"\$2M"]
points_x = [20, 80]
shift = 10  # Rightward shift

# Create the plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r"$\log(x+1)$", color="b", linewidth=2)  # Make curve darker

# Draw rightward and vertical lines and add labels
for xi in points_x:
    yi = np.log(xi + 1)
    xi_new = xi + shift
    yi_new = np.log(xi_new + 1)

    # Rightward line (darker, thicker)
    plt.plot([xi, xi_new], [yi, yi], color="darkred", linestyle="--", linewidth=2)
    # Upward line (darker, thicker)
    plt.plot([xi_new, xi_new], [yi, yi_new], color="darkred", linestyle="--", linewidth=2)

    # Annotate the vertical increase (larger text)
    increase = yi_new - yi
    plt.text(
        xi_new + 2,
        (yi + yi_new) / 2,
        f"{increase:.2f}",
        color="darkred",
        fontsize=14,
        fontweight="bold",
        verticalalignment="center",
    )

    # Draw dashed vertical lines down to x-axis (adjusted to start slightly below zero)
    plt.plot([xi, xi], [np.min(y) - 0.2, yi], color="black", linestyle="--", linewidth=1)

    # Label x-axis points
    # plt.text(xi, np.min(y) - 0.25, f'{xi}', color='black', fontsize=12, fontweight='bold', ha='center', va='top')

# brackets
mid_x = 21.8
bracket_y = np.log(20 + 1) - 0.37  # Adjust to place the bracket below the line
plt.text(
    mid_x,
    bracket_y,
    "}",
    rotation=-90,
    ha="center",
    va="center",
    fontsize=56,
    fontfamily="Courier New",
)

# Text below the bracket
plt.text(mid_x + 6, bracket_y - 0.25, "B Payoff", fontsize=12, color="black", ha="center")

mid_x = 81.8
bracket_y = np.log(80 + 1) - 0.37  # Adjust to place the bracket below the line
plt.text(
    mid_x,
    bracket_y,
    "}",
    rotation=-90,
    ha="center",
    va="center",
    fontsize=56,
    fontfamily="Courier New",
)

# Text below the bracket
plt.text(mid_x + 6, bracket_y - 0.25, "A Payoff", fontsize=12, color="black", ha="center")


# Labels and title (larger font sizes)
plt.ylabel("Utility", fontsize=14)  # Updated y-axis label
plt.xlabel("Wealth of Typical Investor", fontsize=14)

# Remove x-axis tick number labels
plt.xticks([])

# Adjust the y-axis to start slightly below zero (keep the box bottom slightly below zero)
plt.ylim(bottom=np.min(y) - 0.2)  # Make the bottom of the box slightly below the minimum value of y
plt.xticks(points_x, points_xlabel, fontsize=12, fontweight="bold")


# Save the plot
plt.savefig("plots/CH9_x.2_utility.png", dpi=300)

# Show the plot
plt.show()
