import random
import IsInside
import numpy as np
import math
import os

def GenerateLine(points, znak):
    i = random.randint(0, len(points) - 2)
    B = points[i][1] - points[i + 1][1]
    while B == 0:
        i = random.randint(0, len(points) - 2)
        B = points[i][1] - points[i + 1][1]
    A = points[i + 1][0] - points[i][0]
    C = points[i + 1][0] * points[i][1] - points[i][0] * points[i + 1][1]
    j = random.randint(0, len(znak)-1)
    return ['y' + str(znak[j]) + '(' + str(C) + '-' + str(A) + '*x)/' + str(B), 'y2 =' + '(' + str(C) + '-' + str(A) + '*x)/' + str(B)]
def GenerateCircle(points, znak):
    a = random.randint(0, len(points)-1)
    r = random.randint(1, 5)
    x1 = points[a][0]
    y1 = points[a][1]
    j = random.randint(0, len(znak)-1)
    #return ['(x - ' + str(x1) + ')**2' + '+ (y - ' + str(y1) + ')**2' + str(znak[j]) + str(r) + '**2', '(x - ' + str(x1) + ')**2' + '+ (y - ' + str(y1) + ')**2' + '=' + str(r) + '**2']
    #return ['(x - ' + str(x1) + ')**2' + '+ (y - ' + str(y1) + ')**2' + str(znak[j]) + str(r) + '**2',
    #       'y2 = (' + str(r) + '**2 - (x - ' + str(x1) + ')**2)**(0.5) + ' + str(y1),
    #        'y2 = -(' + str(r) + '**2 - (x - ' + str(x1) + ')**2)**(0.5) + ' + str(y1)]
    return ['(x - ' + str(x1) + ')**2' + '+ (y - ' + str(y1) + ')**2' + str(znak[j]) + str(r) + '**2',
            [x1, y1, r]]
def GenerateParabola(points, znak):
    a = random.randint(0, len(points)-1)
    x1 = points[a][0]
    y1 = points[a][1]
    j = random.randint(0, len(znak)-1)
    #return ['y ' + str(znak[j]) + '(x-' + str(x1) + ')**2' + '+' + str(y1), 'y2 =' + '(x-' + str(x1) + ')**2' + '+' + str(y1)]
    return ['y ' + str(znak[j]) + '(x-' + str(x1) + ')**2' + '+' + str(y1),
            [x1, y1]]
def GenerateInsidePoints():
    global minX, minY, maxX, maxY
    points = []
    pointtemp = []
    for i in range(8):
        pointtemp.append(random.randint(-5, 5))
        pointtemp.append(random.randint(-5, 5))
        while IsInside.IsInside(pointtemp[0], pointtemp[1]) == 0:
            pointtemp = []
            pointtemp.append(random.randint(-5, 5))
            pointtemp.append(random.randint(-5, 5))
        if pointtemp[0] > maxX:
            maxX = pointtemp[0]
        if pointtemp[0] < minX:
            minX = pointtemp[0]
        if pointtemp[1] > maxY:
            maxY = pointtemp[1]
        if pointtemp[1] < minY:
            minY = pointtemp[1]
        points.append(pointtemp)
        pointtemp = []
    return points
def GenerateFun(diff):
    global minX, minY, maxX, maxY
    points = []
    pointtemp = []
    for i in range(8):
        pointtemp.append(random.randint(-5, 5))
        pointtemp.append(random.randint(-5, 5))
        if pointtemp[0] > maxX:
            maxX = pointtemp[0]
        if pointtemp[0] < minX:
            minX = pointtemp[0]
        if pointtemp[1] > maxY:
            maxY = pointtemp[1]
        if pointtemp[1] < minY:
            minY = pointtemp[1]
        points.append(pointtemp)
        pointtemp = []
    znak = ['>', '<']
    logicznak = ['&', '|']
    funct = ''
    flag = 0
    graphs = []
    while diff > 0:
        if flag:
            i = random.randint(1, 3)
        else:
            i = random.randint(2, 3)
        j = random.randint(0, 1)
        if i == 1:
            Line = GenerateLine(points, znak)
            graphs.append(Line[1])
            funct += logicznak[j] + '( ' + Line[0] + ' )'
        elif i == 2:
            Circle = GenerateCircle(points, znak)
            graphs.append(Circle[1])
            #graphs.append(Circle[2])
            if flag:
                funct += logicznak[j] + '( ' + Circle[0] + ' )'
            else:
                funct += '( ' + Circle[0] + ' )'
                flag = 1
                fin = open('IsInside.py', 'w')
                fin.write('def IsInside(x, y):\n')
                fin.write('    if ' + Circle[0] + ':\n')
                fin.write('        return 1\n')
                fin.write('    else:\n')
                fin.write('        return 0\n')
                fin.close()
                points = []
                points = GenerateInsidePoints()
        elif i == 3:
            Parabola = GenerateParabola(points, znak)
            graphs.append(Parabola[1])
            if flag:
                funct += logicznak[j] + '( ' + Parabola[0] + ' )'
            else:
                funct += '( ' + Parabola[0] + ' )'
                flag = 1
                fin = open('IsInside.py', 'w')
                fin.write('def IsInside(x, y):\n')
                fin.write('    if ' + Parabola[0] + ':\n')
                fin.write('        return 1\n')
                fin.write('    else:\n')
                fin.write('        return 0\n')
                fin.close()
                points = []
                points = GenerateInsidePoints()
        diff -= i
    graphs.append(funct)
    return graphs
