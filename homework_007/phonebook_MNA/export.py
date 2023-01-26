import csv

def export_txt(file):
    data = open('data.txt', 'r')
    exp_file = open(file, 'w')
    n = 1
    exp_file.write('№ п/п| ФИО| номер телефона| дата рождения|\n')
    for line in data:
        user_data = line.split(', ')
        exp_file.write(f'{n} ')
        for i in range(0, len(user_data)):
            exp_file.write(f'| {user_data[i]}')
        n += 1
    exp_file.close()
    print('Данные экспортированы в txt файл!')

def export_csv(file):
    data = open('data.txt', 'r')
    exp_file = open(file, 'w', newline='')
    for line in data:
        user_data = line.split(', ')
        writer = csv.writer(exp_file, dialect = 'excel', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([user_data[0],user_data[1],user_data[2]])
    exp_file.close()
    print('Данные экспортированы в csv файл!')