import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Generate random data with correlation
np.random.seed(42)

n_points = 50
correlation = -0.9

mean = [0, 0]
cov = [[1, correlation], [correlation, 1]]
data = np.random.multivariate_normal(mean, cov, n_points)

x, y = data[:, 0], data[:, 1]
x, y = x / x.max(), y / y.max()

# Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x=x, y=y)

# Add regression line
slope = -1 / 3
intercept = 0
x_reg = np.linspace(-1.4, 1.4, 2)
y_reg = slope * x_reg + intercept
plt.plot(x_reg, y_reg, color="k", linewidth=2)

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

plt.xlabel("Portfolio Return")
plt.ylabel("Stock Return")

plt.grid(True)

plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

plt.savefig("plots/CH7_HW_7.6.19_no_fit.png")
plt.show()
