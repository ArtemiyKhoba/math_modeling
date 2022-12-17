import matplotlib.pyplot as plt
import numpy as np

def polar_ellipse(ex, foc):
    
    alpha = np.arange(0, 8, 0.01)
    r = foc / (1 + ex *  np.cos(alpha))
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Ellipse')
    plt.axis('equal')
    plt.plot(r * np.cos(alpha), r * np.sin(alpha))
    plt.savefig('pic_1.png')

polar_ellipse(0.5, 4.24)