print('Задача 8. Яма\n')

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор
# ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу, которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

n = int(input('Введите число: '))
next_n = n - 1
number_digits = 0
half_points = 0

while next_n > 0:
    half_points += next_n
    next_n -= 9 * 10 ** number_digits
    number_digits += 1

for layer in range(n, 0, -1):
    if layer == 10 ** (number_digits - 1):
        number_digits -= 1
    for number_left in range(n, layer - 1, -1):
        print(number_left, end='')
    print(half_points * 2 * '.', end='')
    for number_right in range(layer, n + 1):
        print(number_right, end='')
    half_points -= number_digits
    print()
