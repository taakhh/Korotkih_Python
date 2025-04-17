''' В двумерном списке найти минимальный элемент в предпоследнем столбце.'''
import random

a = int(input('Введите количество столбцов: '))
n = int(input('Введите количество строк: '))
lis_gen = ([random.randint(1, 15) for i in range(a)] for i in range(n))
listik = list(lis_gen)
for el in listik:
    print(el)

min_val = min(row[-2] for row in listik)

print(f'Минимальный элемент из предпоследнего столбца: {min_val}')