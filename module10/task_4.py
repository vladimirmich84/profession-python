print('Задача 4. Простые числа\n')

# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на
# каждой итерации цикла. Одна итерация — одно число.

count_number = int(input('Введите количество чисел: '))
count = 0

for _ in range(count_number):
    number = int(input('Введите число: '))
    for divisor in range(2, int((number ** 0.5)) + 1):
        if number % divisor == 0:
            break
    else:
        if number > 1:
            count += 1

print('\nКоличество простых чисел в последовательности:', count)
