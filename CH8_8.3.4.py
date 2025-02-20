import matplotlib.pyplot as plt
import numpy as np

asdf=plt.gca()
x=np.linspace(0,7,1000)
y=[t+2 for t in x]
plt.plot(x,y,color='black')
plt.scatter([4],[6],s=40,color='black')
plt.plot([2,6],[6,6],'--',color='black',lw=1)
plt.plot([4,4],[4,8],'--',color='black',lw=1)
plt.arrow(4, 8,0, 0, head_width=.3, head_length=.2, fc='black', ec='black')
plt.arrow(6, 6,0.01, 0, head_width=.3, head_length=.2, fc='black', ec='black')
plt.arrow(4, 4,0, -0.01, head_width=.3, head_length=.2, fc='black', ec='black')
plt.arrow(2, 6,-.01, 0, head_width=.3, head_length=.2, fc='black', ec='black')
plt.text(-.7, 9.7, r"$E\:[r]$", ha='center', va='center', fontsize=10)
plt.text(7.5,.5,r"$\sigma$")
plt.text(2.8,8.5,r"$E\:[r_A]-r_f>0$")
plt.text(2.8,3.3,r"$E\:[r_A]-r_f<0$")
plt.text(1.1,5.2,r"$\beta_{A,p}<0$")
plt.text(5.5,5.2,r"$\beta_{A,p}>0$")
asdf.set_xticks([])
asdf.set_yticks([])
asdf.spines['right'].set_visible(False)
asdf.spines['top'].set_visible(False)
for spine in asdf.spines.values():
    spine.set_linewidth(2.5)


plt.xlim(0,8)
plt.ylim(1,10)
asdf.set_aspect('equal')

plt.tight_layout()
plt.savefig('plots/CH8_8.3.4.png',dpi=400)
plt.show()