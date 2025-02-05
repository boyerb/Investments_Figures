import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.regression.rolling import RollingOLS

from datasets import FamaFrenchFactors, MomentumPortfolios

# Pull in French Portfolios
df = MomentumPortfolios().df

# Pull in Fama French 5 Factor data
fac = FamaFrenchFactors().df

# Merge factor data to portfolio returns
df = df.merge(fac, on="mdt", how="inner")
df["date"] = pd.to_datetime(df["mdt"]) + pd.offsets.MonthEnd(0)

# Fit the RollingOLS model
for i in [1, 10]:
    df[f"port_{i}"] = df[f"port_{i}"] - df["rf"]
    df = sm.add_constant(df)
    model = RollingOLS(
        endog=df[f"port_{i}"], exog=df[["const", "mkt_rf"]], window=120  # 10 year window
    ).fit()

    df[f"alpha_{i}"] = model.params["const"]

# Generate plot
sns.lineplot(df, x="date", y="alpha_1", label="Losers", color="k", linestyle="dashed")
sns.lineplot(df, x="date", y="alpha_10", label="Winners", color="k")
plt.axhline(0, color="k", linestyle="dotted")
plt.ylabel("Alpha (bps)")
plt.xlabel(None)
plt.savefig("plots/CH12_12.3.2_momemtum.png", dpi=300)
