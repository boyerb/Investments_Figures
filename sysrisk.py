import matplotlib.pyplot as plt
import numpy as np

# Range of beta values
beta = np.linspace(-2, 2, 400)

# CAPM expected return: rf + beta * (rm - rf)
rf = 0.02  # risk-free rate
rm = 0.08  # market return
expected_return = rf + (rm - rf) * beta


# Systematic risk is the absolute value of beta
vm = 0.04  # variance of the market
systematic_risk = (beta**2) * vm

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(beta, expected_return, label="Expected Return", color="black", linewidth=3)
plt.plot(beta, systematic_risk, label="Systematic Risk", color="black", linestyle="--", linewidth=3)

# Highlight an example with negative beta
# highlight_beta = -1.5
# highlight_return = rf + (rm - rf) * highlight_beta
# highlight_risk = abs(highlight_beta)
# plt.scatter([highlight_beta], [highlight_return], color="blue", zorder=5)
# plt.scatter([highlight_beta], [highlight_risk], color="red", zorder=5)
# plt.text(highlight_beta, highlight_return - 0.05, "Low Expected Return", color="blue", ha="center")
# plt.text(highlight_beta, highlight_risk + 0.05, "High Systematic Risk", color="red", ha="center")

# Axes and labels
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
# plt.title("Influence of Beta on Expected Return and Systematic Risk")
plt.xlabel("Beta Relative to Tangent Portfolio", fontsize=16)
# plt.ylabel("Value",fontsize=16)
plt.legend(fontsize=14)
# plt.grid(True)
plt.tight_layout()
plt.savefig("plots/CH9_sysrisk.png", dpi=300)
plt.show()
