import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style and context
sns.set_style("white")
# sns.set_context("talk")

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Define points
point_B = (0.05, 0.075)
point_P = (0.15, 0.175)
point_A = (0.25, 0.275)

# Draw the efficient frontier line
x_line = [0, 0.3]
y_line = [point_B[1] - 0.05, 0.3 + point_B[1] - 0.05]
ax.plot(x_line, y_line, color="black", linewidth=2)

# Add shaded region
x_fill = [0, point_B[0], point_A[0], 0]
y_fill = [point_B[1] - 0.05, point_B[1], point_A[1], point_B[1] - 0.05]
x_fill = [0, 0, 0.3]
y_fill = [point_B[1] - 0.05, 0.3 + point_B[1] - 0.05, 0.3 + point_B[1] - 0.05]
ax.fill(x_fill, y_fill, color="gray", alpha=0.5)


# Plot points
ax.scatter(*point_B, color="black", s=100, label="B")
ax.scatter(*point_P, color="black", s=100, label="P")
ax.scatter(*point_A, color="black", s=100, label="A")

# Add dashed vertical lines
ax.vlines(point_B[0], 0, point_B[1], linestyles="dashed", colors="black")
ax.vlines(point_A[0], 0, point_A[1], linestyles="dashed", colors="black")

# Annotate points
ax.text(point_B[0] + 0.01, point_B[1] - 0.01, "B", fontsize=22, va="center", ha="left")
ax.text(point_P[0] + 0.01, point_P[1] - 0.03, "Asset with\nmaximum\nSharpe Ratio", fontsize=22, va="center", ha="left")
ax.text(point_A[0] + 0.01, point_A[1] - 0.01, "A", fontsize=22, va="center", ha="left")

# Annotate the region
ax.text(0.03, 0.22, "Impossible to\ncreate portfolios in\nthis region.", fontsize=22, va="center", ha="left", 
        bbox=dict(facecolor='white', edgecolor='black'))

# Set limits, labels, and ticks
ax.set_xlim(0, 0.3)
ax.set_ylim(0,0.3)
ax.set_xlabel("$\\sigma$", fontsize=26)
ax.set_ylabel("E[r]", fontsize=26)
ax.set_xticks([point_B[0], point_A[0]])
ax.set_xticklabels(["$x_B$", "$x_A$"], fontsize=22)
ax.set_yticks([])

# Remove grid lines and spines
ax.grid(False)
sns.despine(ax=ax)

# Show the plot
plt.tight_layout()
plt.savefig(
    "plots/CH6_6.2.4_two_fund_separation.png", dpi=300
)  # Save with high resolution (300 dpi)