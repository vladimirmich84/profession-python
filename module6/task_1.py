print('Задача 1. Кубы чисел\n')

# В один из вечеров к Васе домой пришёл племянник и пожаловался на сложности с уроками математики: у него никак не
# получалось разобраться со степенями чисел. Вася решил помочь племяннику и написать программу, которая позволит
# наглядно увидеть возведение чисел в третью степень.

# Напишите программу, которая возводит в третью степень каждое число от 1 до N и выводит результат на экран.

n = int(input('Введите предельное число: '))
number = 1

while number <= n:
    print(number, 'в третьей степени -', number ** 3)
    number += 1