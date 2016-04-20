import numpy as np
import pandas as pd
import pylab as plt
import math
import random
def solve(dataset):
    x, y = dataset.split()
    x, y = float(x), float(y)
    if ( y >(x-0)**2+-4 )&( y >(x--1)**2+4 )|( y>(9-3*x)/4 ):
        return 1
    else:
        return 0
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)
x1 = []
y1 = []
for i in x:
    for j in y:
        if solve(str(i) + ' ' + str(j)):
            x1.append(i)
            y1.append(j)
plt.plot(x1, y1, 'c.', alpha=0.2)
y2 =(x-0)**2+-4
plt.plot(x, y2, 'b')
y2 =(x--1)**2+4
plt.plot(x, y2, 'b')
y2 =(9-3*x)/4
plt.plot(x, y2, 'b')
axes = plt.gca()
axes.set_xlim(-10, 10)
axes.set_ylim(-10, 10)
axes.xaxis.set_major_locator(plt.MultipleLocator(1.0))
axes.xaxis.set_minor_locator(plt.MultipleLocator(1.0))
axes.yaxis.set_major_locator(plt.MultipleLocator(1.0))
axes.yaxis.set_minor_locator(plt.MultipleLocator(1.0))
axes.grid(which='major', axis='x', linewidth=0.5, linestyle='-', color='0.75')
axes.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
axes.grid(which='major', axis='y', linewidth=0.5, linestyle='-', color='0.75')
axes.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('graph1.png', bbox_inches='tight')
