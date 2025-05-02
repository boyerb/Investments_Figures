import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

p = 0.5  # probability of success
n_values = [1, 2, 10, 100, 1000]

for n in n_values:
    bar_width = 0.01  # constant bar width in the scaled space
    if n > 10:
        bar_width = 0.001  # smaller bar width for larger n

    x_raw = np.arange(n + 1)  # 0 to n successes
    probabilities = binom.pmf(x_raw, n, p)

    # Scale x-values to the range [-0.2, 0.4]
    x_scaled = 0 + (x_raw / n) * 0.2  # maps 0 to -0.2, n to 0.4
    xtick_labels = [f"{val:.2f}" for val in x_scaled]

    plt.figure(figsize=(6, 4))
    plt.bar(x_scaled, probabilities, width=bar_width, color="black", edgecolor="black")

    plt.xlabel("Realized Return", fontsize=16)
    plt.ylabel("Probability", fontsize=16)
    plt.xticks([0.0, 0.1, 0.2], ["0.00", "0.10", "0.20"], fontsize=14)
    # plt.yticks(np.arange(0, max(probabilities) + 0.01, 0.01), fontsize=14)
    plt.xlim(-0.15, 0.35)  # fixed x-axis range

    plt.title(f"Binomial Distribution (n={n}, p={p})", fontsize=14)
    plt.tight_layout()
    plt.savefig(f"plots/binomial_n{n}.png")
    plt.show()
