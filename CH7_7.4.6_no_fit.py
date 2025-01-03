import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Generate sample data
np.random.seed(42)
x = np.random.uniform(-0.1, 0.1, 50)
y = 0.3 / 0.1 * x + np.random.uniform(-0.1, 0.1, 50)

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
