print('Задача 1. Я стал новым пиратом!\n')

# Старому капитану нужно пополнить команду, но на корабль попадут только достойные! Он отобрал десять человек. Те,
# кто крикнет слово «Карамба», попадут на борт.

# Пользователь вводит десять слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».

low_word = 'Карамба'
up_word = 'карамба'
count = 0

for i in range(1, 11):
    word = input('Выкрик ' + str(i) + ' кандидата в пираты: ')
    if (word == low_word) or (word == up_word):
        count += 1

print('\nКоличество достойных в пираты:', count)
