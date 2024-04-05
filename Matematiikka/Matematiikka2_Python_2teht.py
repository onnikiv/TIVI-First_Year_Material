from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pii=np.pi
pist_xy=np.array([pii, pii, 3*pii, pii])
nim=np.array([30, 45, 60, 90, 120, 150, 180, 270])
varit=np.array(['red', 'green', 'blue', 'orange'])

text=[r'$\pi$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\frac{\pi}{6}$']

x = np.cos(pist_xy/nim)
y = np.sin(pist_xy/nim)

plt.scatter(x, y, color=varit, marker='X')

for i in range(len(pist_xy)):
    plt.annotate(text[i],
             xy=(np.cos(pist_xy[i]/nim[i]), np.sin(pist_xy[i]/nim[i])), xycoords='data',
             xytext=(+30, +5), textcoords='offset points', fontsize=12,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))


plt.show()