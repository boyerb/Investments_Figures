import matplotlib.pyplot as plt

a,b=plt.subplots(1,1,figsize=(8,4))
nice_blue=(10/255,102/255,194/255)
plt.plot([90,100],[8,-2],color=nice_blue,lw=2.2)
plt.plot([100,110],[-2,8],color=nice_blue,lw=2.2)
plt.title("Straddle")
b.spines['right'].set_visible(False)
b.spines['top'].set_visible(False)
plt.xticks([90, 95, 100, 105, 110, 115])
plt.xlim(85,115)
b.spines['bottom'].set_position('zero')

plt.tight_layout()
plt.savefig('plots/CH15_15.2.2_straddle.png',dpi=400)
plt.show()
