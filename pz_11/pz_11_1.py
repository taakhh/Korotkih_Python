''' Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Исходные данные:
Количество элементов:
Индекс первого минимального элемента:
Умножаем все элементы на минимальный элемент:'''
listik = ['1 -2 90 -228 22 -15 14 45']
f1 = open('data_1.txt', 'w')
f1.writelines(listik)
f1.close()

f2 = open('data_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(listik)
f2.close()

f1 = open('data_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

multi_nums = []
min_el = min(k)
min_ind = k.index(min_el)
for i in k:
    multi_num = i * min_el
    multi_nums.append(multi_num)

f2 = open('data_2.txt', 'w')
f2.write('Исходные данные: ')
f2.write('\n')
f2.write(' '.join(map(str, k)) + '\n')  # Записываем исходные данные
f2.write('Количество элементов:\n')
f2.write(str(len(k)) + '\n')  # Записываем количество элементов
f2.write('Индекс первого минимального элемента:\n')
f2.write(str(min_ind) + '\n')  # Записываем индекс минимального элемента
f2.write('Умножение всех элементов на минимальный элемент:\n')
f2.write(' '.join(map(str, multi_nums)) + '\n')  # Записываем результат умножения
f2.close()

