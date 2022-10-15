b1 = float(input())
q = float(input())
n = int(input())
a = []
for i in range(n): 
  a.append(str(b1))
  b1 *= q
print(', '.join(a))
