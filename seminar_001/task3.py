# Напишите программу, которая будет на вход принимать число N
# и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

num = int(input("Введите число: "))
result = []
start = -num
while start <= num:
    result.append(start)
    start += 1
print(result)