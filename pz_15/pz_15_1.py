'''Приложение ТОРГОВАЯ ФИРМА для автоматизированного контроля продаж
товаров торговой фирмы. БД должна содержать таблицу Продажа товаров со следующей
структурой записи: Дата продажи, Товар, Сумма, Скидка, Филиал, Менеджер.
'''

from data import data
import sqlite3 as sq

with sq.connect('trading_company.db') as con:
  cur = con.cursor()
  cur.execute('DROP TABLE IF EXISTS sale_of_goods')
  cur.execute('''CREATE TABLE sale_of_goods(
    date_sale date NOT NULL PRIMARY KEY AUTOINCREMENT ,
    product VARCHAR(50) NOT NULL,
    amount INT NOT NULL,
    discount FLOAT,
    branch VARCHAR(50),
    manager TEXT
  )''')

  cur.executemany('INSERT INTO sale_of_goods VALUES(?, ?, ?, ?, ?, ?)', data) # Заполнение таблицы данными из своего файла

  # Команды для поиска данных
  print("\nДорогие продажи (сумма > 30000):")
  for row in cur.execute("SELECT * FROM sale_of_goods WHERE amount > 30000"):
    print(row)

  print("\nПродажи в Москве и СПб:")
  for row in cur.execute("SELECT * FROM sale_of_goods WHERE branch = 'Санкт-Петербург' OR branch = 'Москва'"):
    print(row)

  print("\nСмартфоны по цене 40000-45000:")
  for row in cur.execute("SELECT * FROM sale_of_goods WHERE product LIKE '%Смартфон%' AND amount BETWEEN 40000 AND 45000 "):
    print(row)

  # Команды для удаления данных
  cur.execute("DELETE FROM sale_of_goods WHERE date_sale = '2024-03-21'")
  cur.execute("DELETE FROM sale_of_goods WHERE amount < 10000")
  cur.execute("DELETE FROM sale_of_goods WHERE branch = 'Казань'")

  # Команды для изменения данных
  cur.execute("UPDATE sale_of_goods SET amount = amount * (1 - discount) WHERE discount = 0.2")
  cur.execute("UPDATE sale_of_goods SET manager = 'Алехина Н.' WHERE branch = 'Краснодар'")
  cur.execute("UPDATE sale_of_goods SET discount = 0.4 WHERE discount = 0.3")

  print("\nВсе продажи после изменений:")
  for row in cur.execute("SELECT * FROM sale_of_goods"):
    print(row)
