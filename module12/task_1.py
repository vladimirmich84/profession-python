print('Задача 1. Сумма чисел\n')

# Напишите функцию summa_n, которая принимает одно целое положительное число N и выводит сумму всех чисел от 1 до N
# включительно.


def summa_n(n):
    for num in range(n):
        n += num
    return n


n = int(input('Введите число: '))
print('Я знаю, что сумма чисел от', 1, 'до', n, 'равна', summa_n(n))
