# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке
# (пример n=4, lst1=[4,-2,1,3] - список на основе n, а позиции элементов lst2=[3,1].
import random

num = int(input("Введите число: "))
lst1 = []
for i in range(0, num):
    lst1.append(random.randint(-num, num))
# немного сложная конструкция ниже, сделана для того,
# чтобы во второй список позиции, которые надо перемножить были разные, а не, например, [2, 2]
lst2 = [random.randint(0, len(lst1) - 1)]
for i in range(1, 2):
    point = random.randint(0, len(lst1) - 1)
    while point == lst2[0]:
        point = random.randint(0, len(lst1) - 1)
    lst2.append(point)
# находим произведение элементов первого списка под номерами позиций из второго списка
multi = 1
for i in lst2:
    multi *= lst1[i]
print(f"{lst1} and {lst2} -> {multi}")

