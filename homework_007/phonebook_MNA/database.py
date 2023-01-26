# модуль для логики базы данных

def import_data():
    data = open('data.txt', 'r')
    for line in data:
        print(line)
    data.close()

def write_data(count):
    print('Введите данные новых контактов (ФИО, номер телефона, дата рождения) через запятую в формате:')
    print('Иванов Иван Иванович, 33907, 01.02.1993')
    data = open('data.txt', 'a')
    for i in range(0,count):
        input_data = input('Введите данные: ')
        new_data = input_data.split(', ')
        data.write(f'{new_data[0]}, {new_data[1]}, {new_data[2]}\n')
    data.close()
    print('Данные внесены!')

