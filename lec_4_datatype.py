# unmutable - int, float, complex, str, tuple 
# mutable - list, set, dict


def changer(a : int, b : list): 
    a = 2
    b[0] = 'Good'

x = 10 
L = [1, 2]

changer(x, L)

print(x)
print(L)

L = [1, 2] 
changer(x, L[:])

print(L)

x = 3
y = 4

z = complex(x, y) 
print(z)

w = complex(y, x)

print(z + w)

s = 'Hello'

print(s[0])


t = (1, 4, 9) 
print(t)

print(t[0])

t[0] = 3


l = [1, 4, 9]
l[0] = 3
print(l)

d = {'al':4, 4:'al', 'str':'Hello'}
print(d['al'])
print(d[4])
print(d['str'])

d['str'] = 'Good'

print(d)