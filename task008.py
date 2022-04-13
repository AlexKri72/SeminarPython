# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
import os
os.system("cls")

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))
if y == 0 and x == 0:
    print('Точка находится в начале координат, не принадлежит никакой плоскости!')
elif y == 0:
    print('Точка находится на оси X')
elif x == 0:
    print('Точка находится на оси Y')
elif x > 0 and y > 0:
    print('Точка расположена в первой координатной черверти!')
elif x < 0 and y > 0:
    print('Точка расположена во второй координатной черверти!')
elif x < 0 and y < 0:
    print('Точка расположена в третьей координатной черверти!')
else:
    print('Точка расположена в четвертой координатной черверти!')
print('\n')
