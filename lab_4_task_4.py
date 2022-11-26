import numpy as np

def func(a, b, N):
    x = np.linspace(a, b, N)
    y = x ** 2
    coords = np.zeros((N, 2))

    for i in range(N): 
        coords[i, 0] = x[i]
        coords[i, 1] = y[i]
    print(coords)

func(-10, 10, 100)
