a = float(input())
n = int(input())

def power(a, n):
  s = 1
  if n < 0:
    for _ in range(abs(n)):
      s = 1 / (a * s)
  if n == 0:
    return 1
  if n > 0:
    for _ in range(n):
      s = a * s
  return s

print(power(a, n))