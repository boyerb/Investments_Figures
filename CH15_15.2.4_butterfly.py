import matplotlib.pyplot as plt


a,b=plt.subplots(1,1,figsize=(8,4))

x=range(70,131)
y=[-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-6.965,-5.965,-4.965,-3.965,-2.965,-1.965,-0.965,0.035,1.035,2.035,3.035,4.035,5.035,6.035,7.035,8.035,9.035,10.035,11.035,12.035,11.035,10.035,9.035,8.035,7.035,6.035,5.035,4.035,3.035,2.035,1.035,0.035,-0.965,-1.965,-2.965,-3.965,-4.965,-5.965,-6.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965,-7.965]
nice_blue=(10/255,102/255,194/255)
plt.plot(x,y,color=nice_blue,lw=2.2)
plt.xticks([70,80,90,100,110,120,130,140])
plt.xlim(60,140)
plt.yticks([-10,-5,0,5,10,15])
b.spines['right'].set_visible(False)
b.spines['top'].set_visible(False)
b.spines['bottom'].set_position('zero')
plt.title('Butterfly Spread')

plt.tight_layout()
plt.savefig('plots/CH15_15.2.4_butterfly.png',dpi=400)
plt.show()