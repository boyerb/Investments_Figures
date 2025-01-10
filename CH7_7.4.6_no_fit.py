import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Generate random data with correlation
np.random.seed(42)

n_points = 50
correlation = 0.7

mean = [0, 0]
cov = [[1, correlation], [correlation, 1]]
data = np.random.multivariate_normal(mean, cov, n_points)

x, y = data[:, 0], data[:, 1]
x, y = x / x.max() * 0.15, y / y.max() * 0.15

# Plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x=x, y=y)

# Add regression line
slope = -0.1 / 0.15
intercept = 0
x_reg = np.linspace(-0.14, 0.14, 2)
y_reg = slope * x_reg + intercept
plt.plot(x_reg, y_reg, color="k", linewidth=2)

plt.xlim(-0.15, 0.15)
plt.ylim(-0.4, 0.4)

plt.savefig("plots/CH7_7.4.6_no_fit.png")
plt.show()
