import numpy as np


def product(arr: np.ndarray): 
    return arr.prod()

arr = np.array([int(i) for i in input('Input array : ').split()])
print(f'Product : {product(arr)}')
