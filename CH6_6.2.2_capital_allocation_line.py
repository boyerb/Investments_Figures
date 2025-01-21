import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style and figure size
sns.set_theme(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(10, 6))

# Define data points
points = {
    "B": (0.05, 0.05),
    "Portfolio\ninvested 100%\nin Index Fund": (0.17, 0.12),
    "A": (0.306, 0.20),
}
x_vals = [p[0] for p in points.values()]
y_vals = [p[1] for p in points.values()]

# Draw the diagonal line (adjusted intercept at 0.02)
intercept = 0.02
slope = (y_vals[-1] - intercept) / x_vals[-1]
ax.plot([0, 0.4], [intercept, intercept + slope * 0.4], color="black", linewidth=4)

# Add points and dashed lines
for label, (x, y) in points.items():
    ax.plot(x, y, "o", color="black", markersize=16)
    ax.axhline(y=y, xmin=0, xmax=x / 0.4, linestyle="--", color="black")
    ax.axvline(x=x, ymin=0, ymax=y / 0.3, linestyle="--", color="black")
    if "Portfolio" in label:
        ax.text(x - 0.11, y + 0.040, label, fontsize=18, ha="left", va="center")  # Move to the left
    elif label == "A" or label == "B":
        ax.text(x, y + 0.015, label, fontsize=26, ha="center")  # Increased font size for A and B
    else:
        ax.text(x, y + 0.01, label, fontsize=22, ha="center")

# Set axis labels and ticks
ax.set_xlabel(r"$\sigma$", fontsize=26, labelpad=20, ha="right")
ax.set_ylabel(r"$E[r]$", fontsize=26, labelpad=20, rotation=0, va="top")
ax.yaxis.set_label_position("left")  # Move the y label to the top

ax.set_xlim(0, 0.4)
ax.set_ylim(0, 0.3)
ax.set_xticks([0.05, 0.17, 0.306])
ax.set_xticklabels([0.05, 0.17, 0.306], fontsize=22)
ax.set_yticks([0.02, 0.05, 0.12, 0.20])
ax.set_yticklabels([0.02, 0.05, 0.12, 0.20], fontsize=22)

# Remove the top and right spines (no box around the plot)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Increase thickness of the x and y axes
ax.spines["left"].set_linewidth(7)
ax.spines["bottom"].set_linewidth(7)

ax.spines["left"].set_color("black")
ax.spines["bottom"].set_color("black")

# Calculate midpoint between points A and B
mid_x = x_vals[1] - 0.005
mid_y = y_vals[1] + 0.005

# Add an arrow from the "d" in "Fund" to the midpoint between A and B
ax.annotate(
    "",
    xy=(mid_x, mid_y),  # Midpoint between A and B
    xytext=(x_vals[1] - 0.03, y_vals[1] + 0.020),  # Near the "d" in "Fund"
    arrowprops=dict(facecolor="black", edgecolor="black", arrowstyle="->", lw=2),
)

# Save the plot
plt.grid(False)
plt.tight_layout()
plt.savefig(
    "plots/CH6_6.2.2_capital_allocation_line.png", dpi=300
)  # Save with high resolution (300 dpi)
plt.show()
