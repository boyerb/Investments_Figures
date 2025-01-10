import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from datasets import Autoliv

df = Autoliv().df

sns.scatterplot(data=df, x="rp", y="rA")

plt.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
plt.axvline(x=0, color="k", linestyle="-", linewidth=0.5)

plt.xlim(-0.3, 0.3)
plt.ylim(-0.4, 0.4)

plt.ylabel("Return on Autoliv")
plt.xlabel("Return on Portfolio")

plt.savefig("plots/CH7_7.4.1_scatter.png")
plt.show()
