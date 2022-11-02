import numpy as np
def middle(length):
    s = 0
    print('Input array :', end = ' ')
    b = list(map(int, input().split()))
    arr = np.array(b)
    for i in range(length): 
        s += arr[i]
    return s / length

length = int(input('Input length : '))
print(f'Arithmetical mean : {middle(length)}')