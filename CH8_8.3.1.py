import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(11, 9.5))  # 2 rows, 2 columns
axes = axes.flatten()  # Flatten to make indexing easier

x = np.linspace(1.05, 2.95, 1000)
y = [-2 * (t - 1) * (t - 3) for t in x]
panel_titles = ["Panel\u2003A", "Panel\u2003B", "Panel\u2003C", "Panel\u2003D"]
x_values = [1.4, 2.2, 2, 1.364]  # x positions for vertical lines
descriptions = ["Keep Climbing!", "Reverse Course!", "Just Right", "Over Shooting"]
for i, ax in enumerate(axes):
    ax.plot(x, y, color="black", lw=3)

    if i == 0:  # Panel A
        x_vert = x_values[i]  # keep this unchanged
        y_top = -2 * (x_vert - 1) * (x_vert - 3)
        ax.plot([x_vert, x_vert], [0, y_top], color="black", linestyle=(0, (2, 2)), lw=2)
        ax.plot([1, 1.8], [0.32, 2.24], color="red", lw=3)

    elif i == 1:  # Panel B
        x_vert = x_values[i]
        y_top = -2 * (x_vert - 1) * (x_vert - 3)
        ax.plot([x_vert, x_vert], [0, y_top], color="black", linestyle=(0, (2, 2)), lw=2)
        ax.plot([1.498, 2.925], [2.4816, 1.34], color="red", lw=3)

    elif i == 2:  # Panel C
        x_vert = x_values[i]
        y_top = -2 * (x_vert - 1) * (x_vert - 3)
        ax.plot([x_vert, x_vert], [0, y_top], color="black", linestyle=(0, (2, 2)), lw=2)
        ax.plot([1, 3], [2, 2], color="red", lw=3)

    elif i == 3:  # Panel D (new): overshoots the hill
        x_vert = x_values[i]
        y_top = -2 * (x_vert - 1) * (x_vert - 3)
        ax.plot([1.364, 1.364], [0, 1.191], color="black", linestyle=(0, (2, 2)), lw=2)
        ax.plot([0.9, 2.8], [0.8, 2.4], color="red", lw=3)

    ax.text(3.3, -0.13, r"$w_\Omega$", ha="center", va="center", fontsize=22)
    ax.set_xlabel(f"${{\\mathbf{{{panel_titles[i]}}}}}$", fontsize=20)
    ax.text(2, -0.8, descriptions[i], ha="center", va="center", fontsize=18)
    ax.set_ylabel("Sharpe Ratio", fontsize=20)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)  # Thicker axes
    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0, 2.5)
    ax.set_xticks([x_values[i]], labels=[r"$w_\Omega^*$"], fontsize=22)
    ax.set_yticks([])

plt.tight_layout(h_pad=3, w_pad=3, pad=1.0)
plt.savefig("plots/CH8_8.3.1_four_panels.png", dpi=400)
plt.show()
