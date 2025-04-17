''' Для каждого столбца двумерного списка с четным номером найти сумму ее элементов.'''
import random

a = int(input('Введите количество столбцов: '))
n = int(input('Введите количество строк: '))
lis_gen = ([random.randint(1, 15) for i in range(a)] for i in range(n))
listik = list(lis_gen)
print("Сгенерированный список:")
for row in listik:
    print(row)

chet_col = [col for col in range(a) if col % 2 == 0] # определяем четные столбцы

column_sums = [(col, sum(row[col] for row in listik)) for col in chet_col] # считаем сумму каждого четного столбца

print("Суммы элементов в столбцах с четными номерами:")
for col, col_sum in column_sums:
    print(f"Столбец {col}: сумма = {col_sum}")