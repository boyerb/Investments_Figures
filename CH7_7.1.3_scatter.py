import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Generate random data with correlation
np.random.seed(42)

n_points = 100
correlation = 0

mean = [0, 0]
cov = [[1, correlation], [correlation, 1]]
data = np.random.multivariate_normal(mean, cov, n_points)

# Plot
sns.scatterplot(x=data[:, 0], y=data[:, 1])

# Add quadrant lines
plt.axhline(y=0, color="black", linestyle="-", alpha=0.5)
plt.axvline(x=0, color="black", linestyle="-", alpha=0.5)

# Add quadrant labels
dist = 2.6
plt.text(-dist, dist, "I", fontsize=12)
plt.text(dist, dist, "II", fontsize=12)
plt.text(dist, -dist, "III", fontsize=12)
plt.text(-dist, -dist, "IV", fontsize=12)

plt.xlabel("E")
plt.ylabel("F")

plt.xlim(-3, 3)
plt.ylim(-3, 3)

plt.xticks(ticks=[], labels=[])
plt.yticks(ticks=[], labels=[])

plt.savefig("plots/CH7_7.1.3_scatter.png")
plt.show()
