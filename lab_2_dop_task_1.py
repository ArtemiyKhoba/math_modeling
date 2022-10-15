from math import sqrt
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
if d > 0: 
  print(f'x1 = {(-b + sqrt(d))/(2*a)}')
  print(f'x2 = {(-b - sqrt(d))/(2*a)}')
if d == 0: 
  print(f'x = {(-b)/(2*a)}')
if d < 0:
  print('Корней нет')