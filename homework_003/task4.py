# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите число: "))
check = bin(number) # сделаем коротким ходом конвертацию чтобы проверить себя
dif_number = number
num_bin = ""
while dif_number != 0: # здесь мы найдем все 1 и 0, однако они будут в обратной последовательности
    n_bin = dif_number % 2
    num_bin += f"{n_bin}"
    dif_number = int(dif_number / 2)
result = ""
for i in range(0,len(num_bin)): # развернем, то что получилось в предыдущем цикле
    result += f"{num_bin[len(num_bin) - 1 - i]}"

print(f"{number} -> {check}")
print(f"{number} -> {result}")

