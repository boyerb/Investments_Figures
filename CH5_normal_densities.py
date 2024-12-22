import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style for publication-quality plots (without grid lines)
sns.set(style="white", context="talk")

# Parameters for normal distributions
mean_A = 0.10    # Mean of distribution A
mean_B = 0.30    # Mean of distribution B, higher than A
mean_C = 0.10    # Mean of distribution C, same as A

std_A = 0.20     # Standard deviation of A (and B)
std_B = 0.20     # Same standard deviation for B
std_C = 0.30     # Wider variance (standard deviation) for C

# Generate data
x = np.linspace(-10, 10, 1000)
pdf_A = (1 / (std_A * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_A) / std_A) ** 2)
pdf_B = (1 / (std_B * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_B) / std_B) ** 2)
pdf_C = (1 / (std_C * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean_C) / std_C) ** 2)

# Plot the density functions with thicker lines (linewidth=3.5)
plt.figure(figsize=(10, 6))
plt.plot(x, pdf_A, label="A", color='blue', linewidth=6)
plt.plot(x, pdf_B, label="B", color='green', linewidth=6)
plt.plot(x, pdf_C, label="C", color='red', linewidth=6, linestyle='--')  # Dashed line for C

# Adding labels, legend, and title
plt.xlabel("Return", fontsize=26)
plt.ylabel("Density", fontsize=26)
plt.legend(loc="upper right", fontsize=22)

# Adjust the x-axis range for a better view
plt.xlim(-1, 1)  # Focusing on the range where most of the data lies

# Set larger font sizes for tick labels
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)

# Remove grid lines
plt.grid(False)

# Show the plot
plt.tight_layout()
plt.savefig('plots/CH4_normal_distributions_plot.png', dpi=300)  # Save with high resolution (300 dpi)
plt.show()
