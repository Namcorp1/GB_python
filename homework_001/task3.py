# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

check = True
# проверка на ввод 0 для х
while check:
    x = int(input("Введите x: "))
    if x == 0:
        print("Координаты не должны быть нулевыми!")
    else:
        check = False
# проверка на ввод 0 для у
while not check:
    y = int(input("Введите y: "))
    if y == 0:
        print("Координаты не должны быть нулевыми!")
    else:
        check = True
if x > 0 and y > 0:
    print(f"x = {x}, y = {y} -> 1")
elif x < 0 and y > 0:
    print(f"x = {x}, y = {y} -> 2")
elif x < 0 and y < 0:
    print(f"x = {x}, y = {y} -> 3")
else:
    print(f"x = {x}, y = {y} -> 4")

