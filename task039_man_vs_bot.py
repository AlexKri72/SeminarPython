# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
#   На столе лежит 2021 конфета.
#   Играют два игрока делая ход друг после друга.
#   Первый ход определяется жеребьёвкой.
#   За один ход можно забрать не более чем 28 конфет.
#   Все конфеты оппонента достаются сделавшему последний ход.
#   Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#       a) Добавьте игру против бота
#       b) Подумайте, как наделить бота "интеллектом"

# ОТВЕТ: Чтобы выиграл первый игрок ему нужно первым ходом забрать остаток от целочисленного деления
# имеющегося количества конфет на то, которое можно взять за 1 ход максимально + 1
# В дальнейшем первому игроку нужно повторять стратегию
# Пример :  2021 % ( 28 + 1 ) = 20 , первый игрок первым ходом должен взять 20 конфет.
#           если вторым ходом второй игрок взял 10 конфет, то первый должен взять 28 + 1 - 10 = 19

# Игра с конфетами. Дано N конфет.
# Каждый игрок за каждый ход может взять не более M конфет.
# Побеждает игрок,забравший последнюю конфету.

# man vs bot
from random import *
import os
os.system("cls")

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!"\n'
            'Основные правила игры: \n'
            'Нам будет дано некоторое количество конфет,\n'
            'за один ход мы можем взять не более определённого количества, \n'
            'о котором мы с вами договоримся. \n'
            'Итак, начнём!\n')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def candy(n):  # выбираем окончание для слова конфеты
    if n == 1 or (n % 10 == 1 and n > 20):
        return 'а'
    elif 1 < n < 5 or 1 < n % 10 < 5:
        return 'ы'
    else:
        return ''


def introduce_players():
    player1 = input('Давайте познакомися. Как Вас зовут? ')
    player2 = 'Робик'
    print(f'Очень приятно, меня зовут {player2}\n')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать? '))
    m = int(input('Сколько максимально будем брать конфет за один ход? '))

    first = input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу')
    if first != '1':
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):

    count = rules[2]  # кто ходит первым

    while rules[0] > 0:
        max = rules[1]
        if max > rules[0]:  # максимальное взятие не должно превышать остаток
            max = rules[0]
        if not count % 2:   # если ход бота, то он случайным образом забирает конфеты
            move = randint(1, max)
            print(f'Я забираю {move} ')
        else:
            # просим человека взять конфеты
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{candy(rules[1])}, у нас всего {rules[0]} конфет{candy(rules[0])}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] -= move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{candy(rules[0])}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]


print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!\n')
