''' С помощью функций получить вертикальную и горизонтальную линии. Линия
проводится многократной печатью символа. Заключить слово в рамку из
полученных линий. '''


def h_line(length):
  return '-' * length


def ramka(word):
  word_length = len(word)
  horizontal_line = h_line(word_length + 2)
  vertical_line = '|' + word + '|'

  print(horizontal_line)  # верхняя линия
  print(vertical_line)  # слово с вертикальными линиями
  print(horizontal_line)  # нижняя линия


word = input('Введите слово: ')
ramka(word)