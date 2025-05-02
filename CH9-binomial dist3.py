import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

p = 0.5
n_values = [1, 2, 10, 100, 1000]
# n_values = [1000]

for n in n_values:
    # Raw outcomes: 0 to n successes
    x_raw = np.arange(n + 1)
    probabilities = binom.pmf(x_raw, n, p)

    # Scale x values to match the return axis: 0 to 0.2 (or shift as needed)
    x_scaled = (x_raw / n) * 0.2  # outcome 0 -> 0.0, outcome n -> 0.2
    if n == 100:
        x_scaled[35] = 0.07001
    if n == 1000:
        x_scaled[350] = 0.07001
    # Define bins of equal width 0.05 over the range 0 to 0.2
    bin_edges = np.arange(-0.01, 0.27, 0.02)  # bins: [0.00–0.05), [0.05–0.10), ...
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

    # Plot
    plt.figure(figsize=(6, 4))
    plt.bar(bin_centers, bin_probs, width=0.0195, color="#aab7c4", edgecolor="black")

    plt.xlabel("Realized Return", fontsize=18)
    plt.ylabel("Probability", fontsize=18)
    plt.xticks([0.0, 0.1, 0.2], ["0.00", "0.10", "0.20"], fontsize=16)
    plt.xlim(-0.05, 0.25)
    # plt.title(f"Binomial Distribution (n={n}, p={p})", fontsize=14)
    plt.tight_layout()
    plt.savefig(f"plots/binomial_grouped_n{n}.png")
    plt.show()
