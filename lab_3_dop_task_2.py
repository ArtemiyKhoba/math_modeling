import numpy as np
a = np.zeros(5)
print("Введите первые 4 элемента массива : ")
a[0], a[1], a[2], a[3] = map(int, input().split())
print(a)
print('Введите индекс последнего элемента : ')
index = int(input())
print('Введите значение последнего элемента : ')
m = int(input())
s = a[-2]
for i in range(index, 4):
    a[i + 1] = a[i]
a[-1] = s
a[index] = m 

print(a)