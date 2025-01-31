import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Define axes labels
plt.xlabel("$\sigma$", fontsize=26, labelpad=15)
plt.ylabel("E[r]", fontsize=26, labelpad=30, rotation=0)

# Define the Capital Allocation Line (CAL)
x_cal = np.linspace(0, 0.4, 100)
y_cal = 0.02 + 0.44 * x_cal
plt.plot(x_cal, y_cal, color="black", linewidth=3)

# Define points
conservative_position = (0.081, 0.056)
fund = (0.18, 0.1)
levered_position = (0.27, 0.14)

# Plot points with labels
labels = ["3", "1", "2"]
for i, (x, y, label) in enumerate(
    [
        (conservative_position[0], conservative_position[1], "Conservative Position"),
        (fund[0], fund[1], "Fund"),
        (levered_position[0], levered_position[1], "Levered Position"),
    ],
    start=1,
):
    plt.scatter(x, y, color="black", s=200, zorder=5)
    plt.text(x - 0.01, y + 0.001, labels[i - 1], fontsize=20, color="black", ha="center")
    plt.text(x + 0.01, y - 0.015, label, fontsize=20, color="black")

# Add arrows and labels for lending and borrowing
plt.annotate(
    "",
    xy=(0.03, 0.0582),
    xytext=(0.16, 0.1154),
    arrowprops=dict(facecolor="black", edgecolor="black", arrowstyle="->", linewidth=3),
    fontsize=22,
    color="black",
    ha="center",
)

plt.text(
    (0.03 + 0.16) / 2,
    (0.0582 + 0.1154) / 2 + 0.015,
    "Risk Free Lending",
    rotation=25,  # Rotate text to match arrow angle
    rotation_mode="anchor",  # Rotate around anchor point
    fontsize=20,
    ha="center",
    va="center",  # Center-align text
)

plt.annotate(
    "",
    xy=(0.33, 0.1902),
    xytext=(0.20, 0.133),
    arrowprops=dict(facecolor="black", edgecolor="black", arrowstyle="->", linewidth=3),
    fontsize=22,
    color="black",
    ha="center",
)

plt.text(
    (0.33 + 0.20) / 2,
    (0.1902 + 0.133) / 2 + 0.015,
    "Risk Free Borrowing",
    rotation=25,  # Rotate text to match arrow angle
    rotation_mode="anchor",  # Rotate around anchor point
    fontsize=20,
    ha="center",
    va="center",  # Center-align text
)

plt.gca().spines["left"].set_linewidth(5)  # Thicker left axis
plt.gca().spines["left"].set_color("black")  # Black color for bottom axis
plt.gca().spines["bottom"].set_linewidth(5)  # Thicker bottom axis
plt.gca().spines["bottom"].set_color("black")  # Black color for bottom axis

# Set axis limits and ticks
plt.xlim(0, 0.4)
plt.ylim(0, 0.22)

# Get current x and y ticks
xticks = plt.xticks()[0]
yticks = plt.yticks()[0]

# Replace the 0.00 tick label with an empty string
xtick_labels = ["" if tick == 0 else f"{tick:.2f}" for tick in xticks]
ytick_labels = ["" if tick == 0 else f"{tick:.2f}" for tick in yticks]

# Set updated tick labels
plt.xticks(xticks, xtick_labels, fontsize=22)
plt.yticks(yticks, ytick_labels, fontsize=22)

plt.grid(False)
sns.despine()

# Final adjustments and show plot
plt.tight_layout()
plt.savefig("plots/CH6_6.3.1_moving_along_CAL.png", dpi=300)  # Save with high resolution (300 dpi)
plt.show()
