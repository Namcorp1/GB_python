# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

check = True
while check:
    num = int(input("Введите число: "))
    if 1 <= num <= 7:
        check = False
    else:
        print("Не существует такого дня недели!")
if num == 6 or num == 7:
    print(f"{num} -> да")
else:
    print(f"{num} -> нет")