a, b = map(int, input().split())
if b == 0: 
  print('АХ ТЫ ТВАРЬ')
  exit(0)
elif a % b == 0:
  print('YES')
else: 
  print('NO')
  print(a % b)
print(a/b)