# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

# первоначальное решение
# size = int(input("Введите размер списка: "))
# l_bound = int(input("Введите нижний предел: "))
# u_bound = int(input("Введите верхний предел: "))
#
# list_num = []
# for i in range(0,size):
#     item = random.randint(l_bound,u_bound)
#     list_num.append(item)
# sum = 0
# for j in range(1,size,2):
#     sum += list_num[j]
# print(list_num)
# print(f"Сумма элементов на нечетных позициях - {sum}")

# новое решение
def sum_odd_position(size, l_bound, u_bound):
    positions = list(range(0,size)) # создадим список позиций списка
    list_num = [random.randint(l_bound, u_bound) for i in range(size)] # список псевдослучайных чисел таким же размером
    res = dict(zip(positions,list_num))
    # объединим это в словарь (немного костыль, но только так я придумал,
    # чтобы в следующей строке вычленить элементы на нечетных позициях)
    result = sum([res[key] for key in res if key % 2 == 1]) # суммируем элементы на нечетных позициях
    print(list_num)
    print(f"Сумма элементов на нечетных позициях - {result}")

print(sum_odd_position(size = 10,l_bound = 0, u_bound = 15))
