print('Задача 2. Лестница\n')

# Пользователь вводит число N. Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

n = int(input('Введите число N: '))
for row in range(1, n + 1):
    for _ in range(row):
        print(row, end='\t')
    print()
