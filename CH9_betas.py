import matplotlib.pyplot as plt

# Points for each asset
x_vals = [-0.6, 0.6]

# Asset A (red line through black points)
y_a = [0.6733, -1.01]
plt.plot(x_vals, y_a, color="red", label="Asset A")
plt.scatter(x_vals, y_a, color="red", s=80)  # black points, larger size

# Asset B (blue line)
y_b = [-0.0824, 0.1237]
plt.plot(x_vals, y_b, color="blue", label="Asset B")
plt.scatter(x_vals, y_b, color="blue", s=80)

# Asset C (orange line)
y_c = [-0.5509, 0.8264]
plt.plot(x_vals, y_c, color="orange", label="Asset C")
plt.scatter(x_vals, y_c, color="orange", s=80)

# Labels and legend
plt.xlabel("Wealth", fontsize=12)
plt.ylabel("Return", fontsize=12)
plt.tick_params(axis="both", labelsize=10)  # Increase tick label size
plt.legend()
plt.legend(fontsize=10)  # Increase legend font size
# plt.grid(True)
# plt.title("Asset Returns vs. Wealth")

# Save the plot
plt.savefig("plots/CH9_betas.png", dpi=300)

plt.show()
