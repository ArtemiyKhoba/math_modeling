a = int(input())
for i in range(2,a+1): 
  if a % i == 0:
    a = a/i
    print(i)