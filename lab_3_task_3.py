from lab_3_task_1 import gravity_acceleration as g
x0 = int(input("Введите начальную координату Х : "))
y0  = int(input("Введите начальную координату Y : "))
v0 = int(input("Введите начальную скорость V0 : "))
print('t  x  y')
for t in range(6):
    x = x0 + v0 * t 
    y = y0 + v0 * t + (g * t ** 2) / 2
    print(t, x, y, sep = '  ', end = '\t')
    print()