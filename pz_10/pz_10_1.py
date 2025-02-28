'''Книжные магазины предлагают следующие коллекции книг.
Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
БукМаркет – Пушкин, Достоевский, Маяковский.
Галерея – Чехов, Тютчев, Пушкин.
Определить:
1.в каких магазинах можно одновременно приобрести книги Достоевского и
Пушкина.
2.в ассортимент магазина Галерея добавить автора Грибоедов.
3.какие книги из магазина ДомКниги отсутствуют в магазине Галерея.'''

magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
dom_knigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
book_market = {'Пушкин', 'Достоевский', 'Маяковский'}
gallery = {'Чехов', 'Тютчев', 'Пушкин'}

shops_book = set() # Дополнительное множество для длобавления названий магазинов, в которых есть Достоевский и Пушкин
if magistr & {'Достоевский', 'Пушкин'} == {'Достоевский', 'Пушкин'}:
    shops_book.add('Магистр')
if dom_knigi & {'Достоевский', 'Пушкин'} == {'Достоевский', 'Пушкин'}:
    shops_book.add('ДомКниги')
if book_market & {'Достоевский', 'Пушкин'} == {'Достоевский', 'Пушкин'}:
    shops_book.add('БукМаркет')
if gallery & {'Достоевский', 'Пушкин'} == {'Достоевский', 'Пушкин'}:
    shops_book.add('Галерея')
print("Магазины, где можно купить книги Достоевского и Пушкина:", shops_book)

if 'Грибоедов' not in gallery: # Добавление автора Грибоедова в ассортимент магазина Галерея
    gallery.add('Грибоедов')
print('Ассортимент магазина Галерея после добавления Грибоедова: ', gallery)

a = dom_knigi - gallery # Находим разность двух множеств, чтобы определить какие книги из ДомаКниги отсутствуют в Галерее
print('Книги из магазина ДомКниги, которые отсутствуют в магазине Галерея:', a)
