import numpy as np
import pandas as pd
import pylab as plt
import math
import random
def solve(dataset):
    x, y = dataset.split()
    x, y = float(x), float(y)
    if ( (x - -3)**2+ (y - 5)**2<5**2 )&( y>(-7-4*x)/-3 )|( y>(-6-2*x)/-2 )&( (x - 3)**2+ (y - 0)**2<4**2 )&( (x - 3)**2+ (y - 0)**2>2**2 ):
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
Circle = [-3+5* np.cos(np.linspace(0, 2 * math.pi, 1000)), 5+5* np.sin(np.linspace(0, 2 * math.pi, 1000))]
plt.plot(Circle[0], Circle[1], 'b')
plt.plot(-3, 5, 'ko')
y2 =(-7-4*x)/-3
plt.plot(x, y2, 'b')
y2 =(-6-2*x)/-2
plt.plot(x, y2, 'b')
Circle = [3+4* np.cos(np.linspace(0, 2 * math.pi, 1000)), 0+4* np.sin(np.linspace(0, 2 * math.pi, 1000))]
plt.plot(Circle[0], Circle[1], 'b')
plt.plot(3, 0, 'ko')
Circle = [3+2* np.cos(np.linspace(0, 2 * math.pi, 1000)), 0+2* np.sin(np.linspace(0, 2 * math.pi, 1000))]
plt.plot(Circle[0], Circle[1], 'b')
plt.plot(3, 0, 'ko')
axes = plt.gca()
axes.set_xlim(-10, 10)
axes.set_ylim(-10, 10)
axes.xaxis.set_major_locator(plt.MultipleLocator(1.0))
axes.xaxis.set_minor_locator(plt.MultipleLocator(1.0))
axes.yaxis.set_major_locator(plt.MultipleLocator(1.0))
axes.yaxis.set_minor_locator(plt.MultipleLocator(1.0))
axes.grid(which='major', axis='x', linewidth=0.55, linestyle='-', color='0.6')
axes.grid(which='minor', axis='x', linewidth=0.3, linestyle='-', color='0.6')
axes.grid(which='major', axis='y', linewidth=0.55, linestyle='-', color='0.6')
axes.grid(which='minor', axis='y', linewidth=0.3, linestyle='-', color='0.6')
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('graph0.png', bbox_inches='tight')
