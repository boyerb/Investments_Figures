import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

df = pd.read_csv("data/data_2.csv", index_col=0)

plt.figure(figsize=(8, 6))

sns.scatterplot(data=df, x="rp", y="rA")

# Add regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(df["rp"], df["rA"])
x = np.array([-0.3, 0.3])  # Create x values for line
y = slope * x + intercept
plt.plot(x, y, color="black", linestyle="-", linewidth=1)

# Add horizontal and vertical lines at 0
plt.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
plt.axvline(x=0, color="k", linestyle="-", linewidth=0.5)

# Select specific points to annotate (you might need to adjust these values to match your data)
points_to_annotate = [
    {"x": 0.102, "y": 0.304},  # Approximate coordinates from the image
]

# Add annotations and residual lines
for point in points_to_annotate:
    x_val = point["x"]
    actual_y = point["y"]
    predicted_y = slope * x_val + intercept
    residual = actual_y - predicted_y
    residual_pct = residual * 100

    # Draw vertical dotted line
    plt.vlines(x=x_val, ymin=0, ymax=actual_y, colors="red", linestyles=":", linewidth=1)

    plt.hlines(y=actual_y, xmin=0, xmax=x_val, colors="red", linestyles=":", linewidth=1)

    plt.hlines(y=predicted_y, xmin=0, xmax=x_val, colors="red", linestyles=":", linewidth=1)

    # Add residual percentage annotation with box
    plt.annotate(
        f"{residual_pct:.2f}% residual",
        xy=(x_val, (actual_y + predicted_y) / 2),
        xytext=(30, 30),
        textcoords="offset points",
        color="red",
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="red"),
    )

    # Add actual_y val annotation
    plt.annotate(
        f"{actual_y*100:.2f}%",
        xy=(0, actual_y),
        xytext=(-100, -10),
        textcoords="offset points",
        color="red",
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="red"),
    )

    # Add predicted_y val annotation
    plt.annotate(
        f"{predicted_y*100:.2f}%",
        xy=(0, predicted_y),
        xytext=(-100, 10),
        textcoords="offset points",
        color="red",
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="red"),
    )

    # Add predicted_y val annotation
    plt.annotate(
        f"{x_val*100:.2f}%",
        xy=(x_val, 0),
        xytext=(0, -50),
        textcoords="offset points",
        color="red",
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="red"),
    )

# Set axis limits
plt.xlim(-0.3, 0.3)
plt.ylim(-0.4, 0.4)

# Labels
plt.ylabel("Return on Autoliv")
plt.xlabel("Return on Portfolio")

plt.savefig("plots/CH7_7.4.3_residuals.png")
plt.show()
