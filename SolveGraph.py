import numpy as np
import pandas as pd
import pylab as plt
import math
import random
def solve(dataset):
    x, y = dataset.split()
    x, y = float(x), float(y)
    if ( y >(x--3)**2+-6 )|( (x - -10)**2+ (y - -2)**2<2**2 )&( y<(5--7*x)/9 )&( y <(x--8)**2+1 ):
        return 1
    else:
        return 0
