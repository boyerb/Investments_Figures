import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from datasets import CH7_731

df = CH7_731().df

sns.scatterplot(data=df, x="Portfolio", y="stock A")

plt.axhline(y=0, color="k", linestyle="-", linewidth=0.5)
plt.axvline(x=0, color="k", linestyle="-", linewidth=0.5)

plt.xlim(-0.6, 0.8)
plt.ylim(-0.6, 1)

plt.ylabel("Stock A")
plt.xlabel("Original Portfolio")

plt.savefig("plots/CH7_7.3.1_scatter.png")
plt.show()
