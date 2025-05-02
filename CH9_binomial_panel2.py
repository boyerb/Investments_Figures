import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

p = 0.5
n_values = [2, 10, 100, 1000]

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Flatten the 2x2 grid of axes for easy indexing
axs = axs.flatten()

# Loop over the n_values and plot each on the respective subplot
for idx, n in enumerate(n_values):
    x_raw = np.arange(n + 1)
    probabilities = binom.pmf(x_raw, n, p)

    # Scale x values to match the return axis: 0 to 0.2
    x_scaled = (x_raw / n) * 0.2
    if n == 100:
        x_scaled[35] = 0.07001
    if n == 1000:
        x_scaled[350] = 0.07001

    # Define bins of equal width 0.05 over the range 0 to 0.2
    bin_edges = np.arange(-0.01, 0.27, 0.02)
    bin_indices = np.digitize(x_scaled, bin_edges) - 1  # match x values to bins
    if n == 100:
        bin_indices[55] = 5
        bin_indices[65] = 6
    if n == 1000:
        bin_indices[550] = 5
        bin_indices[650] = 6

    # Sum probabilities within each bin
    bin_probs = []
    bin_centers = []

    for i in range(len(bin_edges) - 1):
        mask = bin_indices == i
        bin_total_prob = probabilities[mask].sum()
        bin_probs.append(bin_total_prob)

        # Compute the bin center for plotting
        bin_center = (bin_edges[i] + bin_edges[i + 1]) / 2
        bin_centers.append(bin_center)

    # Plot on the correct axis in the grid
    axs[idx].bar(bin_centers, bin_probs, width=0.0195, color="#aab7c4", edgecolor="black")

    axs[idx].set_xlabel("Realized Return", fontsize=16)
    axs[idx].set_ylabel("Probability", fontsize=16)
    axs[idx].tick_params(axis="y", labelsize=14)
    axs[idx].set_xticks([0.0, 0.1, 0.2])
    axs[idx].set_xticklabels(["0.00", "0.10", "0.20"], fontsize=14)
    axs[idx].set_xlim(-0.05, 0.25)
    axs[idx].set_title(f"{n} Securities", fontsize=19)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Save the figure
plt.savefig("plots/binomial_grouped_2x2.png")

# Show the plot
plt.show()
