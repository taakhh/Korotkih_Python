# Составить генератор (yield), который выводит из строки только цифры.
def num_only(numbers):
    yield from filter(str.isdigit, numbers)

numbers = input('Введите строку: ')
digits = ''.join(num_only(numbers))
print(f'Извлечённые цифры: {digits}')