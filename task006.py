# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.
import os
os.system("cls")

week = ['понедельник', 'вторник', 'среда',
        'четверг', 'пятница', 'суббота', 'воскресенье']
n = int(input('Введите число, обозначающее день недели: '))
while 7 < n or n < 1:
    n = int(input('Ошибка, число должно быть в диапазоне от 1 до 7. \nВведите число, обозначающее день недели: '))
else:
    print(f'Это', week[n-1], end=', ')
if 1 <= n <= 5:
    print('рабочий день!\n')
else:
    print('выходной день!\n')
