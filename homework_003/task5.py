# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input("Введите число: "))
def fib(number):
    if number in [1, 2]:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)
num_fibo = []
for i in range(1, number + 1): # составляем список чисел Фибоначи
    num_fibo.append(fib(i))
result = [0] * (2*len(num_fibo) + 1)
for j in range(0,len(num_fibo)):
    result[j] = -1 * num_fibo[len(num_fibo) - 1 - j]
    result[len(result) - 1 - j] = num_fibo[len(num_fibo) - 1 - j]
print(num_fibo)
print(result)