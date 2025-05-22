import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_parquet("data/msf.parquet")
df = df[df["date"] <= "2020-12-31"]
df = df[df["date"] >= "2016-01-01"]
df = df[df["prc"] >= 5]

dupes = df[df.duplicated(subset=["date", "permno"], keep=False)]
print(f"Number of duplicate rows: {len(dupes)}")
print(dupes.sort_values(["permno", "date"]).head(10))
jan_2016 = df[(df["date"].dt.year == 2016) & (df["date"].dt.month == 1)]

# Get unique permno?s
unique_permnos = jan_2016["permno"].unique()

# Randomly shuffle permnos and pick first 100
np.random.seed(56)
# 49, 52
selected_permnos = np.random.permutation(unique_permnos)[:100]

# Initialize list to store standard deviations
portfolio_stds = []

# Build portfolio incrementally
for n in range(1, 101):
    current_permnos = selected_permnos[:n]
    subset = df[df["permno"].isin(current_permnos)].copy()

    # Pivot so each column is a stock, index is date
    pivot = subset.pivot(index="date", columns="permno", values="ret")

    # Drop rows with any missing data
    pivot = pivot.fillna(0)

    # Equally weighted portfolio
    portfolio_ret = pivot.mean(axis=1)

    # Compute standard deviation and save
    std = portfolio_ret.std() * np.sqrt(12)
    portfolio_stds.append(std)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(range(1, 101), portfolio_stds, color="black", linewidth=3)
plt.xlabel("Number of Stocks in Portfolio", fontsize=17)
plt.ylabel("Portfolio Return Standard Deviation", fontsize=17)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
# plt.title('Diversification Effect: Std. Dev. vs Portfolio Size', fontsize=16)
# plt.grid(True)
plt.savefig("plots/CH9_real_diver.png", dpi=300)
plt.show()
print("hold")
