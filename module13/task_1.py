print('Задача 1. Урок информатики 2\n')

# В прошлый раз учитель написал программу, которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля. Задано положительное число x (x > 0). Ваша задача
# преобразовать его в формат плавающей точки, то есть x = a * 10 ** b, где 1 ≤ а < 10. Обратите внимание, что x теперь
# больше нуля, а не больше единицы. Обеспечьте контроль ввода.


def float_format(x):
    whole_part, fraction, temp_fraction = '', '', ''
    count_fraction = 0
    point_shift = 1

    for symbol in str(x):
        if not whole_part:
            if symbol != '0' and symbol != '.':
                whole_part = symbol
            point_shift -= 1
        elif symbol != '.':
            if symbol == '0':
                temp_fraction += symbol
            else:
                fraction += temp_fraction + symbol
                temp_fraction = ''
            count_fraction += 1
        if symbol == '.':
            point_shift = count_fraction

    if fraction == '' or int(fraction) == 0:
        fraction = '0'
    if point_shift != 0:
        fraction += ' * 10 ** ' + str(point_shift)
    elif count_fraction > 0 and float(x) >= 10:
        fraction += ' * 10 ** ' + str(count_fraction - point_shift)
    return whole_part + '.' + fraction


def main():
    x = input('Введите положительное число x (x > 0): ')
    while float(x) <= 0:
        x = input('\tвведите корректное значение: ')
    print('Формат плавающей точки: x =', float_format(x))


main()
