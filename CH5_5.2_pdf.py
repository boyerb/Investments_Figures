from scipy.stats import norm
from matplotlib import pyplot as plt
import numpy as np

x=np.linspace(-1,1,1000)
y = norm.pdf(x, 0.08, 0.2)

plt.plot(x,y)

plt.ylim(0,2.5)
plt.fill_between(x,y,where=(x>0.5),color='grey')
plt.axvline(0, color="black", linewidth=0.8)

ax = plt.gca()
ax.spines['left'].set_position(('data', 0))
ax.spines['left'].set_color('black')
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.xticks([-1,-0.5,0,0.5,1], labels=[f"{int(tick*100)}%" for tick in [-1,-0.5,0,0.5,1]])
plt.xlim(-1,1)
plt.yticks([0.5, 1, 1.5, 2, 2.5])
plt.xlabel('Outcomes')


plt.savefig('plots/CH5_5.2_pdf.png',dpi=400)
plt.show()
