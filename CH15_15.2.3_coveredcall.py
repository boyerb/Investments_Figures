import matplotlib.pyplot as plt

a,b=plt.subplots(1,1,figsize=(8,5))

plt.plot([90,100],[1,1],'--',color=(1,140/255,59/255),lw=2.2)
plt.plot([100,110],[1,-8],'--',color=(1,140/255,59/255),lw=2.2)

plt.plot([90,110],[-9,11],':',color=(10/255,102/255,194/255),lw=2.2)

plt.plot([90,99.95],[-8.5,1.45],color=(143/255,143/255,143/255),lw=2.2)
plt.plot([100.03,110],[1.5,1.5],color=(143/255,143/255,143/255),lw=2.2)
plt.title('Covered Call')

plt.text(110,9.5,'stock profit')
plt.text(110,2.2,'covered call')
plt.text(110,-7.2,'short call profit')

plt.xticks([90, 95, 100, 105, 110, 115])
plt.yticks([-10,-5,0,5,10,15])
plt.xlim(85,115)
b.spines['right'].set_visible(False)
b.spines['top'].set_visible(False)
b.spines['bottom'].set_position('zero')

plt.tight_layout()
plt.savefig('plots/CH15_15.2.3_coveredcall.png',dpi=400)
plt.show()