# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально и особенность данного языка программирования.
# ваш ответ может не совпадать с примером(может получитя 0,20))
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

size = int(input("Введите размер списка: "))
l_bound = int(input("Введите нижний предел: "))
u_bound = int(input("Введите верхний предел: "))

list_num = []
for i in range(0,size):
    item = random.randint(l_bound,u_bound - 1) + random.random()
    list_num.append(item)
list_frac = []
for j in range(0,len(list_num)):
    fraction_part = list_num[j] - int(list_num[j])
    list_frac.append(fraction_part)
min_frac = list_frac[0]
max_frac = list_frac[0]
for k in list_frac:
    if min_frac > k:
        min_frac = k
    if max_frac < k:
        max_frac = k
result = max_frac - min_frac
print(f"Исходник: {list_num}")
print(f"Дробные части: {list_frac}")
print(f"Мин: {min_frac}; макс: {max_frac}")
print(f"Исходник: {result}")
