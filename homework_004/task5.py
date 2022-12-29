# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# !!! Задача пока решена только для случаев когда степень 1 и 2 многочлена одинакова.
# К сожалению пока не хватает времени делать и красиво и универсально (конец года).

data1 = open('for_task5/polynomial_1.txt','r')
str_data1 = data1.read()
data2 = open('for_task5/polynomial_2.txt','r')
str_data2 = data2.read()

# функция вычлинения коэффициентов из строки
def poli_coef(str1):
    factors1 = []
    factor_str = ""
    start = 0
    a = 0
    if str1[0] == '-':
        start = 0
        a = 1
    for i in range(a,len(str1)):
        if str1[i] == '+' or str1[i] == '-':
            if str1[i-1] == 'x':
                finish = i - 1
            else:
                finish = i-3
            for k in range(start, finish):
                factor_str += f'{str1[k]}'
            if factor_str == '+' or factor_str == '-':
                factor_str += '1'
            factors1.append(factor_str)
            factor_str = ""
            start = i
        if str1[i] == '=':
            for l in range(start,i):
                factor_str += f'{str1[l]}'
            factors1.append(factor_str)
            factor_str = ""
    return factors1

# функция для преобразования строковых коэф-ов в числовые
def convert_to_int(list_str):
    list_num = []
    for i in list_str:
        list_num.append(int(i))
    return list_num

# функция для складывания коэффициентов
def sum_koef(term1,term2):
    sum = []
    for i in range(0,len(term1)):
        sum.append(term1[i] + term2[i])
    return sum

# вывод данных и суммирование 2 наборов коэффициентов многочленов
terms1 = poli_coef(str_data1)
terms2 = poli_coef(str_data2)
koef1 = convert_to_int(terms1)
koef2 = convert_to_int(terms2)
factors = sum_koef(koef1,koef2)

# формирование итогового многочлена
res = ""
for j in range(0,len(factors)):

    if factors[j] != 1:
        if factors[j] < 0:
            factor = f"{factors[j]}"
        else:
            factor = f"+{factors[j]}"
    else:
        factor = ""
    # для 0, где весь член многочлена будет отсутствовать
    if factors[j] == 0:
        polynomial = ""
    else:
        # для заключительного многочлена мы опускаем сам Х, так как Х в нулевой степени это 1 и можно опустить
        if j == len(factors) - 1:
            polynomial = f"{factor}"
        # для предпоследнего члена многочлена также степень в размере 1 можно опустить
        elif j == len(factors) - 2:
            polynomial = f"{factor}x"
        # для остального строим строковую конструкцию члена многочлена
        else:
            polypow = len(factors) - 1 - j
            polynomial = f"{factor}x^{polypow}"
    res += polynomial
res += "=0"
if res[0] == '+':
    res = res[1:]
final_file = open('for_task5/result.txt','w')
final_file.writelines(res)
final_file.close()

print(f"Первый многочлен: {str_data1}")
print(f"Второй многочлен: {str_data2}")
print(f"Сумма: {res}")
print("Результат записан в файле 'result.txt' в папке 'for_task5'.")
