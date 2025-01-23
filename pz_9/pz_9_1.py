# Организовать словарь avto, содержащий 3 ключа (марки авто) и списки
# из трех моделей в качестве значений. Обеспечить отображение вторых моделей по
# каждому авто, всех моделей словаря.

avto = {'Audi': ['Audi RS6', 'Audi A4', 'Audi A8'] ,
        'BMW': ['BMW X6', 'BMW 3','BMW 5'],
        'ferrari' : ['Ferrari F40', 'Ferrari Daytona', 'Ferrari 458']}

print('Вторые модели:')
for marka, model in avto.items():
  print(f'{marka}: {model[1]}')

print('Все модели: ')
for marka, model in avto.items():
  print(f'{marka}: {model}')