import matplotlib.pyplot as plt
import numpy as np

asdf=plt.gca()
y=np.linspace(2.1,10.23046,1000)
x=[0.3*(z-6)**2+3 for z in y]
plt.plot(x,y,color=(10/255,102/255,194/255),zorder=1,lw=2)
plt.plot([0,8.3],[4.5,11.41667],color=(10/255,102/255,194/255),lw=1.2,zorder=2)
plt.plot([0,4.2],[8,8],'--',color='black',lw=1,zorder=3)
plt.plot([0,3],[6,6],'--',color='black',lw=1,zorder=4)
plt.plot([0,5.7],[3,3],'--',color='black',lw=1,zorder=5)
plt.scatter([4.2,3,5.7],[8,6,3],color=(10/255,102/255,194/255),s=40,zorder=6)

asdf.set_yticks([3,4.5,6,8], labels=["-0.01","0.04","0.06","0.12"])

plt.text(-.7, 11.5, r"$E\:[r]$", ha='center', va='center', fontsize=12)
plt.text(10.3,.5,r"$\sigma$",fontsize=12)
plt.text(3.3,5.8,"A",fontsize=12)
plt.text(5.9,3.2,"B",fontsize=12)
plt.text(4.4,7.5,'C',fontsize=12)

asdf.set_xticks([])
asdf.spines['right'].set_visible(False)
asdf.spines['top'].set_visible(False)
for spine in asdf.spines.values():
    spine.set_linewidth(2.5)


plt.xlim(0,11)
plt.ylim(1,12)
asdf.set_aspect('equal')

plt.savefig('plots/CH8_hw_a_pg228.png',dpi=400)
plt.show()