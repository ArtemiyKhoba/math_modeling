x, y = 1, 1
a = []
c = 0
for i in range(int(input()) + 1):
  a.append(x)
  c = x + y
  x = y
  y = c
print(*a)

