import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style and figure size
sns.set(style="whitegrid", context="talk")
fig, ax = plt.subplots(figsize=(10, 6))

# Define data points
points = {
    "A": (0.05, 0.05),
    "Portfolio\ninvested 100%\nin Index Fund": (0.17, 0.12),
    "B": (0.306, 0.20)
}
x_vals = [p[0] for p in points.values()]
y_vals = [p[1] for p in points.values()]

# Draw the diagonal line (adjusted intercept at 0.02)
intercept = 0.02
slope = (y_vals[-1] - intercept) / x_vals[-1]
ax.plot([0, 0.4], [intercept, intercept + slope * 0.4], color="black", linewidth=6)

# Add points and dashed lines
for label, (x, y) in points.items():
    ax.plot(x, y, 'o', color="black", markersize=10)
    ax.axhline(y=y, xmin=0, xmax=x/0.4, linestyle="--", color="black")
    ax.axvline(x=x, ymin=0, ymax=y/0.3, linestyle="--", color="black")
    if "Portfolio" in label:
        ax.text(x - 0.01, y + 0.035, label, fontsize=22, ha="right", va="center")  # Move to the left
    else:
        ax.text(x, y + 0.01, label, fontsize=22, ha="center")

# Set axis labels and ticks
ax.set_xlabel(r"$\sigma$", fontsize=26)
ax.set_ylabel(r"$E[r]$", fontsize=26)
ax.set_xlim(0, 0.4)
ax.set_ylim(0, 0.3)
ax.set_xticks([0.05, 0.17, 0.306])
ax.set_xticklabels([0.05, 0.17, 0.306], fontsize=22)
ax.set_yticks([0.02, 0.05, 0.12, 0.20])
ax.set_yticklabels([0.02, 0.05, 0.12, 0.20], fontsize=22)

# Save the plot
plt.grid(False)
plt.tight_layout()
plt.savefig(
    "plots/CH6_capital_allocation_line.png", dpi=300
)  # Save with high resolution (300 dpi)
plt.show()
