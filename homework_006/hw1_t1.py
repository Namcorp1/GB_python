# Домашняя работа 1, задача 1:
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# первоначальное решение
# check = True
# while check:
#     num = int(input("Введите число: "))
#     if 1 <= num <= 7:
#         check = False
#     else:
#         print("Не существует такого дня недели!")
# if num == 6 or num == 7:
#     print(f"{num} -> да")
# else:
#     print(f"{num} -> нет")

# оптимизированное решение
def check_weekend(num_weekday):
    return f"{num_weekday} -> да" if num_weekday == 6 or num_weekday == 7 else f"{num_weekday} -> нет"

print(check_weekend(num))
