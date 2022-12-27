#Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

lBound = int(input("Введите нижний предел: "))
uBound = int(input("Введите верхний предел: "))
size = int(input("Введите кол-во элементов в списке: "))
list_num = [None] * size
for i in range(0,len(list_num)):
    list_num[i] = random.randint(lBound,uBound)
sort_list_num = []
for j in range(0,len(list_num)):
    check = True
    for k in range(0,len(list_num)):
        # двойное условие для проверки индекса элемента, так как при прогоне одного элемента через другие
        # в любом случае будешь выкидывать элемент, так как при одинаковых индексах значение тоже одинаковые элементов
        # второе условие для частного случая, когда одинаковые элементы стоят по краям списка
        if k == j and k != len(list_num) - 1:
            k += 1
        if list_num[j] == list_num[k]:
            check = False
    if check:
        sort_list_num.append(list_num[j])
print(f"{list_num} - исходный список")
print(f"{sort_list_num} - отфильтрованный список")