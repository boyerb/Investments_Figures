from matplotlib import pyplot as plt

y = [0.10, 0.08, 0.09, 0.10, 0.10, 0.12, 0.09, 0.17, 0.07, 0.09]
x = [0.17, 0.24, 0.66, 0.38, 0.68, 0.66, 0.42, 0.57, 0.60, 0.26]

plt.scatter(x, y, s=60, color="k")
axes = plt.gca()
axes.spines["bottom"].set_position("zero")


axes.spines["right"].set_visible(False)
axes.spines["top"].set_visible(False)

plt.ylim(0, 0.2)
plt.xlim(0, 0.7)
# plt.xticks([0.05,0.1,0.15,0.2,0.25,0.3])
axes.set_xlabel("Volatility", labelpad=4)
plt.ylabel("Expected Return")


plt.savefig("plots/CH8_8.2.1.png")
plt.show()
