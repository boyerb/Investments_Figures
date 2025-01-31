import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style and figure size
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(8, 8))
fig.tight_layout()

# Define data points
points = {
    1: (0.25, 0.20),  # Point 1
    2: (0.15, 0.128),  # Point 2
    3: (0.25, 0.128),  # Point 3
    4: (0.0417, 0.05),  # Point 4
    5: (0.0694, 0.07),  # Point 5
    6: (0.0694, 0.05),  # Point 6
}

# Draw the CAL lines with the same intercept
x = [0, 0.4]
intercept = 0.02
red_slope = (points[1][1] - intercept) / points[1][0]
orange_slope = (points[3][1] - intercept) / points[3][0]

red_line = [intercept + red_slope * i for i in x]
orange_line = [intercept + orange_slope * i for i in x]

ax.plot(x, red_line, color="black", linewidth=4, label="CAL line Asset A")
ax.plot(x, orange_line, color="black", linewidth=7, label="CAL line Asset B")

# Add dashed lines between specified points
dashed_pairs = [(4, 6), (5, 6), (1, 3), (2, 3)]
for p1, p2 in dashed_pairs:
    x_vals = [points[p1][0], points[p2][0]]
    y_vals = [points[p1][1], points[p2][1]]
    ax.plot(x_vals, y_vals, linestyle="--", color="black", linewidth=1.5)

# Add points with labels
for idx, (x, y) in points.items():
    ax.plot(x, y, "o", color="black", markersize=14)
    ax.text(x - 0.009, y + 0.003, str(idx), fontsize=22, ha="center")

# Add investor labels
ax.text(0.303, 0.10, "Investor with\nlow aversion to risk", fontsize=22, ha="center")
ax.text(0.123, 0.02, "Investor with\nhigh aversion to risk", fontsize=22, ha="center")

# Set axis labels and ticks
ax.set_xlabel(r"$\sigma$", fontsize=26, rotation=0)
ax.set_ylabel(r"$E[r]$", fontsize=26, rotation=0, labelpad=30, va="top")
ax.set_xlim(0, 0.4)
ax.set_ylim(0, 0.22)
ax.tick_params(axis="both", labelsize=22)

# Add legend
ax.legend(fontsize=22, loc="upper left")
ax.set_xticks([])
ax.set_yticks([])

# Remove the top and right spines (no box around the plot)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Increase thickness of the x and y axes
ax.spines["left"].set_linewidth(5)
ax.spines["bottom"].set_linewidth(5)

ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")


# Show the plot
plt.grid(False)
plt.tight_layout()
plt.savefig("plots/CH6_6.2.3_two_CAL_lines.png", dpi=300)  # Save with high resolution (300 dpi)
plt.show()
