print('Задача 6. НОД\n')

# Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def nod(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif b < a:
        a, b = b, a

    while b % a:
        b = b % a
        a, b = b, a

    return a


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

print('НОД(' + str(number_1) + ', ' + str(number_2) + ') =', nod(number_1, number_2))
