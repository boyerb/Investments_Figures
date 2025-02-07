import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import norm

# Set the parameters for the two distributions, A and B
mean = 0.16
std_dev_A = 0.08
std_dev_B = 0.20

# Create an array of x values for both A and B, using the range of the larger variance (B)
x_range = np.linspace(mean - 4 * std_dev_B, mean + 4 * std_dev_B, 1000)

# Compute the PDF for A and B using the same x_range
pdf_A = norm.pdf(x_range, mean, std_dev_A)
pdf_B = norm.pdf(x_range, mean, std_dev_B)

# Create the plot
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Plot the PDF with labels for A and B
plt.plot(x_range, pdf_A, color="black", linewidth=3, label="Investment A")
plt.plot(x_range, pdf_B, color="black", linewidth=6, label="Investment B")

# Add labels directly on the plot near the lines
plt.text(0.25, norm.pdf(0.22, mean, std_dev_A), "Investment A", fontsize=16, color="black")
plt.text(0.40, norm.pdf(0.38, mean, std_dev_B), "Investment B", fontsize=16, color="black")

# Shade the area between 0.1 and 0.4 on distribution B
x_fill_1 = np.linspace(mean - 4 * std_dev_B, -0.09, 100)
pdf_fill_1 = norm.pdf(x_fill_1, mean, std_dev_B)
plt.fill_between(x_fill_1, pdf_fill_1, color="gray", alpha=0.5, label="Shading on B (0.1 and below)")

# Shade the area from 0.4 to the end of the domain for B
x_fill_2 = np.linspace(0.51, mean + 4 * std_dev_B, 100)
pdf_fill_2 = norm.pdf(x_fill_2, mean, std_dev_B)
plt.fill_between(x_fill_2, pdf_fill_2, color="gray", alpha=0.5)

# Set larger font sizes for tick labels
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)

# Show the y-axis at 0
plt.axhline(y=0, color='black', linewidth=1.5)

# Adjust the y-axis limits to ensure y=0 is visible
plt.ylim(bottom=0, top=6)

# Remove grid lines
plt.grid(False)

# Use tight layout to adjust subplot parameters
plt.tight_layout()

# Save the figure with high resolution (300 dpi)
# plt.savefig("plots/CH6_Variance_&_PDF.png", dpi=300)

# Show the plot
plt.show()
