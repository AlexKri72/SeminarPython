#	Вывести на экран числа от -N до N
import os
os.system("cls")

n = int(input('Введите любое целое число: '))
m = -n
while m<=n:
    print(m, end=' ')
    m+=1
print('\n')
