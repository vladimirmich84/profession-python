print('Задача 7. Пирамидка 2\n')

# Напишите программу, которая получает на вход количество уровней пирамиды и выводит их на экран

#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input('Введите кол-во уровней пирамиды: '))
number = 1

for level in range(height):
    print(end=(height - level - 1) * '\t')
    for _ in range(level + 1):
        print(number, end=2 * '\t')
        number += 2
    print()
