'''С помощью функций получить вертикальную и горизонтальную линии. Линия
проводится многократной печатью символа. Заключить слово в рамку из
полученных линий.'''
def h_line(length):
  return '-' * length


def ramka(word):
  word_length = len(word)
  vertical_line = ('|' + word + '|')
  horizontal_line = h_line(word_length + 2)
  print(horizontal_line)
  print(vertical_line)
  print(horizontal_line)

word = input('Введите слово: ')
ramka(word)