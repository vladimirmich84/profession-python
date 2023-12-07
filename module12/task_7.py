print('Задача 7. Недоделка\n')


# Вы пришли на работу в контору по разработке игр, целевая аудитория которых - дети и их родители. У прошлого
# программиста было задание сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них. Однако
# программист, на место которого вы пришли, перед увольнением не успел сделать эту задачу и оставил только небольшой
# шаблон проекта. Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
#   программа запрашивает у пользователя строку и выводит: победил он или проиграл,
#   камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
#   программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors():
    print('\nСделайте выбор: камень, ножницы или бумага.')

    first = input('\tПервый игрок: ')
    while first not in ('камень', 'ножницы', 'бумага'):
        first = input('\t\tвведите корректное значение: ')

    second = input('\tВторой игрок: ')
    while second not in ('камень', 'ножницы', 'бумага'):
        second = input('\t\tвведите корректное значение: ')

    if first == second:
        print('Ничья')
    elif (first == 'камень' and second == 'ножницы' or
          first == 'ножницы' and second == 'бумага' or
          first == 'бумага' and second == 'камень'):
        print('Победил первый игрок')
    else:
        print('Победил второй игрок')


def guess_the_number():
    number, count = 7, 0

    while True:
        user_number = int(input('\nВведите число: '))
        count += 1
        if user_number == number:
            print('\tВы угадали! Число попыток:', count)
            break
        elif user_number > number:
            print('\tЧисло больше, чем нужно. Попробуйте ещё раз!')
        else:
            print('\tЧисло меньше, чем нужно. Попробуйте ещё раз!')


def main_menu():
    print('\n1. Камень, ножницы, бумага', '2. Угадай число', '0. Выход', sep='\n')
    n = int(input('Выберите игру: '))

    while n not in (0, 1, 2):
        n = int(input('\tвведите корректное значение: '))
    if n == 1:
        rock_paper_scissors()
    elif n == 2:
        guess_the_number()
    elif n == 0:
        return
    main_menu()


main_menu()

print('Программа завершена!')
