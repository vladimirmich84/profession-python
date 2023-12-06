print('Задача 2. Финансовый отчёт\n')

# Васе пришло очередное задание — автоматизация финансовой отчётности.
# Звучит сложно, а на деле нужно просто написать код, который будет считать нужные для отчёта вычисления автоматически.
# Вычисления, которые нужно реализовать в программе: сумму дохода первых двух кварталов поделить на сумму последних
# двух кварталов, чтобы понять динамику роста или падения дохода.

# Алгоритм действий в программе:
# 1) Запросить у пользователя четыре числа.
# 2) Отдельно сложить два первых и два вторых.
# 3) Разделить первую сумму на вторую.
# 4) Вывести результат на экран.

first_quarter = int(input('Введите доход за первый квартал: '))
second_quarter = int(input('Введите доход за второй квартал: '))
third_quarter = int(input('Введите доход за третий квартал: '))
fourth_quarte = int(input('Введите доход за четвертый квартал: '))

sum_first_half_yeas = first_quarter + second_quarter
sum_second_half_yeas = third_quarter + fourth_quarte

income_dynamics = sum_first_half_yeas / sum_second_half_yeas

print('\nДинамика доходов:', income_dynamics)