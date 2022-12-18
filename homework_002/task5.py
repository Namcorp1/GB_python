# Реализуйте алгоритм перемешивания списка.
# (рандомно поменять местами элементы списка между собой)
import random

size = int(input("Введите размер массива: "))
arr = [0] * size
i = 0
while i < size:
    arr[i] = random.randint(-size, size)
    i += 1
print(f"ДО перемешивания - {arr}") # распечатаем массив ДО, чтобы потом его уже менять можно было
sortarr = []
i = 0
while i < size:
    sortIndex = random.randint(0,len(arr) - 1)
    sortarr.append(arr[sortIndex])
    arr.remove(arr[sortIndex])
    i += 1
print(f"ПОСЛЕ перемешивания - {sortarr}")
