#Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все целые степени числа A от 1 до N.
A = input('введите вещественное число: ')
N = input('введите целое число: ')
P = 1
while type(A) != float or type(N) != int: #обработка исключений
  try:
    A = float(A)
    N = int(N)
    if N > 0:
        break  # Выходим из цикла, если введенные данные корректные
    else:
        print('Вы ввели число меньше 0')
        N = input('Введите число больше 0: ')
  except ValueError:
    print('вы ввели не число')
    A = input('введите вещественное число: ')
    N = input('введите целое число: ')

i = 1
while i <= N: #обработка исключений
    P *= A
    print(A, "в степени", i, "равно", P)
    i += 1
