print('Задача 6. Замечательные числа\n')

# Напишите программу, которая находит и выводит все двузначные числа, которые равны утроенному произведению своих
# цифр. К таким относятся, например, 15 и 24.

for number in range(10, 100):
    if number == (number // 10) * (number % 10) * 3:
        print(number, '->', str(number // 10) + '*' + str(number % 10) + '*' + '3 =', number)
