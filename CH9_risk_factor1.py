import matplotlib.pyplot as plt
import numpy as np

# Generate x values
x = np.linspace(-5, 5, 10)

# Lines with slope 1 and -1
y_pos = x  # slope of 1
y_neg = -x  # slope of -1

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x, y_pos, color="red", linewidth=3, label="Asset with +Beta")
plt.plot(x, y_neg, color="green", linewidth=3, label="Asset with -Beta")

# Label axes
plt.xlabel("GDP growth", fontsize=14)
plt.ylabel("Return", fontsize=14)

# Remove ticks (you can also keep them if you want, just comment these out)
plt.xticks([])
plt.yticks([])

plt.legend()

# Show plot
# plt.grid(True)
# plt.title('Lines with Slopes ±1')
# Save the plot
plt.savefig("plots/CH9_risk_factor1.png", dpi=300)
plt.show()
