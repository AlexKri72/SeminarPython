# Подсчитать сумму цифр в вещественном числе.
import os
import random
os.system("cls")

# задаем случайное вещественное число из диапазона
a = random.uniform(1, 1001)
print('Задано число:', a)

a = str(a).replace('.', '')     # переводим в строковый тип, убираем точку

summa = sum(map(int, a))        # переводим в числовой тип, считаем сумму
print('Сумма цифр данного числа равна:', summa, '\n')
