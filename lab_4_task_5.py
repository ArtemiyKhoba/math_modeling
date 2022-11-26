import numpy as np

def area(*args, **kw):
    
    if kw['figure'] == 'triangle': 
            return 0.5 * float(args[0]) * float(args[1])
    if kw['figure'] == 'rectangular':
        return float(args[0]) * float(args[1])
    if kw['figure'] == 'circle': 
        return np.pi * (float(args[0]) / 2) ** 2


print(area(2, 3, figure = input()))
