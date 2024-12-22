import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

# Set the parameters for the normal distribution
mean = 0.16
std_dev = 0.20

# Create an array of x values
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)

# Compute the PDF
pdf = norm.pdf(x, mean, std_dev)

# Create the plot
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Plot the PDF
plt.plot(x, pdf, color='black', linewidth=6)

# Shade the area between 0.10 and 0.40
x_fill = np.linspace(0.10, 0.40, 100)
pdf_fill = norm.pdf(x_fill, mean, std_dev)
plt.fill_between(x_fill, pdf_fill, color='gray', alpha=0.5)

# Add labels
plt.xlabel('Return', fontsize=26)
plt.ylabel('Probability Density', fontsize=26)

# Set larger font sizes for tick labels
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)

# Remove grid lines
plt.grid(False)

# Use tight layout to adjust subplot parameters
plt.tight_layout()

# Save the figure with high resolution (300 dpi)
plt.savefig('plots/CH4_normalcdf3.png', dpi=300)

# Show the plot
plt.show()
