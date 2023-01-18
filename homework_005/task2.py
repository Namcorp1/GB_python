# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

def candy_game(candy_count = 2021, max_one_move = 28):
    player_1 = 0
    player_2 = 0
    player = 2
    total_move = 0
    remainder = candy_count
    # кол-во конфет в первом ходе должно быть таким,
    # чтобы осталось конфет кратно максимальному кол-ву для одного хода +1,
    # тогда после хода второго игрока, первому игроку остается брать кол-во конфет до максимального + 1
    if candy_count % (max_one_move + 1) == 0:
        first_move = max_one_move + 1
    else:
        first_move = candy_count % (max_one_move + 1)
    remainder -= first_move # выигрышный первый ход первого игрока
    while remainder > 0:
        if player == 1:
            player_1 = int(input())
            remainder -= player_1
            player = 2
            total_move += 1
        elif player == 2:
            player_2 = random.randint(1,max_one_move)
            remainder -= player_2
            print(f"Второй игрок взял {player_2} конфет")
            print(f"Осталось {remainder} конфет")
            player = 1
            total_move += 1
    if player == 2: # для вывода в консоль победителя, так как у нас в цикле было переключение игроков
        player = 1
    else:
        player = 2
    print(f"{first_move} - столько надо взять конфет первому игроку, чтобы победить в игре")
    print(f"Игрок {player} - победитель")
    print(f"{total_move} - всего ходов")

candy_game(100,9)