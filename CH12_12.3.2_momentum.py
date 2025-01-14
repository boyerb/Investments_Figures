import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.regression.rolling import RollingOLS

from datasets import CRSPMonthly, FamaFrenchFactors

# Dates in original textbook
start_date = "1927-01-01"
end_date = "2021-12-31"

# Pull in raw CRSP Monthly dataset
df = CRSPMonthly().df

# Filter to given date range and create month date column
df = df[(df["date"] >= start_date) & (df["date"] <= end_date)].reset_index(drop=True)
df["mdt"] = df["date"].dt.strftime("%Y-%m")

# Calculate log return
df["logret"] = np.log1p(df["ret"])

# Momentum from t-12 to t-1
df["mom"] = df.groupby("permno")["logret"].rolling(11, 11).sum().reset_index(drop=True)
df["mom"] = df.groupby("permno")["mom"].shift(1)  # Lag 1 period

# Filter to stocks greater than 5 dollars per share and where we know the momentum signal
df["prclag"] = df.groupby("permno")["prc"].shift(1)
df = df.query("mom == mom and prclag > 5").reset_index(drop=True)

# Create decile portfolios
df["bin"] = df.groupby("mdt")["mom"].transform(lambda x: pd.qcut(x, 10, labels=False)) + 1

# Create returns dataframe
rets = df.groupby(["mdt", "bin"])["ret"].mean().unstack(level=["bin"]) * 100
rets = rets.rename(columns={col: f"port_{col}" for col in rets.columns})
rets = rets.fillna(0).reset_index()

# Pull in fama french 5 factor data
fac = FamaFrenchFactors().df
fac = fac.rename(columns={"DATE": "mdt", "Mkt-RF": "MKTRf"})
fac["mdt"] = pd.to_datetime(fac["mdt"], format="%Y%m").dt.strftime("%Y-%m")
fac = fac[["mdt", "MKTRf"]]

# Merge returns and factor dataframes
rets = rets.merge(fac, on="mdt", how="left").dropna().reset_index(drop=True)
rets["mdt"] = pd.to_datetime(rets["mdt"]) + pd.offsets.MonthEnd(0)

# Fit the RollingOLS model
for i in [1, 10]:
    rets = sm.add_constant(rets)
    model = RollingOLS(
        endog=rets[f"port_{i}"], exog=rets[["const", "MKTRf"]], window=120  # 10 year window
    ).fit()

    rets[f"alpha_{i}"] = model.params["const"]

# Generate plot
sns.lineplot(rets, x="mdt", y="alpha_1", label="Losers", color="k", linestyle="dashed")
sns.lineplot(rets, x="mdt", y="alpha_10", label="Winners", color="k")

plt.axhline(0, color="k", linestyle="dotted")

plt.ylabel("Alpha (bps)")
plt.xlabel(None)

plt.savefig("plots/CH12_12.3.2_momentum.png")
plt.show()
