# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import random
'''
Не до конца понял суть задачи (семинар смотрел в записи),
поэтому сделал так:
- определим вводом границы для выбора псевдослучайных чисел
- случайно определим точность округления результата
- процессом вычисления выберем простое умножение двух чисел
- в консоль выведем само выражение с результатом и округленный результат с указанием точности
'''
lBound = int(input("Введите нижний предел:"))
uBound = int(input("Введите верхний предел:"))
round_num = random.randint(1,10)
d = 10 ** -round_num
fullPart = random.randint(lBound,uBound)
number1 = fullPart + random.random()
number2 = fullPart + random.random()
result = number1 * number2
round_result = round(result, round_num)
print(f"{number1} * {number2} = {result}")
print(f"при d = {d}, result = {round_result}")
