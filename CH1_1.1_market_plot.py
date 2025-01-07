import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

data = yf.download(tickers=["SPY"], start="2005-01-01", end="2024-12-31")

data = data.stack(future_stack=True).reset_index()

data["Return"] = data["Close"].pct_change()

data["Gross Return"] = data["Return"] + 1

data["Cummulative Return"] = data["Gross Return"].cumprod()

data["Investment Value"] = 1000 * data["Cummulative Return"]

sns.lineplot(data, x="Date", y="Investment Value")

plt.savefig("plots/CH1_1.1_market_plot.png")
plt.show()
