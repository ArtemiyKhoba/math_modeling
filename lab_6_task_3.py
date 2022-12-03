import matplotlib.pyplot as plt 
import numpy as np 

def plotter(x0, x1, N, *args, **kwrgs):
    if kwgrs['obj'] == 'circle':
        x = np.arange(-2 * args[0], 2 * args[0], N)
        y = np.arange(-2 * args[0], 2 * args[0], N)
        X, Y = np.meshgrid(x, y)

        fxy = X ** 2 + Y ** 2 - args[0] ** 2

        plt.contour(X, Y, fxy, levels = [0])
    
    # elif kwrgs['obj'] == 'ellips':
    #     x = np.arange(-2 * args[0], 2 * args[0], N)
    #     y = np.arange(-2 * args[1], 2 * args[1], N)
    #     X, Y = np.meshgrid(x, y)

    #     fxy = (X/args[0]) ** 2 - (Y/args[1]) ** 2 - 1

    #     plt.contour(X, Y, fxy, levels = [0])

    plt.axis('equal')
    plt.savefig('pic_1.png')


plotter(1, 4, 5, 5, obj = 'circle')  

