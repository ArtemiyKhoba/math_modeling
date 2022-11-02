import numpy as np
row = int(input('Input row: '))
col = int(input('Input col: '))
arr1, arr2, arr3 = np.zeros((row, col)), np.zeros((row, col)), np.zeros((row, col))
print('Введите элементы первого массива построчно : ')
for i in range(row): 
    s = list(map(int, input().split()))
    for j in range(col): 
        arr1[i, j] = s[j]
    s.clear()

print('Введите элементы второго массива построчно : ')
for i in range(row): 
    s = list(map(int, input().split()))
    for j in range(col): 
        arr2[i, j] = s[j]
    s.clear()

for i in range(row): 
    for j in range(col): 
        arr3[i][j] = max(arr2[i][j], arr1[i][j])

print(arr3)


