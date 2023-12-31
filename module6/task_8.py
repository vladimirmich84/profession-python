print('Задача 8. Игра «Компьютер угадывает число»\n')

# Поменяйте мальчика и компьютер из прошлой задачи местами. Теперь мальчик загадывает число между 1 и 100
# (включительно). Компьютер может спросить у мальчика: «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
#   1 — равно,
#   2 — больше,
#   3 — меньше.

# Напишите программу, которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

low = 1
high = 100
count = 0

while True:
    count += 1
    n = (low + high) // 2
    x = int(input('Твое число равно (1), больше (2) или меньше (3), чем число ' + str(n) + '? '))

    if x == 1:
        print('Число угадано! Количество попыток:', count)
        break
    elif x == 2:
        low = n + 1
    elif x == 3:
        high = n - 1
