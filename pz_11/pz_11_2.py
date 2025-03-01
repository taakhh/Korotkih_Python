''' Из предложенного текстового файла (text18-14.txt) вывести на экран его содержимое,
количество пробельных символов. Сформировать новый файл, в который поместить текст
в стихотворной форме предварительно заменив символы третей строки их числовыми
кодами.'''
t = 0  # Счётчик строк
d = 0  # Счётчик пробельных символов

for i in open('text18-14.txt', encoding='UTF-8'):
    print(i, end='')  # Выводим содержимое файла на экран
    t += 1  # Считаем количество строк
    for j in i:
        if j.isspace():  # Проверяем, является ли символ пробельным
            d += 1  

print(end='\n')
print('Количество строк: ', t, end='\n')
print('Количество пробельных символов: ', d, end='\n')

f1 = open('text18-14.txt', encoding='UTF-8')
l = f1.readlines()  
f1.close()

if len(l) >= 3:  
    third_line = l[2].rstrip('\n') 
    third_line_codes = []  

    for char in third_line:
        code = ord(char)  # Получаем числовой код символа
        third_line_codes.append(str(code))  # Добавляем код в список как строку

    third_line_codes_str = ' '.join(third_line_codes)
    l[2] = third_line_codes_str + '\n'  # Обновляем третью строку

# Создаем новый файл с изменённым текстом
f2 = open('text18-2.txt', 'w', encoding='UTF-8')
f2.writelines(l)  
f2.close()
