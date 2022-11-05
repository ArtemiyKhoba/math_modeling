
def enegry(m, h, v):
    g = 9.81
    E = m * g * h + (m * v ** 2) / 2
    return E

m = float(input('Input mass :'))
h = float(input('Input height :'))
v = float(input('Input speed :'))
print('Energy : ', enegry(m, h, v))