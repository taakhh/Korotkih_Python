# Составить генератор (yield), который выводит из строки только цифры.
def num_only(numbers):
  for i in numbers:
    if i.isdigit():
      yield i

numbers = input('Введите строку: ')
num = num_only(numbers)
print('Цифры в строке: ')
for i in num:
  print(i)