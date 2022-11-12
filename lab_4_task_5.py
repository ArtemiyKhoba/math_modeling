import numpy as np

def area(s, a, h):
    if s == 1: 
        return 0.5 * a * h 
    if s == 2:
        return a * h 
    if s == 3: 
        return np.pi * (h / 2) ** 2
    
str = input('Введите название фигуры : ')
if str in ('треугольник', 'Треугольник'): 
    a = float(input('Введите длину стороны : '))
    h = float(input('Высота : '))
    s = 1
if str in ('прямоугольник', 'Прямоугольник'):
    a = float(input('Стоорона а : '))
    b = float(input('Сторона b : '))
    s = 2
if str in ('Круг', 'круг', 'окружность', 'Окружность'): 
    a = 0
    h = float(input('Введите диаметр : '))
    s = 3

print(area(s, a, h))