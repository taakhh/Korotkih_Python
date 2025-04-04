#Дано целое число N (>0). Найти наименьшее целое положительное число K, квадрат которого превосходит N: K2 > N. Функцию извлечения квадратного корня не использовать.
N = input('Введите целое число: ')
while type(N) != int: #обработка исключений
    try:
        N = int(N)
        if N > 0:
            break
        else:
            print('Вы ввели число меньше или равное 0')
            N = input('Введите целое число: ')
    except ValueError:
        print('Вы ввели не то число')
        N = input('Введите целое число: ')

K = 1
while K * K <= N: #обработка исключений
    K += 1

print("Наименьшее целое положительное число K, квадрат которого превосходит", N, ':', K)