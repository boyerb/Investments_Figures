import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.ticker import FuncFormatter

from datasets.ipo_data import IPOData

# Load data
df = IPOData().df

# Clean data
df = df[df["Year"] != "1980-2024"].copy()

df["Year"] = df["Year"].astype("int")

df["Equal-weighted"] = df["Equal-weighted"].str.rstrip("%").astype("float")

df["Amount Left on the Table"] = (
    df["Amount Left on the Table"].str.replace("$", "").str.replace("billion", "").astype("float")
)

df["Number of IPOs"] = df["Number of IPOs"].astype("int")


# Plot
fig, ax1 = plt.subplots()

# Left y-axis
sns.barplot(df, x="Year", y="Number of IPOs", ax=ax1)
ax1.set_ylabel("Number of IPOs (bars)")

# Right y-axis
ax2 = ax1.twinx()

sns.lineplot(data=df["Equal-weighted"], ax=ax2, color="red")
ax2.set_ylabel("Average First Day Return (line)")


def percentage_formatter(x, p):
    return f"{x:.0f}%"


ax2.yaxis.set_major_formatter(FuncFormatter(percentage_formatter))

# X-axis
years = df["Year"].to_list()
xticks = years[::5]
ax1.set_xticks(np.arange(0, len(years), 5))
ax1.set_xticklabels(xticks, rotation=45)
ax1.set_xlabel(None)

plt.savefig("plots/CH3_3.2_ipo_chart_1.png")
plt.show()
