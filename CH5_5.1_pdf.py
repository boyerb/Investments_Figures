from matplotlib import pyplot as plt

yeet=[f'{i}%' for i in range(-6,12)]
yvals=[0,0.3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.7,0]
plt.figure(figsize=(8.5, 4))
plt.bar(yeet,yvals)
plt.ylim(0,0.8)
plt.xlabel('Outcomes')
plt.ylabel('Probability')

plt.tight_layout()
plt.savefig('plots/CH5_5.1_pdf.png',dpi=400)
plt.show()