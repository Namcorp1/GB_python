# a = 37
# b = 1.47
# #print(type(a))

# # None присовить можно если заранее нету значения для переменной
# value = None
# print(type(value))
# value = 777
# print(type(value))

# t = "My name is Nikita"
# print(a, '-', b, '-', t)
# print('{} - {} - {}'.format(a,b,t))
# # добавив индексы можно упорядочить вывод переменных
# print('{2} - {0} - {1}'.format(a,b,t))
# print(f'{a} - {b} - {t}')

# b = True #True и False пишутся с большой буквы
# print(b)

# listI = [1, 3, 5, 7]
# listS = ['1','three','5','seven']
# print(listI,listS)

# по умолчанию в input мы работаем со строками, 
# поэтому берем в скобки и добавляем в начале 
# числовой тип int или float
# print('Введите первое число')
# num1 = float(input())
# print('Введите второе число')
# num2 = float(input())
# sum = num1+num2
# print(sum)

# особенности в хранения типа данных
# выводят не совсем корректный результат, 
# поэтому надо использовать функцию округления
# x = 1.3
# y = 3
# c1 = x * y
# c2 = round(x * y,1)
# print(c1,c2)

# Логические операторы

# examlpeList = [1,43,55,109]
# print(55 in examlpeList)

# оператор if else
# например, найдем минимальное число из двух чисел

# n1 = int(input('number 1 = '))
# n2 = int(input('number 2 = '))
# if n1 < n2:
#     print(n1)
# else:
#     print(n2)

# цикл while
# разворот числа
# original = int(input('Введите число: '))
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# цикл for
list = [1,3,5,7,9]
# range[11] - числа от 0 до 10 (включительно), 11 не входит в диапазон
# range[1,11] - первое число ОТ, второе ДО (не включительно это число)
# range[1,11,2] - третье число показывает итерации (какой будет шаг числа), вывод будет 1,3,5,7,9
r = range(1,10,2)
for i in r:
    print(i*10)