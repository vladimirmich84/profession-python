print('Задача 4. Первая цифра\n')

# Дано положительное действительное число X. Выведите его первую цифру после десятичной точки. При решении этой
# задачи нельзя пользоваться условной инструкцией, циклом или строками

x = float(input('Введите действительное число: '))
x = abs(int(x)*10 - int(x*10))

print('Первая цифра после десятичной точки:', x)
