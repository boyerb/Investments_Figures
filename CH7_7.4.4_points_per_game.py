import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

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

plt.savefig("plots/CH7_7.4.4_points_per_game.png")
plt.show()
