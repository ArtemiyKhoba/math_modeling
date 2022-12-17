import matplotlib.pyplot as plt
import numpy as np
plt.axis('equal')
def cycloid_astroid_plotter(R, kind):
    t = np.arange(0, 8 * np.pi, 0.01)
    if kind == 'cycloid':
        x = R * (t*R - np.sin(t)*R)
        y = R * (R - R*np.cos(t))
        plt.plot(x, y, ls='-', lw=4)
        plt.savefig('pic.png')
    elif kind == 'astroid':
        x = R * np.cos(t) ** 3
        y = R * np.sin(t) ** 3
        plt.plot(x, y, ls='--', lw=2)
        plt.savefig('pic.png')


# cycloid_astroid_plotter(3, 'cycloid')

cycloid_astroid_plotter(3, 'astroid')