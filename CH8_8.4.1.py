import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(11, 5))
plt.subplots_adjust(wspace=0.05)

it = axes[0]

it.set_frame_on(False)
it.xaxis.set_visible(False)
it.yaxis.set_visible(False)

it.plot([-4, 10], [4.65, 4.65], color="black")  # horizontal line 1
it.plot([-0.5, 10], [12, 12], color="black")  # top horizontal line
it.plot([-4, 10], [9.3, 9.3], color="black")  # horizontal line 2
it.plot([4.3 + 0.5, 4.3 + 0.5], [0, 12], color="black")
it.plot([-0.5, -0.5], [0, 12], color="black")  # vertical line 2
it.plot([-4, 10], [0, 0], color="black")  # horizontal line 3
it.plot([-4, -4], [0, 9.3], color="black")
it.plot([10, 10], [0, 12], color="black")  # vertical line 3


plt.text(-7.49, 6.9, "Case 1", fontweight="bold", fontsize=12.5)
plt.text(-4.19, 6.9, "Case 4", fontweight="bold", fontsize=12.5)
plt.text(-7.49, 3.8, "Case 3", fontweight="bold", fontsize=12.5)
plt.text(-4.19, 3.8, "Case 2", fontweight="bold", fontsize=12.5)
plt.text(-8.19, 8.5, "$E[r_A]>E[r_p]$", fontweight="bold", fontsize=15)
plt.text(-10.35, 5.9, r"$\beta_{Ap}<1$", fontweight="bold", fontsize=15)
plt.text(-4.89, 8.5, "$E[r_A]<E[r_p]$", fontweight="bold", fontsize=15)
plt.text(-10.35, 2.8, r"$\beta_{Ap}>1$", fontweight="bold", fontsize=15)
# plt.text(-9.3,10,r"$E\:[r_A]-r_f$",fontsize=13,fontweight='bold')
# plt.text(-13.9,5,r"$\beta_{A,p}$",fontsize=13,fontweight='bold',rotation='vertical')
plt.text(
    -3.43,
    5.7,
    "Sign of alpha\n not known \n unless\n calculated",
    ha="center",
    va="center",
    fontsize=11.5,
)
plt.text(-6.74, 5.85, "Alpha must\n be\n positive", ha="center", va="center", fontsize=11.5)
plt.text(-3.54, 2.62, "Alpha must \n be\n negative", ha="center", va="center", fontsize=11.5)
plt.text(
    -6.75,
    2.5,
    "Sign of alpha \n not known\n unless\ncalculated",
    ha="center",
    va="center",
    fontsize=11.5,
)


asdf = plt.gca()
x = np.linspace(0, 7, 1000)
y = [t + 2 for t in x]
plt.plot(x, y, color="black")
plt.scatter([4], [6], s=85, color="black")
plt.plot([3, 5], [6, 6], "--", color="black")
plt.plot([3, 3], [4, 8], "--", color="black")
plt.plot([5, 5], [4, 8], "--", color="black")
plt.scatter([3, 3, 5, 5], [4, 8, 4, 8], s=30, color="black")
plt.text(4.3, 8.4, "Case 3", fontweight="bold", fontsize=12.5)
plt.text(4.3, 3.3, "Case 2", fontweight="bold", fontsize=12.5)
plt.text(2.3, 8.4, "Case 1", fontweight="bold", fontsize=12.5)
plt.text(2.3, 3.3, "Case 4", fontweight="bold", fontsize=12.5)


plt.text(-0.8, 9.7, r"$E\:[r]$", ha="center", va="center", fontsize=18)
plt.text(7.5, 0.4, r"$\sigma$", fontsize=18)


asdf.set_xticks([])
asdf.set_yticks([])
asdf.spines["right"].set_visible(False)
asdf.spines["top"].set_visible(False)
for spine in asdf.spines.values():
    spine.set_linewidth(2.5)


plt.xlim(0, 8)
plt.ylim(1, 10)
asdf.set_aspect("equal")


plt.savefig("plots/CH8_8.4.1.png", dpi=400)
plt.show()
