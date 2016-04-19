def solve(dataset):
    x, y = dataset.split()
    x, y = float(x), float(y)
    if ( y >(x--3)**2+1 )&( y >(x--3)**2+2 )|( y >(x-5)**2+4 ):
        return 1
    else:
        return 0
