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
f1.writelines(listik)  # Записываем список в файл
f1.close()
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
for num in k:
    f2.write(f"{num} ")  # Записываем каждое число с пробелом
f2.write('\n')
f2.write('Количество элементов:\n')
f2.write(f"{len(k)}\n")
f2.write('Индекс первого минимального элемента:\n')
f2.write(f"{min_ind}\n")
f2.write('Умножение всех элементов на минимальный элемент:\n')
for num in multi_nums:
    f2.write(f"{num} ")  # Записываем каждое число с пробелом
f2.write('\n')
f2.close()


