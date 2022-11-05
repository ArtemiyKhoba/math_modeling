import numpy as np


def middle(arr: np.ndarray[int]) -> float:
    return arr.mean()

arr = np.array([int(i) for i in input('Input array : ').split()])
print(f'Arithmetical mean : {middle(arr)}')