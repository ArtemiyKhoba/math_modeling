a, b, c = float(input()), float(input()), float(input())
if a + b > c and a + c > b and b + c > a: 
  print('Существует ', end='')
  if a == b == c: 
    print('Равносторонний')
  elif a in (b, c) or b in (a,c):
    print('Равнобедренный')
  else: 
    print('Разносторонний')
else: 
  print('Не существует')
