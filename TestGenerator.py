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
