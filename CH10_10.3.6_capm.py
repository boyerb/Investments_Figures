import matplotlib.pyplot as plt
import numpy as np


yeet=plt.gca()
y=np.linspace(1.9,4.9,1000)
x=[(i-3)**2+1.5 for i in y]
dot_x=[1.66,4,4,5.45,5,1.2]
dot_y=[3.4,3.8,2.87,1.325,3.8,4.5]
plt.plot(x,y,color='black')
plt.plot([0,3.34],[1.325,5.5], color='black')
plt.plot([0,6],[1.325,1.325],linestyle='--',color='black',lw=1)
plt.plot([0,6],[3.8,3.8],linestyle='--',color='black',lw=1)
plt.plot([4,4],[0,5.5],linestyle='--',color='black',lw=1)
for spine in yeet.spines.values():
    spine.set_linewidth(2.5)
plt.scatter(dot_x,dot_y,s=30,color='black')
yeet.set_xticks([])
yeet.set_yticks([])
yeet.spines['right'].set_visible(False)
yeet.spines['top'].set_visible(False)
plt.text(1.71,3.14,"market")
plt.text(5.8,-.3,r"$\sigma$")
plt.text(5.53,1.03,r"$D$")
plt.text(5.1,3.5,r"$B$")
plt.text(4.08,2.53,r"$C$")
plt.text(4.1,3.5,r"$A$")
plt.text(1.3,4.2,r"$E$")
plt.text(-.3, 5.7, r"$E\:[r]$", ha='center', va='center', fontsize=10)

plt.xlim(0,6)
plt.ylim(0,6)







plt.savefig('plots/CH10_10.3.6_capm.png',dpi=400)
plt.show()
