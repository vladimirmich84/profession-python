print('Задача 8. Максимальное число (по желанию)\n')

# Пользователь вводит три числа.
# Напишите программу, которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a < b:
    a = b
elif a < c:
    a = c

print('\nМаксимальное число:', a)
