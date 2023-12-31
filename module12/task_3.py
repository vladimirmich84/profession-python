print('Задача 3. Апгрейд калькулятора\n')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные
# арифметические действия. Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму
# его цифр, максимальную или минимальную цифру.

# Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.


def operations_digits():
    n = int(input('\nВведите число: '))
    operation = input('Введите операцию: ')
    if operation == 'сум':
        sum_digits(n)
    elif operation == 'макс':
        max_digits(n)
    elif operation == 'мин':
        min_digits(n)
    operations_digits()


def sum_digits(n):
    sum_dig = 0
    while n > 0:
        sum_dig += n % 10
        n //= 10
    print('Сумма цифр:', sum_dig)


def max_digits(n):
    max_dig = 0
    while n > 0:
        if max_dig < n % 10:
            max_dig = n % 10
        n //= 10
    print('Максимальная цифра:', max_dig)


def min_digits(n):
    min_dig = 9
    while n > 0:
        if min_dig > n % 10:
            min_dig = n % 10
        n //= 10
    print('Минимальная цифра:', min_dig)


print('Bывод суммы ("сум") цифр числа, максимальной ("макс") или минимальной ("мин") цифры.')
operations_digits()
