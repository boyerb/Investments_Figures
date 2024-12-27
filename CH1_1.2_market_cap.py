import matplotlib.pyplot as plt
import seaborn as sns

from datasets.crsp_monthly import CRSPMonthly

df = CRSPMonthly().df

df["mkt_cap"] = df["shrout"] * df["prc"]

aggregate = df.groupby("date").agg({"mkt_cap": "sum", "permno": "count"}).reset_index()

aggregate = aggregate[(aggregate["date"] >= "1975-01-01") & (aggregate["date"] <= "2023-12-31")]

aggregate["mkt_cap"] = aggregate["mkt_cap"] / 1e9

sns.lineplot(aggregate, x="date", y="mkt_cap")
plt.title("Total Market Cap of Listed Firms ($Trillions)")
plt.xlabel(None)
plt.ylabel(None)
plt.savefig("plots/CH1_1.2_market_cap.png")
plt.show()

sns.lineplot(aggregate, x="date", y="permno")
plt.title("Number of Listed Firms")
plt.xlabel(None)
plt.ylabel(None)
plt.savefig("plots/CH1_1.2_listed_firms.png")
plt.show()
