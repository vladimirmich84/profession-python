print('Задача 5. Текстовый редактор\n')

# Мы продолжаем разрабатывать новый текстовый редактор, и в этот раз нам поручили написать для него код,
# который считает количество любой буквы и любой цифры в тексте (а не только буквы Ы как раньше).

# Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое в нём количество цифр K и
# букв N.

# Функция должна вывести на экран информацию о найденных буквах и цифрах в определенном формате.


def count_letters(text):
    digit = input('\nКакую цифру ищем? ')
    letter = input('Какую букву ищём? ')
    k, n = 0, 0
    for symbol in text:
        if digit == symbol:
            k += 1
        elif letter == symbol:
            n += 1
    print('\nКоличество цифр', digit + ':', k)
    print('Количество букв', letter + ':', n)


count_letters(input('Введите текст: '))
