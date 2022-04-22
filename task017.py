# Задать список из N элементов, заполненных числами из[-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

import os
import random
os.system("cls")

n = random.randint(16, 26)
list = []
for i in range(-n, n+1):
    list.append(i)
print('1 список, list: ', list)

with open('file.txt', 'w') as data:
    for i in range(int(n/2)):
        data.write(f'{random.randint(0, n*2)}\n')


def read2list(file):    # читает файл в список
    file = open(file, 'r')
    lines = file.readlines()    # читаем все строки и удаляем переводы строк
    lines = [line.rstrip('\n') for line in lines]
    file.close()
    return lines


lines = read2list('file.txt')
print('2 список, lines: ', lines)

total = 1
for i in lines:
    total *= int(list[int(i)])
print('Total= ', total)
