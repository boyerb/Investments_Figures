import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import minimize

# -------------------------------------------------- Inputs --------------------------------------------------
# Tickers
tickers = ["IBM", "COG", "AAPL"]

# Covariance matrix
covariance_matrix = np.array(
    [[0.0016, -0.0003, 0.0019], [-0.0003, 0.0100, -0.0026], [0.0019, -0.0026, 0.0071]]
)

# Expected returns
expected_returns = np.array([0.0056, 0.0279, 0.0272])

# Risk free rate
rf = 0.0015


# -------------------------------------------------- Functions --------------------------------------------------
def portfolio_return(weights: np.array, expected_returns: np.array):
    return weights.T @ expected_returns


def portfolio_volatility(weights: np.array, covariance_matrix: np.array):
    return np.sqrt(weights.T @ covariance_matrix @ weights)


def portfolio_sharpe(
    weights: np.array,
    expected_returns: np.array,
    covariance_matrix: np.array,
    rf: float,
):
    port_ret = portfolio_return(weights, expected_returns)
    port_vol = portfolio_volatility(weights, covariance_matrix)

    return (port_ret - rf) / port_vol


def negative_portfolio_sharpe(
    weights: np.array,
    expected_returns: np.array,
    covariance_matrix: np.array,
    rf: float,
):
    return -portfolio_sharpe(weights, expected_returns, covariance_matrix, rf)


# -------------------------------------------------- MVE Portfolios + Efficient Frontier --------------------------------------------------
# Mean Variance Efficient function
def mve_portfolio(target_return, expected_returns, covariance_matrix):
    constraints = (
        {"type": "eq", "fun": lambda w: w.T @ expected_returns - target_return},
        {"type": "eq", "fun": lambda w: np.sum(w) - 1},
    )

    initial_weights = np.ones(3) / 3

    result = minimize(
        fun=portfolio_volatility,
        x0=initial_weights,
        args=(covariance_matrix),
        method="SLSQP",
        constraints=constraints,
    )

    return result.x


# Target returns
n_points = 10
target_returns = np.linspace(
    -0.03, -0.03 + (10 - 1) * 0.015, n_points
)  # start at -.03 and increment by .015 n_points times

# Generate MVE portfolios
mve_portfolios = [
    mve_portfolio(target, expected_returns, covariance_matrix) for target in target_returns
]

# MVE portfolio heuristics
returns = [portfolio_return(w, expected_returns) for w in mve_portfolios]
volatilities = [portfolio_volatility(w, covariance_matrix) for w in mve_portfolios]
sharpes = [portfolio_sharpe(w, expected_returns, covariance_matrix, rf) for w in mve_portfolios]

# Portfolios dataframe
portfolios = pd.DataFrame()
portfolios["Name"] = [f"Portfolio {x+1}" for x in range(len(mve_portfolios))]

# Weight columns
for index in range(len(tickers)):
    portfolios[tickers[index]] = np.array([row[index] for row in mve_portfolios])

# Heuristic columns
portfolios["expected_return"] = returns
portfolios["volatility"] = volatilities
portfolios["sharpe_ratio"] = sharpes

# Table
print("-" * 50 + " MVE Portfolios " + "-" * 50)
print(portfolios)

# Chart
plt.plot(volatilities, returns, label="Efficient Frontier", marker="o", zorder=1)
plt.xlim(0)
plt.axhline(y=0, color="k")
plt.xlabel("Volatility")
plt.ylabel("Expected Return")
plt.title("Efficient Frontier")
plt.legend()
plt.savefig("plots/CH8_8.2.4_efficient_frontier.png", dpi=300)

# -------------------------------------------------- Optimal Portfoio --------------------------------------------------
# Constraints
constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}  # weights sum to 1

# Optimization
initial_weights = np.ones(3) / 3
result = minimize(
    fun=negative_portfolio_sharpe,
    x0=initial_weights,
    args=(expected_returns, covariance_matrix, rf),
    method="SLSQP",
    constraints=constraints,
)

# Results
optimal_weights = result.x
optimal_return = portfolio_return(optimal_weights, expected_returns)
optimal_volatility = portfolio_volatility(optimal_weights, covariance_matrix)
optimal_sharpe = portfolio_sharpe(optimal_weights, expected_returns, covariance_matrix, rf)

# Print optimal results
print("-" * 50 + " Optimal Portfolio " + "-" * 50)
print(", ".join([f"{ticker}: {weight:.4f}" for ticker, weight in zip(tickers, optimal_weights)]))
print(f"Sharpe: {optimal_sharpe:.4f}")

# -------------------------------------------------- Capital Allocation Line --------------------------------------------------


def cal(x: float, sharpe: float, rf: float) -> float:
    return x * sharpe + rf


x = 0, max(portfolios["volatility"])
y = [cal(x_, optimal_sharpe, rf) for x_ in x]

plt.plot(x, y, label="Capital Allocation Line", zorder=2)
plt.scatter(
    optimal_volatility,
    optimal_return,
    color="r",
    marker="*",
    s=200,
    label="Optimal Portfolio",
    zorder=3,
)
plt.legend()
plt.savefig("plots/CH8_8.2.5_efficient_frontier.png", dpi=300)

# -------------------------------------------------- Client Portfolio --------------------------------------------------
client_target_return = 0.03
scale = (client_target_return - rf) / (optimal_return - rf)
client_weights = optimal_weights * scale
rf_weight = 1 - sum(client_weights)
client_return = portfolio_return(client_weights, expected_returns) + rf * rf_weight
client_volatility = portfolio_volatility(client_weights, covariance_matrix)

plt.scatter(
    client_volatility,
    client_target_return,
    label="Client Portfolio",
    color="green",
    s=100,
    zorder=3,
)
plt.legend()
plt.savefig("plots/CH8_8.2.6_efficient_frontier.png", dpi=300)

# -------------------------------------------------- Hedge Fund Portfolio --------------------------------------------------
z = stats.norm.ppf(0.95)
fund_var = -0.10
scale = (fund_var - rf) / (optimal_return - rf - z * optimal_volatility)
fund_weights = scale * optimal_weights
rf_weight = 1 - sum(fund_weights)
fund_return = portfolio_return(fund_weights, expected_returns) + rf * rf_weight
fund_volatility = portfolio_volatility(fund_weights, covariance_matrix)

plt.scatter(fund_volatility, fund_return, label="Fund Portfolio", color="black", s=100, zorder=3)
plt.legend()
plt.savefig("plots/CH8_8.2.7_efficient_frontier.png", dpi=300)
