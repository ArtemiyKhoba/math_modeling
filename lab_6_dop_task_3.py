import matplotlib.pyplot as plt
import numpy as np

def func(a, b, x_start, x_stop, x_points):
    
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Piecewise graph')
    plt.axis('equal')

    y = np.zeros(len())

    x = np.linspace(x_start, a, 2)
    y = np.full(len(x), a ** 2)
    plt.plot(x, y)

    x = np.linspace(a, b, x_points)
    y = x ** 2
    plt.plot(x, y)

    x = np.linspace(b, x_stop, 2)
    y = np.full(len(x), b ** 2)
    plt.plot(x, y)
    
    plt.savefig('pic_1.png')

func(-2.67, 5.78, -11.26, 23.6, 100)