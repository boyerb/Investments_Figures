import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.regression.rolling import RollingOLS
from tqdm import tqdm

from datasets import FamaFrenchFactors, MomentumPortfolios

# Pull in French Beta Portfolios
df = MomentumPortfolios().df

# Pull in Fama French 5 Factor data
fac = FamaFrenchFactors().df

# Merge factor data to portfolio returns
df = df.merge(fac, on="mdt", how="inner")

# Generate alphas dataframe
alphas = []
for i in range(1, 11):
    df[f"port_{i}"] = df[f"port_{i}"] - df["rf"]
    model = smf.ols(f"port_{i} ~ mkt_rf", df).fit()
    lower_bound = model.conf_int().loc["Intercept"][0]
    upper_bound = model.conf_int().loc["Intercept"][1]
    mean = model.params["Intercept"]
    alphas.append({"port": i, "5%": lower_bound, "50%": mean, "95%": upper_bound})

alphas = pd.DataFrame(alphas)

# Create plot
sns.lineplot(alphas, x="port", y="5%", label="5%", color="k", linestyle="dashed")
sns.lineplot(alphas, x="port", y="50%", label="50%", color="k")
sns.lineplot(alphas, x="port", y="95%", label="95%", color="k", linestyle="dashed")

plt.ylabel("Alpha (bps)")
plt.xlabel("Decile Portfolio")

plt.xticks(range(1, 11))

plt.axhline(y=0, color="k", linestyle="dotted")

plt.savefig("plots/CH12_12.3.1_momentum.png", dpi=300)

start_date = df["mdt"].min()
end_date = df["mdt"].max()
print(f"Date range: {start_date} - {end_date}")
