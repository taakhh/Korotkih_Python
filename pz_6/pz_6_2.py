''' Дан список A размера N. Сформировать два новых списка B и C: в список B записать
все положительные элементы список A, в список C — все отрицательные (сохраняя
исходный порядок следования элементов). Вывести вначале размер и содержимое
списка B, а затем — размер и содержимое списка C.'''
import random

N = input('Введите размер списка: ')
while True:  # обработка исключений
  try:
    N = int(N)
    N > 0
    break
  except ValueError:
    print('Вы ввели не число!')
    N = input('Введите размер списка повторно: ')

A, B, C = [], [], []
c = 0
while c < N:
  A.append(random.randint(-100, 100))
  c += 1
print('Исходный список:', A)

for num in A:
  if num >= 0:
    B.append(num)
  elif num < 0 :
    C.append(num)

print('Размер списка B:', len(B), '\n', 'Содержимое списка B:', B)
print('Размер списка C:', len(C), '\n', 'Содержимое списка C:', C)