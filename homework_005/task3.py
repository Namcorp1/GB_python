# Создайте программу для игры в ""Крестики-нолики"".

# Крестики-нолики через координаты (как сам сообразил)
def tic_tac_toe(size_area = 3):
    # суть заключается в представлении игрового поля в виде списка позиций пустых ячеек и Х и О
    area = [i for i in range(1,10)]
    for i in range(0,size_area):
        for j in range(0,size_area):
            print(f" {area[3 * i + j]} ",end='')
        print()
    player = 1
    move = 0
    while move < size_area ** 2:
        # много условий для проверки победы одного из игроков перед ходом другого
        if (area[0] == 'X' and area[1] == 'X' and area[2] == 'X' or
        area[3] == 'X' and area[4] == 'X' and area[5] == 'X' or
        area[6] == 'X' and area[7] == 'X' and area[8] == 'X' or
        area[0] == 'X' and area[3] == 'X' and area[6] == 'X' or
        area[1] == 'X' and area[4] == 'X' and area[7] == 'X' or
        area[2] == 'X' and area[5] == 'X' and area[8] == 'X' or
        area[0] == 'X' and area[4] == 'X' and area[8] == 'X' or
        area[2] == 'X' and area[4] == 'X' and area[6] == 'X'):
            return print(f'Игрок {player} (O) проиграл:)')
        elif (area[0] == 'O' and area[1] == 'O' and area[2] == 'O' or
        area[3] == 'O' and area[4] == 'O' and area[5] == 'O' or
        area[6] == 'O' and area[7] == 'O' and area[8] == 'O' or
        area[0] == 'O' and area[3] == 'O' and area[6] == 'O' or
        area[1] == 'O' and area[4] == 'O' and area[7] == 'O' or
        area[2] == 'O' and area[5] == 'O' and area[8] == 'O' or
        area[0] == 'O' and area[4] == 'O' and area[8] == 'O' or
        area[2] == 'O' and area[4] == 'O' and area[6] == 'O'):
            return print(f'Игрок {player} (X) проиграл:)')
        else:
            # определение позиции хода игрока и постановка туда соответствующего символа
            if player == 1:
                point = int(input('Введите позицию для X: '))
                area[point - 1] = 'X'
                player = 2
            else:
                point = int(input('Введите позицию для O: '))
                area[point - 1] = 'O'
                player = 1
            for i in range(0, size_area):
                for j in range(0, size_area):
                    print(f" {area[3 * i + j]} ",end='')
                print()
        move += 1
    if (area[0] == 'X' and area[1] == 'X' and area[2] == 'X' or
            area[3] == 'X' and area[4] == 'X' and area[5] == 'X' or
            area[6] == 'X' and area[7] == 'X' and area[8] == 'X' or
            area[0] == 'X' and area[3] == 'X' and area[6] == 'X' or
            area[1] == 'X' and area[4] == 'X' and area[7] == 'X' or
            area[2] == 'X' and area[5] == 'X' and area[8] == 'X' or
            area[0] == 'X' and area[4] == 'X' and area[8] == 'X' or
            area[2] == 'X' and area[4] == 'X' and area[6] == 'X'):
        return print(f'Игрок {player} (O) проиграл:)')
    elif (area[0] == 'O' and area[1] == 'O' and area[2] == 'O' or
          area[3] == 'O' and area[4] == 'O' and area[5] == 'O' or
          area[6] == 'O' and area[7] == 'O' and area[8] == 'O' or
          area[0] == 'O' and area[3] == 'O' and area[6] == 'O' or
          area[1] == 'O' and area[4] == 'O' and area[7] == 'O' or
          area[2] == 'O' and area[5] == 'O' and area[8] == 'O' or
          area[0] == 'O' and area[4] == 'O' and area[8] == 'O' or
          area[2] == 'O' and area[4] == 'O' and area[6] == 'O'):
        return print(f'Игрок {player} (X) проиграл:)')
    return print("Ничья!")





tic_tac_toe()