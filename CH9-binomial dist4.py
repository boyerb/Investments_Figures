import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

# Parameters
n = 2  # number of trials
p = 0.5  # probability of success

# Generate binomial probabilities
x = range(n + 1)  # possible outcomes: 0 to n successes
probabilities = binom.pmf(x, n, p)

scaled_labels = [f"{i / n * 0.2:.2f}" for i in x]
yticks = np.arange(0, max(probabilities) + 0.1, 0.1)

# Plot
plt.bar(x, probabilities, color="black", edgecolor="black", width=0.30)
# plt.title(f"Binomial Distribution (n={n}, p={p})")
plt.xlabel("Realized Return", fontsize=16)
plt.ylabel("Probability", fontsize=16)
plt.xticks(x, scaled_labels, fontsize=14)
plt.yticks(yticks, fontsize=14)
# plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the plot
plt.savefig("plots/CH9-binomial dist4.png")
plt.show()
