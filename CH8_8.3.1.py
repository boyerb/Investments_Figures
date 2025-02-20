import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

x = np.linspace(1.05, 2.95, 1000)
y=[-2*(t-1)*(t-3) for t in x]
listy=['Panel A','Panel B','Panel C']
x_values=[1.4,2.2,2]

for i, ax in enumerate(axes):
    ax.plot(x, y, color='black',lw=2)
    if i == 0:
        ax.plot([x_values[i],x_values[i]],[0,1.28], color='black', linestyle=(0,(5,5)),lw=1)
        ax.plot([1, 1.8], [0.32, 2.24], color='red', lw=2)

    elif i == 1:
        ax.plot([x_values[i],x_values[i]],[0,1.92], color='black', linestyle=(0, (5, 5)),lw=1)
        ax.plot([1.498, 2.925], [2.4816,1.34], color='red', lw=2)

    elif i == 2:
        ax.plot([x_values[i],x_values[i]],[0,2], color='black', linestyle=(0, (5, 5)),lw=1)
        ax.plot([1,3],[2,2], color='red', lw=2)


    ax.text(3.3, -0.13, r"$W_i$", ha='center', va='center', fontsize=10)

    ax.set_xlabel(listy[i])
    ax.set_ylabel("Sharpe Ratio")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlim(0.5,3.5)
    ax.set_ylim(0,2.5)
    ax.set_xticks([x_values[i]], labels=[r"$w_i^*$"])
    ax.set_yticks([])


plt.tight_layout()


plt.savefig('plots/CH8_8.3.1.png',dpi=400)
plt.show()