'''Организовать и вывести последовательность из N случайных целых чисел. Из
исходной последовательности организовать последовательность, содержащую
положительные числа и последовательность, содержащую отрицательные числа. Найти
количество элементов в полученных последовательностях.'''
import random
n = int(input('Введите количество элементов в последовательности: '))
posled = [random.randint(-100, 100) for i in range(n)]
poloz_num = [x for x in posled if x > 0]
neg_num = [x for x in posled if x < 0]
poloz_count = len(poloz_num)
neg_count = len(neg_num)
print(f'Исходная последовательность: {posled}')
print(f'Последовательность с положительными числами: {poloz_num}')
print(f'Последовательность с отрицательными числами: {neg_num}')
print(f'Количество положительных элементов: {poloz_count}')
print(f'Количество отрицательных элементов: {neg_count}')