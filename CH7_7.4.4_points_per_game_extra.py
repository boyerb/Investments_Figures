import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

# Select specific points to annotate (you might need to adjust these values to match your data)
points_to_annotate = [{"x": 17.8, "y": 0.524}, {"x": 16.2, "y": 0.305}]

for i, point in enumerate(points_to_annotate):
    df = pd.read_csv("data/data_3.csv")

    sns.scatterplot(data=df, x="AVG PPG by TOP SCORER", y="%WINS")

    # Add regression line
    slope, intercept, r_value, p_value, std_err = stats.linregress(
        df["AVG PPG by TOP SCORER"], df["%WINS"]
    )
    x = np.array([15, 20])  # Create x values for line
    y = slope * x + intercept
    plt.plot(x, y, color="black", linestyle="-", linewidth=1)

    plt.xlabel("Average Points per Game by the Top Scorer on the Team")
    plt.ylabel("Percentage of Games Won During Regular Season")

    # Add annotations and residual lines
    x_val = point["x"]
    actual_y = point["y"]
    predicted_y = slope * x_val + intercept
    residual = actual_y - predicted_y

    # Draw vertical dotted line
    plt.vlines(x=x_val, ymin=predicted_y, ymax=actual_y, colors="red", linestyles=":", linewidth=1)

    plt.hlines(y=actual_y, xmin=15, xmax=x_val, colors="red", linestyles=":", linewidth=1)

    plt.hlines(y=predicted_y, xmin=15, xmax=x_val, colors="red", linestyles=":", linewidth=1)

    # Add residual percentage annotation with box
    plt.annotate(
        r"$\ z_t =$" + f"{residual:.2f}",
        xy=(x_val, (actual_y + predicted_y) / 2),
        xytext=(30, 30),
        textcoords="offset points",
        color="k",
        fontsize=10,
        arrowprops=dict(arrowstyle="->", color="k"),
    )

    plt.xlim(15, 20)

    plt.savefig(f"plots/CH7_7.4.4_points_per_game_extra_{i+1}.png")
    plt.show()
