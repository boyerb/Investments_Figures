import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2,figsize=(10,4))


it=axes[0]

it.set_frame_on(False)
it.xaxis.set_visible(False)
it.yaxis.set_visible(False)

it.plot([0,10],[4.65,4.65],color='black')
it.plot([.6,10],[10,10],color='black')
it.plot([0,10],[9.3,9.3],color='black')
it.plot([4.7+.6,4.7+.6],[0,10],color='black')
it.plot([.6,.6],[0,10],color='black')
it.plot([0,10],[0,0],color='black')
it.plot([0,0],[0,9.3],color='black')
it.plot([10,10],[0,10],color='black')



plt.text(-11.1,8,'Case 1',fontweight='bold',fontsize=10)
plt.text(-6.65,8,'Case 2',fontweight='bold',fontsize=10)
plt.text(-11.1,4.1,'Case 3',fontweight='bold',fontsize=10)
plt.text(-6.65,4.1,'Case 4',fontweight='bold',fontsize=10)
plt.text(-10.5,9.17,'+',fontweight='bold',fontsize=10)
plt.text(-12.93,7,'+',fontweight='bold',fontsize=10)
plt.text(-6,9.37,'_',fontweight='bold',fontsize=10)
plt.text(-12.85,3.45,'_',fontweight='bold',fontsize=10)
plt.text(-9.3,10,r"$E\:[r_A]-r_f$",fontsize=13,fontweight='bold')
plt.text(-13.9,5,r"$\beta_{A,p}$",fontsize=13,fontweight='bold',rotation='vertical')
plt.text(-10.25, 6.7, "Sign of alpha not\nknown unless\ncalculated", ha='center', va='center')
plt.text(-5.85,6.92,'Alpha must be\nnegative',ha='center',va='center')
plt.text(-10.25,3.02,'Alpha must be\npositive',ha='center',va='center')
plt.text(-5.85, 2.8, "Sign of alpha not\nknown unless\ncalculated", ha='center', va='center')



asdf=plt.gca()
x=np.linspace(0,7,1000)
y=[t+2 for t in x]
plt.plot(x,y,color='black')
plt.scatter([4],[6],s=85,color='black')
plt.plot([3,5],[6,6],'--',color='black')
plt.plot([3,3],[4,8],'--',color='black')
plt.plot([5,5],[4,8],'--',color='black')
plt.scatter([3,3,5,5],[4,8,4,8],s=30,color='black')
plt.text(4.3,8.4,"Case 1")
plt.text(4.3,3.3,"Case 2")
plt.text(2.3,8.4,"Case 3")
plt.text(2.3,3.3,"Case 4")



plt.text(-.7, 9.7, r"$E\:[r]$", ha='center', va='center', fontsize=12)
plt.text(7.5,.5,r"$\sigma$",fontsize=12)




asdf.set_xticks([])
asdf.set_yticks([])
asdf.spines['right'].set_visible(False)
asdf.spines['top'].set_visible(False)
for spine in asdf.spines.values():
    spine.set_linewidth(2.5)


plt.xlim(0,8)
plt.ylim(1,10)
asdf.set_aspect('equal')


plt.savefig('plots/CH8_8.4.1.png',dpi=400)
plt.show()