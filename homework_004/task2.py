# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

input_num = int(input("Введите число: "))
number = input_num
simple_num = []
d = 2
while d * d <= number:
    if number % d == 0:
        simple_num.append(d)
        number //= d
    else:
        d += 1
if number > 1:
        simple_num.append(number)
print(f"{input_num} -> {simple_num}")