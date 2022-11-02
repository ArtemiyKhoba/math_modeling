import numpy as np
row = int(input('Input row : '))
col = int(input('Input col : '))
a = np.zeros((row, col))
print('Введите элементы массива построчно : ')
for i in range(row): 
    s = list(map(int, input().split()))
    for j in range(col): 
        a[i, j] = s[j]
    s.clear()
print(a)

for i in range(col): 
    print(f'Максимум {i}-го стоблца : {max(a[ : , i])}')