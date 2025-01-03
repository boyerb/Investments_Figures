import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

data = yf.download(["GE", "SPY"], "2023-08-01", "2023-08-30")

data = data.stack(future_stack=True).reset_index()

data = data.sort_values(by=["Ticker", "Date"]).reset_index(drop=True)

data["Return"] = data.groupby("Ticker")["Close"].pct_change()

x = data[data["Ticker"] == "SPY"]["Return"].to_list()
y = data[data["Ticker"] == "GE"]["Return"].to_list()

sns.scatterplot(x=x, y=y)

plt.xlabel("Return on S&P500")
plt.ylabel("Return on GE")

plt.savefig("plots/CH7_HW_7.6.2.png")
plt.tight_layout()
plt.show()
