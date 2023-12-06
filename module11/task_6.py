print('Задача 6. Ход конём\n')

# В рамках разработки шахматного ИИ стоит новая задача. По заданным вещественным координатам коня и второй точки
# программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов. Обеспечьте контроль ввода.

print('\nВведите местоположение коня:')
x_horse = float(input('\tпо горизонтали: '))

while not (0 < x_horse < 0.8):
    x_horse = float(input('\t\tвведите корректное значение (0, 0.8): '))

x_horse = int(x_horse * 10)
y_horse = float(input('\tпо вертикали: '))

while not (0 < y_horse < 0.8):
    y_horse = float(input('\t\tвведите корректное значение (0, 0.8): '))

y_horse = int(y_horse * 10)
print('\nВведите местоположение точки на доске:')
x_point = float(input('\tпо горизонтали: '))

while not (0 < x_point < 0.8):
    x_point = float(input('\t\tвведите корректное значение (0, 0.8): '))

x_point = int(x_point * 10)
y_point = float(input('\tпо вертикали: '))

while not (0 < y_point < 0.8):
    y_point = float(input('\t\tвведите корректное значение (0, 0.8): '))

y_point = int(y_point * 10)
print('\nКонь в клетке (', x_horse, ',', y_horse, '). Точка в клетке (', x_point, ',', y_point, ').', sep='')

dx = abs(x_horse - x_point)
dy = abs(y_horse - y_point)

if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь не может ходить в эту точку.')
