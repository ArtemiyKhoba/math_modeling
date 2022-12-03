import matplotlib.pyplot as plt 
import numpy as np 

def plotter(x0, x1, N, *args, **kwrgs): 
    X = np.arange(x0, x1, N)

    if kwrgs['obj'] == 'parabola':
        y = args[0] * X ** 2 + args[1] * X + args[2]
        title = 'parabola'
    elif kwrgs['obj'] == 'hyperbola':
        i = np.arange(0)
        np.delete(X, i)
        y = args[0] / X + args[1]
        title = 'hyperbola'
    
    plt.plot(X, y)
    plt.xlabel('coord: x')
    plt.ylabel('coord: y')
    plt.title(title)
    plt.axis('equal')
    plt.savefig('pic_1.png')


plotter(-20, 10, 0.1, 1, 3, 6,obj = 'parabola')

    




