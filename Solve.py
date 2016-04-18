def solve(dataset):
    x, y = dataset.split()
    x, y = float(x), float(y)
    if ( y <(x--10)**2+3 )&( y <(x-9)**2+-3 )&( (x - 7)**2+ (y - -4)**2>4**2 ):
        return 1
    else:
        return 0
