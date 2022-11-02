from lab_3_task_1 import gravity_acceleration as g
import numpy as np 
x0 = int(input('Input x0 : '))
y0 = int(input('Input y0 : '))
v0 = int(input('Input v0 : '))
a = np.degrees(int(input('Input alpha : ')))
vx0 = v0 * np.cos(np.radians(a))
vy0 = v0 * np.sin(np.radians(a))


t = np.arange(0, 5, 0.01)
x = x0 + vx0 * t
y = y0 + vy0 * t + g * t ** 2 / 2

coord = np.zeros((len(t), 3))

for i in range(len(t)): 

    coords[i, 0] = t[i]
    coords[i, 1] = x[i]
    coords[i, 2] = y[i]

print(coords)