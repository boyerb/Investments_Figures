import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

np.random.seed(42)


def generate_correlated_data(rho, n=100):
    mean = [0, 0]
    cov = [[1, rho], [rho, 1]]
    return np.random.multivariate_normal(mean, cov, n)


fig, axes = plt.subplots(2, 2, figsize=(10, 6))

# Parameters
correlations = [0.74, -0.76, 1, -1]
colors = ["blue", "blue", "red", "red"]
n_points = [50, 50, 50, 50]

for i, (ax, rho, color, n) in enumerate(zip(axes.flat, correlations, colors, n_points)):

    # Generate data
    data = generate_correlated_data(rho, n)

    # Create scatter plot
    ax.scatter(data[:, 0], data[:, 1], color=color, alpha=0.6)

    # Add correlation coefficient text
    if rho == 1:
        text = f"ρ=+1"
    else:
        text = f"ρ={rho}"
    ax.text(0.05, 0.95, text, transform=ax.transAxes, verticalalignment="top", fontsize=12)

    # Bounds
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    # Axis lines
    ax.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
    ax.axvline(x=0, color="k", linestyle="-", linewidth=0.5)

    # Grid
    ax.grid(True, linestyle="--", alpha=0.3)

    # Ticks
    ax.set_xticks([])
    ax.set_yticks([])

plt.savefig("plots/CH7_7.2.1_scatter.png")
plt.show()
