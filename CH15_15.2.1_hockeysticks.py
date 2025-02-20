import matplotlib.pyplot as plt

nice_blue=(10/255,102/255,194/255)
nice_red=(210/255, 43/255, 43/255)
fig, axes = plt.subplots(2, 2, figsize=(12,7))


figz=[axes[0,0],axes[0,1],axes[1,0],axes[1,1]]


figz[0].plot([90,99.94],[-1,-1],color=nice_blue,lw=2.2)
figz[0].plot([100.02,110],[-.98,9],color=nice_blue,lw=2.2)
figz[0].set_title('Long Call Option Profit')

figz[1].plot([90,99.98],[9,-.98],color=nice_red,lw=2.2)
figz[1].plot([100.06,110],[-1,-1],color=nice_red,lw=2.2)
figz[1].set_title('Long Put Option Profit')

figz[2].plot([90,99.94],[1,1],color=nice_blue,lw=2.2)
figz[2].plot([100.02,110],[.98,-9],color=nice_blue,lw=2.2)
figz[2].set_title('Short Call Option Profit')

figz[3].plot([90,99.98],[-9,.98],color=nice_red,lw=2.2)
figz[3].plot([100.06,110],[1,1],color=nice_red,lw=2.2)
figz[3].set_title('Short Put Option Profit')

for axes in figz:
    axes.spines['right'].set_visible(False)
    axes.spines['top'].set_visible(False)
    axes.spines['bottom'].set_position('zero')
    axes.set_xticks([85, 90, 95, 100, 105, 110, 115])
    axes.set_xlim(80,115)

for a in [0,1]:
    figz[a].set_yticks([-2,0,2,4,6,8,10])

for a in [2,3]:
    figz[a].set_yticks([-10,-8,-6,-4,-2,0,2])

plt.subplots_adjust(hspace=0.4)
plt.subplots_adjust(wspace=0.2)

# plt.tight_layout()
plt.savefig('plots/CH15_15.2.1_hockeysticks.png',dpi=400)
plt.show()

