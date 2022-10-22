a = int(input())
a1 = a
s = []
for j in range(1, a): 
  a = j
  for i in range(2, a + 1): 
    if a % i == 0:
      a = a / i
      s.append(i)
  if sum(s) == j:
    print(j, end=' ')
  s = []


