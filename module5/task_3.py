print('Задача 3. Поступление\n')

# В университете на особый факультет на направление кибернетики очень серьёзный конкурс — поступают только сильнейшие,
# первые десять человек из списка. Потом среди поступивших определяется, кто будет на стипендии. Для стипендии общий
# балл при поступлении должен составлять не менее 290.

# Напишите программу, которая получает на вход место студента в списке и его балл, а затем выводит соответствующие
# сообщения о поступлении и получении стипендии.

place = int(input('Введите место в списке поступающих: '))

if place <= 10:
    score = int(input('Введите количество баллов за экзамены: '))
    print('\nПоздравляем, Вы поступили!')
    if score >= 290:
        print('Бонусом Вам будет начисляться стипендия.')
    else:
        print('Но Вам не хватило баллов для стипендии.')
else:
    print('\nК сожалению, вы не поступили.')