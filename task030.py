# Вычислить число π c заданной точностью d Пример: при d = 0.001,π = 3.141.
# 10^(-1)  ≤  d  ≤  10^(-10)  (до 10 знаков после запятой)

import os
from math import pi
from random import*
os.system("cls")

d = randint(1, 10)
print('Точность вывода = ', d, 'после запятой')

a = 1.0
for i in range(d):
    a = a/10.0

# переводим точность в вещественное число, по условию задачи
print('Точность вывода = ', round(a, d))

count = 0
while a < 1:  # считаем сколько нужно знаков после запятой
    a *= 10
    count += 1

print('Пи = ', round(pi, count), '\n')
