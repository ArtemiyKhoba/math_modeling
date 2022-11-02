import numpy as np
N = int(input('Input row: '))
M = int(input('Input col: '))
A = np.zeros((N, M))
for i in range(N): 
    for j in range(M):
        s = np.sin(N * (i+1) + M * (j + 1))
        if s < 0: 
            A[i][j] = 0
        else: 
            A[i][j] = s

print(A)