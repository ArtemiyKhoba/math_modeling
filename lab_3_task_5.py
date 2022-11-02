from lab_3_task_4 import A 
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
A1 = A.copy()
s = A1[ : , 1]
q = A[ : , 2]
A[ : , 1] = q 
A[ : , 2] = s
print(A)