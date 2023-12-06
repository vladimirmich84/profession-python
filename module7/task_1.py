print('Задача 1. Должники\n')

# В базе банка хранятся данные и должников, и законопослушных граждан. Каждому человеку система присваивает свой
# номер. У нас есть случайная выборка из десяти номеров. Правда, иногда база глючит и выдаёт номер с отрицательным
# значением. А ещё по статистике, которую собрал наш «МирПрогБанк», каждый второй пользователь брал кредит и не
# выплатил его вовремя, то есть является должником.

# Напишите программу, которая при вводе десяти чисел определяет, сколько из них являются одновременно чётными и
# положительными.

count = 0

print('Введите 10 чисел')

for i in range(1, 11):
    number = int(input(str(i) + ' число: '))
    if (not number % 2) and (number > 0):
        count += 1

print('\nКол-во одновременно четных и положительных:', count)
