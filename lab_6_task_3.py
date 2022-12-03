import matplotlib.pyplot as plt 
import numpy as np 

def plotter(x0, x1, N, *args, **kwrgs): 
    if kwrs['obj'] == 'circle':
        x = np.arange(-2 * args[0], 2 * args[0], 0.1)
        y = np.arange(-2 * args[0], 2 * args[0], 0,1)
        X, Y = np.mashgrid(x, y)
        

    # elif kwrgs['obj'] == 'ellips':
        