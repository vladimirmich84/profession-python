print('Задача 5. Часы\n')

# Напишите программу, которая получает на вход число n — количество минут, — затем считает:
# 1) сколько это будет в часах
# 2) сколько минут останется
# и выводит на экран эти два результата.

n = int(input('Введите количество минут: '))

hours = n // 60
minutes = n % 60

print('\nЧасов:', hours)
print('Минут:', minutes)
