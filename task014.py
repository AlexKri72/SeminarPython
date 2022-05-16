# Подсчитать сумму цифр в вещественном числе.
import os
import random
os.system("cls")

# задаем случайное вещественное число из диапазона
a = random.uniform(1, 1001)
print('Задано число:', a)

summa = sum(map(int, str(a).replace('.', '')))
print('Сумма цифр данного числа равна:', summa, '\n')
