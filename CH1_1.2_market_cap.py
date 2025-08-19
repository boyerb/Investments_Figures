import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None)
import matplotlib.dates as mdates
import numpy as np

from datasets.crsp_monthly import CRSPMonthly

df = pd.read_parquet("datasets/msf.parquet")
# df = CRSPMonthly().df
# df = pd.read_csv("datasets/crsp_monthly_manual.csv")

print(df)

df = df[df["shrcd"].isin([10, 11])]

df["mkt_cap"] = df["shrout"] * np.abs(df["prc"])

aggregate = df.groupby("date").agg({"mkt_cap": "sum", "permno": "count"}).reset_index()

aggregate = aggregate[(aggregate["date"] >= "1975-01-01")]

aggregate["mkt_cap"] = aggregate["mkt_cap"] / 1e9

# Set a clean, minimalist style
# sns.set_style("whitegrid")

# --- First Plot: Total Market Cap ---
plt.figure(figsize=(10, 6))
sns.lineplot(data=aggregate, x="date", y="mkt_cap", color="black", linewidth=2)
# plt.title("Total Market Cap of Listed Firms ($Trillions)")
plt.xlabel(None)
plt.ylabel(None)

# Format x-axis: ticks every 5 years, fixed range, horizontal labels
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator(5))  # Every 5 years
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plt.xlim(pd.to_datetime("1975"), pd.to_datetime("2030"))
plt.xticks(rotation=0)

# Make ticks bigger
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.tight_layout()
plt.savefig("plots/CH1_1.2_market_cap.png")
plt.show()

# --- Second Plot: Number of Listed Firms ---
plt.figure(figsize=(10, 6))
sns.lineplot(data=aggregate, x="date", y="permno", color="black", linewidth=2)
# plt.title("Number of Listed Firms")
plt.xlabel(None)
plt.ylabel(None)

# Format x-axis: ticks every 5 years, fixed range, horizontal labels
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.YearLocator(5))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
plt.xlim(pd.to_datetime("1975"), pd.to_datetime("2030"))
plt.xticks(rotation=0)

# Make ticks bigger
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.tight_layout()
plt.savefig("plots/CH1_1.2_listed_firms.png")
plt.show()
