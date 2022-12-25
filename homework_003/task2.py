# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random

size = int(input("Введите размер списка: "))
l_bound = int(input("Введите нижний предел: "))
u_bound = int(input("Введите верхний предел: "))

list_num = []
for i in range(0,size):
    item = random.randint(l_bound,u_bound)
    list_num.append(item)
result = []
if len(list_num) % 2 == 1:
    half = int(len(list_num)/2) + 1
else:
    half = int(len(list_num)/2)
for j in range(0,half):
    multiply = list_num[j] * list_num[len(list_num) - 1 - j]
    result.append(multiply)
print(f"{list_num} => {result}")