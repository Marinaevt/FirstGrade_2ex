def solve(dataset):
    x, y = dataset.split()
    x, y = float(x), float(y)
    if ( y >(x--1)**2+-9 )&( y<(60--1*x)/-10 )&( y >(x--5)**2+-10 ):
        return 1
    else:
        return 0
