import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# plt.rcParams["text.usetex"] = True

# Lakers' leading scorer PPG and team win percentage from 1980 to present
ppg = [
    30.0,
    27.7,
    26.2,
    25.8,
    23.8,
    24.8,
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
    15.1,
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
    24.0,
    27.6,
    35.4,
    31.6,
    28.3,
    26.8,
    27.0,
    25.3,
    27.9,
    27.3,
    17.4,
    12.0,
    17.6,
    15.6,
    16.1,
    27.4,
    26.1,
    25.0,
    30.3,
    28.9,
    25.7,
    24.4,
]

win_percentage = [
    36.6,
    48.8,
    64.6,
    54.9,
    57.3,
    73.2,
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
    58.3,
    40.2,
    52.4,
    57.3,
    61.5,
]

# Convert win percentage to decimal
# win_percentage = [w / 100 for w in win_percentage]

# Create scatter plot with line of best fit
plt.figure(figsize=(10, 6))
sns.regplot(
    x=ppg,
    y=win_percentage,
    scatter_kws={"s": 100, "color": "black"},
    line_kws={"color": "black", "lw": 3.0},
    ci=None,
)

# Labels and title
plt.xlabel("Leading Scorer's PPG", fontsize=18)
plt.ylabel("Win Percentage (%)", fontsize=18)
# plt.title("Los Angeles Lakers: PPG vs. Win Percentage (1980-Present)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=18)

# Add text box with regression coefficients
textstr = "a = 34.89\nb =  1.02"
plt.text(
    30,
    25,
    textstr,
    fontsize=16,
    family="monospace",
    bbox=dict(facecolor="white", edgecolor="black", boxstyle="round,pad=0.5"),
)

# Display the plot
plt.savefig("plots/CH7_7.0.0_lakers_ppg_vs_win_percentage.png", dpi=300)
plt.show()
