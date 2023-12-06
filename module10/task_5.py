print('Задача 5. Наибольшая сумма цифр\n')

# Вводится N чисел. Среди натуральных чисел, которые были введены, найдите наибольшее по сумме цифр. Выведите на
# экран это число и сумму его цифр.

count_number = int(input('Введите количество чисел: '))
max_digit_sum, number = 0, 0

for _ in range(count_number):
    new_number = input('Введите число: ')
    digit_sum = 0
    for digit in new_number:
        digit_sum += int(digit)
    if max_digit_sum < digit_sum:
        max_digit_sum = digit_sum
        number = new_number

print('\nУ числа', number, 'наибольшая сумма цифр равная', max_digit_sum)
