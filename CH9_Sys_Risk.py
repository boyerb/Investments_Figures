import matplotlib.pyplot as plt

# Data
N = [2, 10, 30, 60, 100]
variance = [0.010437, 0.004364, 0.004365, 0.003674, 0.003744]
idio = [0.007117, 0.001183, 0.000322, 0.000177, 0.000107]
sys = [0.00365, 0.003681, 0.003842, 0.003498, 0.003637]

# Create plot
plt.figure(figsize=(8, 5))
plt.plot(N, variance, label="Variance", color="blue", marker="o", linewidth=3, markersize=8)
plt.plot(N, idio, label="Idiosyncratic Risk", color="orange", marker="s", linewidth=3, markersize=8)
plt.plot(N, sys, label="Systematic Risk", color="green", marker="^", linewidth=3, markersize=8)

# Labels and legend
plt.xlabel("N", fontsize=16)
plt.ylabel("Risk", fontsize=16)
# plt.title('Portfolio Risk by Number of Stocks')
plt.legend(fontsize=14)
# plt.grid(True)
plt.tight_layout()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.savefig("plots/CH9_Sys_Risk.png", dpi=300)
# Show plot
plt.show()
