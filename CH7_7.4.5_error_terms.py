import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from datasets import Autoliv

df = Autoliv().df

x = df["rp"]
y = df["rA"]

params_list = [
    {"a": -0.003, "b": 1.10},
    {"a": 0.2, "b": 1.10},
    {"a": -0.003, "b": 4},
]

x_limits = (-0.15, 0.15)
y_limits = (-0.4, 0.4)

fig, axes = plt.subplots(1, 3, figsize=(15, 4), sharey=True)

for i, params in enumerate(params_list):
    sns.scatterplot(x=x, y=y, ax=axes[i])

    axes[i].plot(x, params["b"] * x + params["a"], color="black")  # Trend line

    axes[i].set_xlim(x_limits)
    axes[i].set_ylim(y_limits)

    axes[i].set_xlabel("Return on Portfolio")
    axes[i].set_ylabel("Return on Autoliv")

axes[0].set_title("Panel A: a = -0.003  b = 1.10\nCorrect.\n$\overline{z} = 0$, $Cov(r_A, z) = 0$")
axes[1].set_title(
    "Panel B: a = 0.20  b = 1.10\nLine shifted too high.\n$\overline{z} > 0$, $Cov(r_A, z) = 0$"
)
axes[2].set_title(
    "Panel C: a = -0.003  b = 4\nLine tilted counter-clockwise.\n$\overline{z} = 0$, $Cov(r_A, z) < 0$"
)

plt.tight_layout()

plt.savefig("plots/CH7_7.4.5_error_terms.png")
plt.show()
