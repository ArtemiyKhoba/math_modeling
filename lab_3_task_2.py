import numpy as np 
from math import sqrt
from lab_3_task_1 import gravity_acceleration as g
from lab_3_task_1 import ℏ, k, e

h = 100
b = np.degrees(30)
a = np.radians(np.pi) / 3
v = sqrt(g * h * (np.tan(np.radians(b) ** 2) / 2 * np.cos(a) ** 2 * (1 - np.tan(b) * np.tan(a))))
print(v)

T = 200
N = (2 / sqrt(np.pi)) * (ℏ / (k * T) ** (3/2)) * (e ** (e * (-1) / k * T )) * e ** (T / 2)
print(N)