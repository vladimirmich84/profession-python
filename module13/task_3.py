print('Задача 3. Число наоборот 2\n')

# Пользователь вводит два числа — N и K. Напишите программу, которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке, затем складывает их, снова переворачивает и
# выводит ответ на экран.


def revers_number(n):
    revers_n = ''
    for symbol in str(n):
        revers_n = symbol + revers_n
    return int(revers_n)


def main():
    n = revers_number(int(input('Введите первое число: ')))
    k = revers_number(int(input('Введите второе число: ')))

    print('\nПервое число наоборот:', n)
    print('Второе число наоборот:', k)

    print('\nСумма', n + k)
    print('Сумма наоборот:', revers_number(n + k))


main()
