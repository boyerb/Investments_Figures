import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

from datasets import Autoliv

df = Autoliv().df

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="rp", y="rA")

# Add regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(df["rp"], df["rA"])
x = np.array([-0.3, 0.3])  # Create x values for line
y = slope * x + intercept
plt.plot(x, y, color="black", linestyle="-", linewidth=1)

np.random.seed(42)  # for reproducibility
sample_points = df.sample(n=4)

# Add annotations and residual lines
for x_val in [-0.1, 0.1]:
    predicted_y = slope * x_val + intercept
    print(x_val, predicted_y)

    # Draw vertical dotted line
    plt.vlines(
        x=x_val,
        ymin=min(0, predicted_y),
        ymax=max(0, predicted_y),
        colors="k",
        linestyles=":",
        linewidth=1,
    )

    # Draw horizontal dotten line
    plt.hlines(
        y=predicted_y,
        xmin=min(0, x_val),
        xmax=max(0, x_val),
        colors="k",
        linestyles=":",
        linewidth=1,
    )


# Add horizontal and vertical lines at 0
plt.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
plt.axvline(x=0, color="k", linestyle="-", linewidth=0.5)

# Set axis limits
plt.xlim(-0.3, 0.3)
plt.ylim(-0.4, 0.4)

# Labels
plt.ylabel("Return on Autoliv")
plt.xlabel("Return on Portfolio")

# Save and show plot
plt.savefig("plots/CH7_7.4.2_residuals.png")
plt.show()
