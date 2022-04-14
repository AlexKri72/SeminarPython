# Найти расстояние между двумя точками пространства
import os
os.system("cls")

print('Введите 3 координаты первой точки через пробел: ', end=' ')
x1, y1, z1 = map(float, input().split())
print('Введите 3 координаты второй точки через пробел: ', end=' ')
x2, y2, z2 = map(float, input().split())


def distance(x1, y1, z1, x2, y2, z2):
    c = ((x2-x1)**2 + (y2-y1)**2+(z2-z1)**2)**0.5
    return c


print('Расстояние межде точками равно ',
      round(distance(x1, y1, z1, x2, y2, z2), 2), '\n')
