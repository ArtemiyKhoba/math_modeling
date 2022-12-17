import matplotlib.pyplot as plt
import numpy as np

def polar_coord(cefs, kind=None):
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Graph')
    plt.axis('equal')

    if kind == 'logarithmic_spiral':
        alpha = np.linspace(0, 8 * np.pi, 337)
        b = cefs[0]
        r = np.exp(b * alpha)
        plt.plot(r * np.cos(alpha), r * np.sin(alpha))
        plt.savefig('pic_1.png')
    elif kind == 'archimedean_spiral':
        alpha = np.arange(0, 8, 0.01)
        k = cefs[0]
        r = k * alpha
        plt.plot(r * np.cos(alpha), r * np.sin(alpha))
        plt.savefig('pic_1.png')
    elif kind == 'wand':
        alpha = np.arange(0.01, 8, 0.01)
        k = cefs[0]
        r = k / np.sqrt(alpha)
        plt.plot(r * np.cos(alpha), r * np.sin(alpha))
        plt.savefig('pic_1.png')
    elif kind == 'rose':
        alpha = np.arange(0, 8, 0.01)
        k = cefs[0]
        r = np.sin(k * alpha)
        plt.plot(r * np.cos(alpha), r * np.sin(alpha))
        plt.savefig('pic_1.png')
    else:
        print('Failed')

"""
cefs = [0.1]
polar_coord(cefs, 'logarithmic_spiral')

cefs = [2.0345]
polar_coord(cefs, 'archimedean_spiral')

cefs = [1.12]
polar_coord(cefs, 'wand')
"""
cefs = [8]
polar_coord(cefs, 'rose')