difficulty = 7
numvar = 2
for k in range(numvar):
    maxY = -10
    minY = 10
    maxX = -10
    minX = 10
    f = open('Solve' + str(k) + '.py', 'w')
    f1 = open('SolveGraph' + str(k) + '.py', 'w')
    f2 = open('TestGenerator.py', 'r')
    f3 = open('CheckFile.py', 'r')
    for line in f2:
        f.write(line)
    f.write('def solve(dataset):\n')
    f.write('    x, y = dataset.split()\n')
    f.write('    x, y = float(x), float(y)\n')
    funct = GenerateFun(difficulty)
    f.write('    if ' + funct[-1] + ':\n')
    f.write('        return \'YES\'\n')
    f.write('    else:\n')
    f.write('        return \'NO\'\n')
    for line in f3:
        f.write(line)
    f1.write('import numpy as np\nimport pandas as pd\nimport pylab as plt\nimport math\nimport random\n')
    f1.write('def solve(dataset):\n')
    f1.write('    x, y = dataset.split()\n')
    f1.write('    x, y = float(x), float(y)\n')
    f1.write('    if ' + funct[-1] + ':\n')
    f1.write('        return 1\n')
    f1.write('    else:\n')
    f1.write('        return 0\n')
    f1.write('x = np.linspace(-10, 10, 200)\ny = np.linspace(-10, 10, 200)\n')
    f1.write('x1 = []\ny1 = []\n')
    f1.write('for i in x:\n')
    f1.write('    for j in y:\n')
    f1.write('        if solve(str(i) + \' \' + str(j)):\n')
    f1.write('            x1.append(i)\n')
    f1.write('            y1.append(j)\n')
    f1.write('plt.plot(x1, y1, \'c.\', alpha=0.2)\n')
    for i in range(len(funct)-1):
        aaaa = len(funct[i])
        if len(funct[i]) == 3:
            f1.write('Circle = [' + str(funct[i][0]) + '+' + str(funct[i][2]) + '* np.cos(np.linspace(0, 2 * math.pi, 1000)), ' + str(funct[i][1]) + '+' + str(funct[i][2]) + '* np.sin(np.linspace(0, 2 * math.pi, 1000))]\n')
            f1.write('plt.plot(Circle[0], Circle[1], \'b\')\n')
            f1.write('plt.plot({}, {}, \'ko\')\n'.format(funct[i][0], funct[i][1]))
            # f1.write('y2 = ' + str(funct[i][0]) + '\n')
            # f1.write('x2 = ' + str(funct[i][1]) + '\n')
            # f1.write('plt.plot(x2, y2, \'b\')\n')
        elif len(funct[i]) == 2:
            f1.write('y2 = (x - {})**2+{}\n'.format(funct[i][0], funct[i][1]))
            f1.write('plt.plot(x, y2, \'b\')\n')
            f1.write('plt.plot({}, {}, \'ko\')\n'.format(funct[i][0], funct[i][1]))
        else:
            f1.write(funct[i] + '\n')
            f1.write('plt.plot(x, y2, \'b\')\n')
    f1.write('axes = plt.gca()\n')
    #f1.write('axes.set_xlim(' + str(minX) + ', ' + str(maxX) + ')\n')
    #f1.write('axes.set_ylim(' + str(minY) + ', ' + str(maxY) + ')\n')
    f1.write('axes.set_xlim(-10, 10)\n')
    f1.write('axes.set_ylim(-10, 10)\n')
    f1.write('axes.xaxis.set_major_locator(plt.MultipleLocator(1.0))\n')
    f1.write('axes.xaxis.set_minor_locator(plt.MultipleLocator(1.0))\n')
    f1.write('axes.yaxis.set_major_locator(plt.MultipleLocator(1.0))\n')
    f1.write('axes.yaxis.set_minor_locator(plt.MultipleLocator(1.0))\n')
    f1.write('axes.grid(which=\'major\', axis=\'x\', linewidth=0.55, linestyle=\'-\', color=\'0.6\')\n')
    f1.write('axes.grid(which=\'minor\', axis=\'x\', linewidth=0.3, linestyle=\'-\', color=\'0.6\')\n')
    f1.write('axes.grid(which=\'major\', axis=\'y\', linewidth=0.55, linestyle=\'-\', color=\'0.6\')\n')
    f1.write('axes.grid(which=\'minor\', axis=\'y\', linewidth=0.3, linestyle=\'-\', color=\'0.6\')\n')
    f1.write('plt.gca().set_aspect(\'equal\', adjustable=\'box\')\n')
    f1.write('plt.savefig(\'graph' + str(k) + '.png\', bbox_inches=\'tight\')\n')
    f.close()
    f1.close()
    f2.close()
    f3.close()
for k in range(numvar):
    os.system('python SolveGraph' + str(k) + '.py')
