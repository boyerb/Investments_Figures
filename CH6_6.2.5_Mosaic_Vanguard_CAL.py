import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))

# Define axes labels and styles
plt.xlabel("$\sigma$", fontsize=28, labelpad=15)
plt.ylabel("E[r]", fontsize=28, labelpad=30, rotation=0)

# Define Vanguard CAL (slope=0.3125, intercept=0.07)
intercept = 0.07
vanguard_sharpe = 0.3125
x_vanguard = np.linspace(0, 0.6, 100)
y_vanguard = intercept + vanguard_sharpe * x_vanguard
plt.plot(x_vanguard, y_vanguard, color="black", label="Vanguard CAL", linewidth=2)

# Define Mosaic CAL (slope=0.267, intercept=0.07)
mosaic_sharpe = 0.267
x_mosaic = np.linspace(0, 0.6, 100)
y_mosaic = intercept + mosaic_sharpe * x_mosaic
plt.plot(x_mosaic, y_mosaic, color="black", label="Mosaic CAL", linewidth=5)

# Define the Client's Portfolio point
client_portfolio = (0.2625, 0.14)
plt.scatter(*client_portfolio, color="black", s=200, edgecolor="black", zorder=5)
plt.text(
    client_portfolio[0] + 0.15,
    client_portfolio[1] - 0.022,
    "Client's Original Portfolio",
    fontsize=26,
    ha="center",
)

plt.gca().spines["left"].set_linewidth(4)  # Thicker left axis
plt.gca().spines["left"].set_color("black")  # Black color for bottom axis
plt.gca().spines["bottom"].set_linewidth(4)  # Thicker bottom axis
plt.gca().spines["bottom"].set_color("black")  # Black color for bottom axis
# Add dashed lines from Client's Portfolio
# Horizontal dashed line
plt.plot(
    [(client_portfolio[1] - intercept) / vanguard_sharpe, client_portfolio[0]],
    [client_portfolio[1], client_portfolio[1]],
    linestyle="dashed",
    color="black",
    linewidth=1.5,
)
# Vertical dashed line
plt.plot(
    [client_portfolio[0], client_portfolio[0]],
    [intercept + client_portfolio[0] * vanguard_sharpe, client_portfolio[1]],
    linestyle="dashed",
    color="black",
    linewidth=1.5,
)

# Set axis limits and ticks
plt.xlim(0, 0.6)
plt.ylim(0, 0.25)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)

# Adjust aspect ratio to make the angle between the lines larger
plt.gca().set_aspect(2, adjustable="box")  # Increase the aspect ratio to stretch the y-axis

plt.grid(False)
sns.despine()

# Final adjustments and show plot
plt.tight_layout()
plt.legend(fontsize=22, loc="upper left")
plt.savefig(
    "plots/CH6_6.2.5_Mosaic_Vanguard_CAL.png", dpi=300
)  # Save with high resolution (300 dpi)
plt.show()
