import random
def GenerateLine(points, znak):
    i = random.randint(0, len(points)-2)
    B = points[i][1] - points[i + 1][1]
    A = points[i + 1][0] - points[i][0]
    C = points[i + 1][0] * points[i][1] - points[i][0] * points[i + 1][1]
    j = random.randint(0, len(znak)-1)
    return ['y' + str(znak[j]) + '(' + str(C) + '-' + str(A) + '*x)/' + str(B), 'y =' + '(' + str(C) + '-' + str(A) + '*x)/' + str(B)]
def GenerateCircle(points, znak):
    a = random.randint(0, len(points)-1)
    r = random.randint(1, 5)
    x1 = points[a][0]
    y1 = points[a][1]
    j = random.randint(0, len(znak)-1)
    return ['(x - ' + str(x1) + ')**2' + '+ (y - ' + str(y1) + ')**2' + str(znak[j]) + str(r) + '**2', '(x - ' + str(x1) + ')**2' + '+ (y - ' + str(y1) + ')**2' + '=' + str(r) + '**2']
def GenerateParabola(points, znak):
    a = random.randint(0, len(points)-1)
    x1 = points[a][0]
    y1 = points[a][1]
    j = random.randint(0, len(znak)-1)
    return ['y ' + str(znak[j]) + '(x-' + str(x1) + ')**2' + '+' + str(y1), 'y =' + '(x-' + str(x1) + ')**2' + '+' + str(y1)]
def GenerateFun(diff):
    points = []
    pointtemp = []
    for i in range(8):
        pointtemp.append(random.randint(-10, 10))
        pointtemp.append(random.randint(-10, 10))
        points.append(pointtemp)
        pointtemp = []
    znak = ['>', '<']
    logicznak = ['&', '|']
    funct = ''
    flag = 0
    while diff > 0:
        if flag:
            i = random.randint(1, 3)
        else:
            i = random.randint(2, 3)
        j = random.randint(0, 1)
        if i == 1:
            Line = GenerateLine(points, znak)[0]

            funct += logicznak[j] + '( ' +  + ' )'
        elif i == 2:
            if flag:
                funct += logicznak[j] + '( ' + GenerateCircle(points, znak) + ' )'
            else:
                funct += '( ' + GenerateCircle(points, znak) + ' )'
                flag = 1
        elif i == 3:
            if flag:
                funct += logicznak[j] + '( ' + GenerateParabola(points, znak) + ' )'
            else:
                funct += '( ' + GenerateParabola(points, znak) + ' )'
                flag = 1
        diff -= i
    return funct
difficulty = 7
f = open('Solve.py', 'w')
f1 = open('SolveGraph.py', 'w')
f.write('def solve(dataset):\n')
f.write('    x, y = dataset.split()\n')
f.write('    x, y = float(x), float(y)\n')
funct = GenerateFun(difficulty)
f.write('    if ' + funct + ':\n')
f.write('        return 1\n')
f.write('    else:\n')
f.write('        return 0\n')
f.close()
f1.close()