# Add arrows pointing from the dashed line's intersection with the top curve

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the utility function: U(W) = 1 - exp(-a * W)
def utility_function(wealth, a):
    return 1 - np.exp(-a * wealth)

# Define the range of wealth and risk aversion parameters
wealth = np.linspace(0, 1.2, 100)
risk_aversion_parameters = [10, 4, 1.75, 0.75, 0.2]

# Initialize the plot
plt.figure(figsize=(8, 6))
colors = sns.color_palette("husl", len(risk_aversion_parameters))

# Plot each utility curve
for i, a in enumerate(risk_aversion_parameters):
    utility = utility_function(wealth, a)
    plt.plot(wealth, utility, label=f'a = {a:.1f}', color=colors[i])

# Add a dashed line going up to the top curve (a=10 in this case)
max_utility = utility_function(0.2, risk_aversion_parameters[0])  # Calculate the utility at wealth=0.2 for the highest curve
plt.axvline(x=0.2, ymin=0, ymax=max_utility / 1.2, color='black', linestyle='--')  # Scale ymax by y-axis limit

# Add arrows pointing left and slightly down, and right and slightly up from the intersection point
plt.annotate('', xy=(0.125, max_utility - 0.13), xytext=(0.19, max_utility),
             arrowprops=dict(arrowstyle='->', color='black'))
plt.annotate('', xy=(0.3, max_utility + 0.1), xytext=(0.21, max_utility + 0.02),
             arrowprops=dict(arrowstyle='->', color='black'))

# Add labels, legend, and annotations
plt.xlabel('Wealth', fontsize=16, fontweight='bold')
plt.ylabel('Utility', fontsize=16, fontweight='bold')
plt.text(0.2, -0.13, 'Initial\nWealth', fontsize=10, ha='center', fontweight='bold')
plt.ylim(0, 1.2)
plt.xlim(0, 1.2)

# Show the plot
plt.tight_layout()
plt.show()


