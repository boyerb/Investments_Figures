from matplotlib import pyplot as plt

x=[0.09,0.06,0.13,0.24,0.15,0.17,0.08,0.15,0.09,0.13]
y=[-0.03,-0.01,0.03,0.07,0.02,0.00,0.02,-0.01,0.03,0.05]

plt.scatter(x,y,s=60)
axes=plt.gca()
axes.spines['bottom'].set_position('zero')


axes.spines['right'].set_visible(False)
axes.spines['top'].set_visible(False)

plt.ylim(-0.04,0.08)
plt.xlim(0,0.3)
plt.xticks([0.05,0.1,0.15,0.2,0.25,0.3])
axes.set_xlabel('Volatility',labelpad=80)
plt.ylabel('Expected Return')





plt.tight_layout()
plt.savefig('plots/CH8_8.2.1.png',dpi=400)
plt.show()