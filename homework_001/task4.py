# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

check = True
while check:
    num = int(input("Введите номер четверти: "))
    if 1 <= num <= 4:
        check = False
    else:
        print("Такого номера четверти не существует!")
# в диапазоне необходимо указать (0, + бесконечность) или (- бесконечность, 0)
# однако не знаю как правильно это отобразить, поэтому сделал вывод через знаки сравнения
if num == 1:
    print(f"{num} четверть - x > 0, y > 0")
elif num == 2:
    print(f"{num} четверть - x < 0, y > 0")
elif num == 3:
    print(f"{num} четверть - x < 0, y < 0")
else:
    print(f"{num} четверть - x > 0, y < 0")
