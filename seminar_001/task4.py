# Напишите программу, которая будет принимать на вход дробь
# и показывать первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

num = float(input("Введите число: "))
num *= 10
numRound = round(num)
if numRound > num:
    numRound -= 1
result = numRound % 10
if result == 0:
    print("Нет")
else:
    print(result)