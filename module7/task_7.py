print('Задача 7. Пропавшая карточка\n')

# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера
# оставшихся карточек.

# Вводится число N, далее еще N − 1 чисел: номера оставшихся карточек (различные числа от 1 до N). Программа должна
# вывести номер потерянной карточки.

n = int(input('Введите количество карточек: '))
card = n

for i in range(1, n):
    card += i - int(input('Введите номер оставшейся карточки: '))

print('\nНомер пропавшей карточки:', card)
