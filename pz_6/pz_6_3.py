'''Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
одну позицию (при этом A1 перейдет в A2, A2 — в A3,..., AN — в A1).'''
import random

N = input('Введите размер списка: ')
while True: # обработка исключений
  try:
    N = int(N)
    break
  except ValueError:
    print('Вы ввели не число!')
    N = input('Введите размер списка повторно: ')

A = []
c = 0
while c < N:
  A.append(random.randint(-100, 100))
  c += 1
print('Исходный список:', A)

if N > 0:
  last_el = A[-1]

  for i in range(N - 1, 0, -1):
      A[i] = A[i - 1]
  A[0] = last_el

print('Список после циклического сдвига вправо:', A)