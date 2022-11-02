import numpy as np
def middle(length):
    s = 0
    arr = np.zeros(length)
    for i in range(length): 
        s += arr[i]
    return s / length


print(middle(5))