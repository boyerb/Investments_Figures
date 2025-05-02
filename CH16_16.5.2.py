import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 1, figsize=(8,4))
yeet=plt.gca()

x=[np.linspace(1.51795,28,1000),np.linspace(0,13.45,1000),np.linspace(0,26.8,1000)]
funky=[lambda n: 7*np.log10(n-1)+2,lambda n: 0.8*1.8**(0.5*n-2)-0.246194,lambda n: 2.5**(0.2*n-2.5)-0.16]

plt.plot([6.7546,6.7546],[funky[0](6.7546),funky[1](6.7546)],color='black',lw=1.2,linestyle=(0,(3,3)))
plt.plot([13.88063,13.88063],[funky[0](13.88063),funky[2](13.88063)],color='black',lw=1.2,linestyle=(0,(3,3)))

plt.plot(x[0],[funky[0](x) for x in x[0]],color='black',lw=2)
plt.plot(x[1],[funky[1](x) for x in x[1]],color='black',lw=2)
plt.plot(x[2],[funky[2](x) for x in x[2]],color='black',lw=2,linestyle=(0,(4,4)))

yeet.spines['right'].set_visible(False)
yeet.spines['top'].set_visible(False)
yeet.set_xticks([6.7546,13.88063],labels=[r"$I_B$",r"$I_E$"])
yeet.set_yticks([])
plt.text(23.5,-.8,"Amount of Information",fontsize=10)
plt.text(-3.8,15,"Costs and",fontsize=10)
plt.text(-3.25,14.2,"Benefits",fontsize=10)
plt.text(10.6,13.9,"Cost of Additional")
plt.text(9.8,13.1,"Information (Beginner)")
plt.text(24.17,14.8,"Cost of Additional")
plt.text(23.8,14,"Information (Expert)")
plt.text(28.5,12.2,"Benefit of Additional")
plt.text(28.5,11.4,"Information")

plt.ylim(0,16)
plt.xlim(0,32)

plt.tight_layout()
plt.savefig('plots/CH16_16.5.2.png',dpi=400)
plt.show()

