import matplotlib.pyplot as plt
import numpy as np

asdf=plt.gca()
y=np.linspace(2.1,10.23046,1000)
x=[0.3*(z-6)**2+3 for z in y]
plt.plot(x,y,color='black',zorder=1,lw=2)
plt.plot([0,8.3],[4.5,11.41667],color='black',lw=1.2,zorder=2)



plt.scatter([4.2],[8],color='black',s=40,zorder=6)



plt.text(-.7, 11.5, r"$E\:[r]$", ha='center', va='center', fontsize=12)
plt.text(10.3,.5,r"$\sigma$",fontsize=12)
plt.text(5.9,10.9,"Line A",fontsize=12)
plt.text(5.9,3.2,"Curve B",fontsize=12)
plt.text(4.4,7.5,'Point C',fontsize=12)

asdf.set_xticks([])
asdf.set_yticks([])
asdf.spines['right'].set_visible(False)
asdf.spines['top'].set_visible(False)
for spine in asdf.spines.values():
    spine.set_linewidth(2.5)


plt.xlim(0,11)
plt.ylim(1,12)
asdf.set_aspect('equal')

plt.savefig('plots/CH8_hw_b_pg228.png',dpi=400)
plt.show()