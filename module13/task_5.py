print('Задача 5. Маятник\n')

# Известно, что амплитуда качающегося маятника с каждым разом затухает на 8,4% от амплитуды прошлого колебания. Если
# качнуть маятник, то, строго говоря, он не остановится никогда, просто амплитуда будет постоянно уменьшаться до тех
# пор, пока мы не сочтём такой маятник остановившимся.

# Напишите программу, определяющую, сколько раз качнётся маятник, прежде чем он, по нашему мнению, остановится.

# Программа получает на вход начальную амплитуду колебания в сантиметрах и конечную амплитуду его колебаний,
# которая считается остановкой маятника.


def pendulum_oscillations(initial, stop, attenuation):
    count = 0
    while initial > stop:
        initial -= initial * attenuation
        count += 1
    return count


def main():
    attenuation = 0.084
    initial_amplitude = float(input('Введите начальную амплитуду: '))
    stopping_amplitude = float(input('Введите амплитуду остановки: '))
    oscillations = pendulum_oscillations(initial_amplitude, stopping_amplitude, attenuation)

    print('Маятник считается остановившимся через', oscillations, 'колебаний')


main()
