import math
import random

def generate():
    numtests = 10
    tests = []
    for i in range(numtests):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        tests.append(str(x) + ' ' + str(y))
    return tests
def solve(dataset):
    x, y = dataset.split()
    x, y = float(x), float(y)
    if ( (x - 5)**2+ (y - -4)**2<1**2 )|( y <(x--4)**2+-2 )|( (x - 2)**2+ (y - -3)**2>4**2 ):
        return 'YES'
    else:
        return 'NO'
def check(reply, clue):
    if reply == clue:
        return 1
    else:
        return 0