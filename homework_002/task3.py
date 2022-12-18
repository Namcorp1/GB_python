# Задайте список из n чисел последовательности (1+1/n)**n
# и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input("Введите число: "))
sum = 0
result = []
for i in range(1,num+1):
    result.append(round((1 + 1 / i) ** i, 2))
    sum += round((1 + 1 / i) ** i, 2)
print(f"{num} -> sum = {sum}, {result}")
