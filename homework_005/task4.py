# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_coding(file_path): # функция RLE кодирования
    data = open(file_path,'r')
    result = open('for_task4/coding.txt','w')
    count = 1
    for line in data:
        letter_coding = ''
        i = 0
        for j in range(i + 1,len(line)):
            if line[j] == line[i]:
                count += 1
            else:
                letter_coding += f'{count}{line[i]}'
                count = 1
                i = j
        result.write(f'{letter_coding}\n')
    data.close()
    result.close()
    return result

def rle_decoding(file_path): # функция RLE декодирования
    data = open(file_path, 'r')
    result = open('for_task4/decoding.txt', 'w')
    count = 1
    for line in data:
        str_res = ''
        nums_str = ''
        for i in range(0,len(line)):
            if line[i].isalpha():
                nums_str += ','
            else:
                nums_str += line[i]
        nums_str = nums_str.split(',')
        letter_str = [i for i in line if i.isalpha()]
        for i in range(0,len(letter_str)):
            str_res += f'{letter_str[i]}' * int(nums_str[i])
        result.write(f'{str_res}\n')
    data.close()
    result.close()
    return result

file = 'for_task4/data.txt' # исходный файл
crypto = rle_coding(file) # сжатый методом RLE кодирования
decypto = rle_decoding(crypto.name) # развернутый файл, который должен равняться исходному файлу