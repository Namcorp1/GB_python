# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
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
# result = []
# if len(list_num) % 2 == 1:
#     half = int(len(list_num)/2) + 1
# else:
#     half = int(len(list_num)/2)
# for j in range(0,half):
#     multiply = list_num[j] * list_num[len(list_num) - 1 - j]
#     result.append(multiply)
# print(f"{list_num} => {result}")

def multiply_double_num(size, l_bound, u_bound):
    list_num = [random.randint(l_bound, u_bound) for i in range(size)] # list comprehension
    first_half = list_num[:int(size / 2)]
    if size % 2 == 0:
        second_half = list_num[size:int(size / 2)-1:-1]
    else:
        second_half = list_num[size:int(size / 2):-1]
    result = [first_half[i] * second_half[i] for i in range(0,int(size/2))] # list comprehension
    if size % 2 == 1:
        result.append(list_num[int(size / 2)])
    print(f"{list_num} => {result}")

print(multiply_double_num(5,9,20))

