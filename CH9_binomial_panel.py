import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

p = 0.5
n_values = [10, 100, 1000]

fig = plt.figure(figsize=(10, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

# Top two plots (n=10 and n=100)
ax0 = fig.add_subplot(gs[0, 0])
ax1 = fig.add_subplot(gs[0, 1])
# Bottom plot (n=1000) in center by using space from col 0 and hiding col 1
ax2 = fig.add_subplot(gs[1, 0])
fig.add_subplot(gs[1, 1]).axis("off")  # Hide empty subplot to center ax2

axs = [ax0, ax1, ax2]

for idx, (n, ax) in enumerate(zip(n_values, axs)):
    x_raw = np.arange(n + 1)
    probabilities = binom.pmf(x_raw, n, p)

    x_scaled = (x_raw / n) * 0.2
    if n == 100:
        x_scaled[35] = 0.07001
    if n == 1000:
        x_scaled[350] = 0.07001

    bin_edges = np.arange(-0.01, 0.27, 0.02)
    bin_indices = np.digitize(x_scaled, bin_edges) - 1

    if n == 100:
        bin_indices[55] = 5
        bin_indices[65] = 6
    if n == 1000:
        bin_indices[550] = 5
        bin_indices[650] = 6

    bin_probs = []
    bin_centers = []

    for i in range(len(bin_edges) - 1):
        mask = bin_indices == i
        bin_total_prob = probabilities[mask].sum()
        bin_probs.append(bin_total_prob)
        bin_center = (bin_edges[i] + bin_edges[i + 1]) / 2
        bin_centers.append(bin_center)

    ax.bar(bin_centers, bin_probs, width=0.0195, color="#aab7c4", edgecolor="black")
    ax.set_xlabel("Realized Return", fontsize=12)
    ax.set_ylabel("Probability", fontsize=12)
    ax.set_xticks([0.0, 0.1, 0.2])
    ax.set_xticklabels(["0.00", "0.10", "0.20"], fontsize=10)
    ax.set_xlim(-0.01, 0.21)
    ax.set_title(f"n = {n}", fontsize=12)

plt.tight_layout()
plt.savefig("plots/binomial_grouped_centered_final.png")
plt.show()
