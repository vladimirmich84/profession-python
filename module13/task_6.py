print('Задача 6. Яйца\n')

# В рамках программы колонизации Марса компания «Спейс Инжиниринг» вывела особую породу черепах, которые, по задумке,
# должны размножаться, откладывая яйца в марсианском грунте. Откладывать яйца слишком близко к поверхности опасно
# из-за радиации, а слишком глубоко — из-за давления грунта и недостатка кислорода. Вообще, факторов очень много,
# но специалисты проделали большую работу и предположили, что уровень опасности для черепашьих яиц рассчитывается по
# формуле:
#   D = x**3 − 3x**2 − 12x + 10,
#     где x — глубина кладки в метрах,
#         D — уровень опасности в условных единицах.
# Для тестирования гипотезы нужно взять пробу грунта на безопасной, согласно формуле, глубине.
#
# Напишите программу, находящую такое значение глубины "х", при котором уровень опасности как можно более близок к
# нулю. На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля, а программа должна
# рассчитать приблизительное значение "х", удовлетворяющее этому отклонению. Известно, что глубина точно больше нуля
# и меньше четырёх метров.
#
# Обеспечьте контроль ввода.


def danger_level(x):
    return x ** 3 - 3 * x ** 2 - 12 * x + 10


def depth(d):
    min_depth, max_depth = 0, 4
    while abs(danger_level((min_depth + max_depth) / 2)) >= d:
        if abs(danger_level(min_depth)) > abs(danger_level(max_depth)):
            min_depth = (min_depth + max_depth) / 2
        else:
            max_depth = (min_depth + max_depth) / 2
    return (min_depth + max_depth) / 2


def main():
    d = float(input('Введите максимально допустимый уровень опасности: '))
    print('Приблизительная глубина безопасной кладки:', str(depth(d)) + 'м')


main()
