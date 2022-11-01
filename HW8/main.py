# print('showAll - Отобразить весь справочник')
# print('findByName - Найти сотрудника по фамилии')
# print('findByJob - Найти сотрудника по номеру телефона')
# print('findByTel - Найти сотрудника по номеру телефона')
# print('addWorker - Добавить сотрудника в справочник')
# print('saveTXT - сохранить справочник в текстовом формате')
# print('importTXT - импортировать контакты из TXT-файла')
# print('saveCSV - сохранить справочник в формате CSV')
# print('importCSV - импортировать контакты из CSV-файла')
# print('saveJSON - сохранить справочник в формате JSON')
# print('importJSON - импортировать контакты из JSON-файла')

import dataflex as df
import impex as ie
import view as v

booted = True

db=[]

while booted:
    inp_cmd = input('Введите команду или help:\n')
    if inp_cmd == 'quit':
        booted = False
        print('Всего хорошего...')
    elif inp_cmd == 'show':
        v.Show(db)
    elif inp_cmd == 'help':
        v.Help()
    elif inp_cmd == 'addWorker':
        df.add_one(db)
    elif inp_cmd == 'findByName':
        n=df.find_name(db, input('Введите имя: '))
        if n == -1:
            print('Сотрудник не найден')
        else:
            v.Peek(db, n)
    elif inp_cmd == 'findByJob':
        n=df.find_assignment(db, input('Введите должность: '))
        if n == -1:
            print('Сотрудник не найден')
        else:
            v.Peek(db, n)
    elif inp_cmd == 'findByTel':
        n=df.find_tel(db, input('Введите номер телефона: '))
        if n == -1:
            print('Сотрудник не найден')
        else:
            v.Peek(db, n)
    elif inp_cmd == 'saveTXT':
        ie.export_txt(db)
    elif inp_cmd == 'importTXT':
        db = db + ie.import_txt()
    elif inp_cmd == 'saveJSON':
        ie.export_json(db)
    elif inp_cmd == 'importJSON':
        db = db + ie.import_json()
    elif inp_cmd == 'saveCSV':
        ie.export_csv(db)
    elif inp_cmd == 'importCSV':
        db = db + ie.export_csv(db)
    else:
        print('Команда не распознана. Попробуйте ещё раз... ')