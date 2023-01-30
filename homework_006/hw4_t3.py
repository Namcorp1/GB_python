#Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

# lBound = int(input("Введите нижний предел: "))
# uBound = int(input("Введите верхний предел: "))
# size = int(input("Введите кол-во элементов в списке: "))
# list_num = [None] * size
# for i in range(0,len(list_num)):
#     list_num[i] = random.randint(lBound,uBound)
# sort_list_num = []
# for j in range(0,len(list_num)):
#     check = True
#     for k in range(0,len(list_num)):
#         # двойное условие для проверки индекса элемента, так как при прогоне одного элемента через другие
#         # в любом случае будешь выкидывать элемент, так как при одинаковых индексах значение тоже одинаковые элементов
#         # второе условие для частного случая, когда одинаковые элементы стоят по краям списка
#         if k == j and k != len(list_num) - 1:
#             k += 1
#         if list_num[j] == list_num[k]:
#             check = False
#     if check:
#         sort_list_num.append(list_num[j])
# print(f"{list_num} - исходный список")
# print(f"{sort_list_num} - отфильтрованный список")

# новое решение
# создадим список отдельной функцией
def create_list(size, l_bound, u_bound):
    return [random.randint(l_bound, u_bound) for i in range(size)]  # list comprehension

def exclusive_item(arr): # функция для проверки списка методом map
    result = []
    for i in range(0, len(arr)):
        check = [j for j in arr] # каждый раз снова дублируем список
        check.pop(i) # чтобы проверять наличие повторяющихся элементов для каждого элемента исходного списка
        if arr[i] not in check:
            result.append(arr[i])
    return result
#клиентский код
list_num = create_list(size = 10, l_bound = 1, u_bound = 7) #создаем список
list_num_for_map = [[i for i in list_num]] #создаем список списков отдельно для метода map,
# так как он проверяет все итерируемые элементы и я не понял можно ли обойтись без этого
res = list(map(exclusive_item, list_num_for_map))
print(f'{list_num} - исходный список')
print(f'{exclusive_item(list_num)} - обработка функцией')
print(f'{res[0]} - через метод map') #выводим 0 список из списка списков, так как для проверки только 1 был список