# 42.	Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции + , -, /, *. приоритет операций стандартный.
# Пример:
# 2+2 = > 4
# 1+2*3 = > 7
# 1-2*3 = > -5
# a.	Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример:
# 1+2*3 = > 7
# (1+2)*3 = > 9.
import os
os.system("cls")

str = '(1+2)*3-1+2*3'
print(str, ' = ', eval(str), '\n')
