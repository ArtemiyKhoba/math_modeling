import numpy as np


def product(arr: np.ndarray): 
    s = 1
    for i in range(len(arr)): 
        s *= arr[i]
    return s

arr = np.array([int(i) for i in input('Input array : ').split()])
print(f'Product : {product(arr)}')
