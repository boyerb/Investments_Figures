import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))

# Generate data points for the utility curve
x = np.linspace(0, 10, 1000)
y = 5 * (1 - np.exp(-0.5 * x))  # Diminishing returns function

plt.plot(x, y, "k-", linewidth=2)

# Define the two key points (R and E)
r_x, e_x = 3, 8
r_y = 5 * (1 - np.exp(-0.5 * r_x))
e_y = 5 * (1 - np.exp(-0.5 * e_x))

# Plot the points
plt.plot(r_x, r_y, "ko", markersize=10)
plt.plot(e_x, e_y, "ko", markersize=10)

# Draw dashed vertical lines
plt.axvline(x=r_x, color="gray", linestyle="--")
plt.axvline(x=e_x, color="gray", linestyle="--")

# Draw marignal untility lines for R
r_y_2 = 5 * (1 - np.exp(-0.5 * (r_x + 2)))
plt.plot([r_x, r_x + 2], [r_y, r_y], color="gray", linestyle="--")
plt.plot([r_x + 2, r_x + 2], [r_y, r_y_2], color="gray", linestyle="--")

# Add utility annotations
plt.text(r_x + 2.2, r_y + 0.3, "added utility", fontsize=10)
plt.text(r_x + 0.2, r_y - 0.5, "extra $2\nfrom Ace", fontsize=10, color="k")

plt.text(
    e_x + 0.2,
    e_y - 0.75,
    "extra $2\nfrom BMW\nadds almost nothing to\nutility",
    fontsize=10,
    color="k",
)

# Set axis labels
plt.ylabel("Utility", fontsize=14)
plt.xlabel("Consumption Next Year", fontsize=14)

# Remove top and right spines
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

# Set the limits
plt.xlim(-0.5, 12)
plt.ylim(-0.5, 6)

# Remove x-ticks
plt.xticks(ticks=[r_x, e_x], labels=["R", "E"], fontsize=12)
plt.yticks([])

plt.tight_layout()
plt.savefig("plots/CH9_9.1.1_concave_wealth.png", dpi=300)
