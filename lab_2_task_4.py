x, y = 1, 1
a = []
for i in range(int(input()) + 1):
  a.append(x)
  x, y  = y, x + y
print(*a)
