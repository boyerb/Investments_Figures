import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Lakers' leading scorer PPG and team win percentage from 1980 to present
ppg = [
    26.2,
    23.9,
    21.8,
    21.5,
    22.0,
    23.4,
    23.9,
    19.6,
    22.5,
    22.3,
    19.4,
    19.9,
    19.9,
    14.2,
    21.7,
    21.2,
    26.2,
    28.3,
    26.3,
    29.7,
    28.7,
    27.2,
    30.0,
    21.5,
    27.6,
    35.4,
    31.6,
    28.3,
    26.8,
    27.0,
    25.3,
    27.9,
    27.3,
    17.9,
    22.3,
    17.6,
    18.6,
    16.1,
    27.4,
    25.9,
    26.1,
]

win_percentage = [
    65.9,
    69.5,
    70.7,
    65.9,
    75.6,
    75.6,
    79.3,
    75.6,
    69.5,
    76.8,
    70.7,
    52.4,
    47.6,
    40.2,
    58.5,
    64.6,
    68.3,
    74.4,
    62.0,
    81.7,
    68.3,
    70.7,
    61.0,
    68.3,
    41.5,
    54.9,
    51.2,
    69.5,
    79.3,
    69.5,
    69.5,
    62.1,
    54.9,
    32.9,
    25.6,
    20.7,
    31.7,
    42.7,
    45.1,
    73.2,
    67.1,
]

# Convert win percentage to decimal
win_percentage = [w / 100 for w in win_percentage]

# Remove the (29.7, 81.7) point before plotting
filtered_ppg = [x for x, y in zip(ppg, win_percentage) if x != 29.7 or y != 81.7 / 100]
filtered_win_percentage = [y for x, y in zip(ppg, win_percentage) if x != 29.7 or y != 81.7 / 100]

# Compute regression line equation
slope, intercept = np.polyfit(ppg, win_percentage, 1)

# Extend regression line to the y-axis (x=0)
x_vals = np.linspace(0, max(ppg), 100)  # Generate x values from 0 to max(ppg)
y_vals = slope * x_vals + intercept  # Compute corresponding y values

# Create scatter plot (without Seaborn's regression line)
plt.figure(figsize=(10, 6))
ax = sns.regplot(
    x=filtered_ppg,
    y=filtered_win_percentage,
    scatter_kws={"s": 100, "color": "black"},
    fit_reg=False,
)

# Manually plot the extended regression line (only one black line)
plt.plot(x_vals, y_vals, color="black", lw=3.0)

# Highlight (29.7, 81.7) with a star (no black dot behind it)
plt.scatter(
    29.7, 81.7 / 100, color="black", s=400, marker="*", label="1999-2000 Season\n x=29.7, y=81.7"
)

# Calculate expected win percentage at PPG = 29.7
expected_win_pct = slope * 29.7 + intercept

# Ensure axes start from 0
plt.ylim(0, plt.ylim()[1])
plt.xlim(0, plt.xlim()[1])

# Draw dashed vertical line from 29.7 to regression line
plt.plot([29.7, 29.7], [0, expected_win_pct], linestyle="dashed", color="gray")

# Draw dashed horizontal line from expected value to the y-axis (x=0)
plt.plot([0, 29.7], [expected_win_pct, expected_win_pct], linestyle="dashed", color="gray")

# Illustrate residual with a dashed line
plt.plot([29.7, 29.7], [expected_win_pct, 81.7 / 100], linestyle="dashed", color="black")

# Add curly brace for residual
plt.text(
    32,
    0.735,
    "Residual\n z=0.139",
    fontsize=14,
    color="black",
    bbox=dict(facecolor="white", edgecolor="none", boxstyle="round,pad=0.3"),
)
plt.text(30.3, 0.698, r"}", fontsize=64, color="black", fontname="Calibri", fontweight="light")
plt.text(3.7, 0.56, "E[y|x=29.7]=67.83%", fontsize=16, color="black", rotation=0)
plt.text(23, 0.07, "x=29.7", fontsize=16, color="black", rotation=0)
plt.annotate(
    "",
    xy=(0.1, 0.67),
    xytext=(3.5, 0.59),
    arrowprops=dict(facecolor="black", edgecolor="black", arrowstyle="->", lw=2, mutation_scale=20),
)
plt.annotate(
    "",
    xy=(29.6, 0.005),
    xytext=(27, 0.06),
    arrowprops=dict(facecolor="black", edgecolor="black", arrowstyle="->", lw=2, mutation_scale=20),
)


# Labels and title
plt.xlabel("Leading Scorer's PPG", fontsize=18)
plt.ylabel("Win Percentage", fontsize=18)
plt.tick_params(axis="both", which="major", labelsize=18)
# plt.legend()
plt.legend(loc="upper left", bbox_to_anchor=(0.05, 1), fontsize=14)

# Display the plot
plt.savefig("plots/CH7_7.0.1_lakers_ppg_vs_win_percentage.png", dpi=300)
plt.show()
