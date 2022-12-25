# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

size = int(input("Введите размер списка: "))
l_bound = int(input("Введите нижний предел: "))
u_bound = int(input("Введите верхний предел: "))

list_num = []
for i in range(0,size):
    item = random.randint(l_bound,u_bound)
    list_num.append(item)
sum = 0
for j in range(1,size,2):
    sum += list_num[j]
print(list_num)
print(f"Сумма элементов на нечетных позициях - {sum}")
