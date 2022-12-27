# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input("Введите максимальную степень многочлена: "))
uBound = int(input("Введите верхний предел для коэффициентов: "))
# создадим список знаков для коэффициентов
operations = ["-","+"]
factors = []
# создадим массив коэффициентов от 0 до верхнего введенного предела
# отрицательные значения не нужны, так как мы будем случайно выбирать знак
for i in range(0,k):
    factors.append(random.randint(0, uBound))
result = ""
for j in range(0,len(factors)):
    # теперь будем составлять каждый член многочлена
    oper = operations[random.randint(0, 1)]
    factor = ""
    # условие для коэф. равного 1, его не к чему записывать, поэтому отдельная запись, где 1 опускается
    if factors[j] != 1:
        factor = f"{factors[j]}"
    # тоже самое только для 0, где весь член многочлена будет отсутствовать
    if factors[j] == 0:
        polynomial = ""
    else:
        # для заключительного многочлена мы опускаем сам Х, так как Х в нулевой степени это 1 и можно опустить
        if j == len(factors) - 1:
            polynomial = f" {oper} {factor}"
        # для предпоследнего члена многочлена также степень в размере 1 можно опустить
        elif j == len(factors) - 2:
            polynomial = f" {oper} {factor}x"
        # для остального строим строковую конструкцию члена многочлена
        else:
            polypow = len(factors) - 1 - j
            if oper == "+" and j == 0:
                polynomial = f" {factor}x^{polypow}"
            else:
                polynomial = f" {oper} {factor}x^{polypow}"
    result += polynomial
# и в конце добалвяем равенство многочлена нулю
result += " = 0"
print(f"{factors} - список коэффициентов.")
print(result)
data = open('polynomial.txt', 'w')
data.writelines(f"{factors} - коэффициенты многочлена.\n")
data.writelines(f"{result}\n")
data.close()

