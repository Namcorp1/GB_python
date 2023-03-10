# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# пришлось делать импорт библиотеки работы с рациональными числами
# т.к. при использовании моего алгоритма, при вводе 0.56 из-за того,
# что числа с плавающей точкой являются неточными, результат был некорректен (12)
from decimal import*

data = Decimal(input("Введите число: "))
num = data # сделано для красоты в выводе, чтобы оставить исходник вводимого числа
while int(num) != num:
    num *= 10
n = int(num)
result = 0
while n > 0:
    result += n % 10
    n = (n - n % 10) / 10
print(f"{data} -> {int(result)}")