print('Задача 4. Число наоборот')

# Вводится последовательность чисел, которая оканчивается нулём.
# Реализуйте функцию, которая принимает в качестве аргумента каждое число, переворачивает его и выводит на экран.
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.


def palindrome(n):
    while not (n % 10):
        print('', end='')
        n //= 10
    print('Число наоборот: ', end='')
    while n > 0:
        print(n % 10, end='')
        n //= 10
    print()


while True:
    n = int(input('\nВведите число: '))
    if n:
        palindrome(n)
    else:
        break

print('Программа завершена!')
