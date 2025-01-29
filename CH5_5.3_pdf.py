from scipy.stats import skewnorm
from matplotlib import pyplot as plt
import numpy as np


x=np.linspace(-1.5,2,1000)
x_altered=[2*x[i]+0.6 for i in range(len(x))]
y = skewnorm.pdf(x_altered, 5)
y_scaled = y / y.max() * 1.4

plt.plot(x,y_scaled)

ax = plt.gca()
ax.spines['left'].set_position(('data', 0))
ax.spines['left'].set_color('black')
ax.spines['left'].set_linewidth(1)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.xticks([-2,-1.5,-1,-0.5,0,0.5,1,1.5,2], labels=[f"{int(tick*100)}%" for tick in [-2,-1.5,-1,-0.5,0,0.5,1,1.5,2]])
plt.xlim(-2,2)
plt.yticks([0.2,0.4,0.6,0.8,1,1.2,1.4,1.6])
plt.xlabel('Outcomes')
plt.ylim(bottom=0)

plt.savefig('plots/CH5_5.3_pdf.png',dpi=400)
plt.show()