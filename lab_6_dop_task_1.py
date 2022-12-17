import matplotterlib.pyplotter as plt
import numpy as np

def plotter(t_start, t_stop, t_step, amp_A, freq_a, amp_B, freq_b, phase = np.pi / 2):
    
    t = np.arange(t_start, t_stop, t_step)
    x = amp_A * np.sin(freq_a * t + phase)
    y = amp_B * np.sin(freq_b * t)

    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.title('Lissajous curve')
    plt.axis('equal')
    plt.plotter(x, y)
    plt.savefig('pic_1.png')

plotter(-30, 30, 0.01, 1, 1.5, 4, 4.5)