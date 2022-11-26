def func(a, b, N): 
    for x in range(1, N):
        if a > x ** 2 > b: 
            return x ** 2

print(func(1, 5, 2))