import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")
plt.figure(figsize=(10, 8))

# Define axes labels and styles
plt.xlabel("Portfolio Standard Deviation", fontsize=26, labelpad=15)
plt.ylabel("Portfolio Expected Return", fontsize=26, labelpad=15)

# Define Vanguard CAL (slope=0.3125, intercept=0.07)
intercept = 0.07
vanguard_sharpe = 0.3125
x_vanguard = np.linspace(0, 0.6, 100)
y_vanguard = intercept + vanguard_sharpe * x_vanguard
plt.plot(x_vanguard, y_vanguard, color="blue", label="Vanguard CAL", linewidth=2)

# Define Mosaic CAL (slope=0.267, intercept=0.07)
mosaic_sharpe = 0.267
x_mosaic = np.linspace(0, 0.6, 100)
y_mosaic = intercept + mosaic_sharpe * x_mosaic
plt.plot(x_mosaic, y_mosaic, color="red", label="Mosaic CAL", linewidth=2)

# Define the Client's Portfolio point
client_portfolio = (0.2625, 0.14)
plt.scatter(*client_portfolio, color="cyan", s=100, edgecolor="black", zorder=5)
plt.text(
    client_portfolio[0] + 0.1,
    client_portfolio[1] - 0.012,
    "Client's Portfolio",
    fontsize=22,
    ha="center",
)

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
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

plt.grid(False)
sns.despine()

# Final adjustments and show plot
plt.tight_layout()
plt.legend(fontsize=22, loc="upper left")
plt.savefig(
    "plots/CH6_6.2.5_Mosaic_Vanguard_CAL.png", dpi=300
)  # Save with high resolution (300 dpi)
