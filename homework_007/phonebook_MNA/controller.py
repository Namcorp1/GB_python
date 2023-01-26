import database
import export

def phonebook():
    print('Показать данные перед внесением (да/нет)?')
    answer = input()
    if answer == 'да':
        database.import_data()
    print('Желаете внести новых абонентов в справочник (да/нет)?')
    if answer == 'да':
        print('Сколько записей желаете добавить в справочник?')
        count = int(input())
        database.write_data(count) #аргумент функций - кол-во новых записей в телефонный справочник
    print('В какой формат экспортировать данные, введите число (1 - сsv / 2 - txt / 3 - в оба формата)?')
    answer = input()
    if answer == '1':
        export.export_csv('export1.csv')
    elif answer == '2':
        export.export_txt('export.txt')
    elif answer == '3':
        export.export_csv('export1.csv')
        export.export_txt('export.txt')