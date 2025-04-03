# Составить генератор (yield), который выводит из строки только цифры.
def num_only(numbers):
    yield from filter(str.isdigit, numbers)

numbers = input('Введите строку: ')
num = num_only(numbers)
a = []
for i in num:
    a.append(i)
print(''.join(a))