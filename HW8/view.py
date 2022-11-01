# интерфейс
def Help():
    print('show - Отобразить весь справочник')
    print('findByName - Найти сотрудника по имени')
    print('findByJob - Найти сотрудника по номеру телефона')
    print('findByTel - Найти сотрудника по номеру телефона')
    print('addWorker - Добавить сотрудника в справочник')
    print('saveTXT - сохранить справочник в текстовом формате')
    print('importTXT - импортировать контакты из TXT-файла')
    print('saveCSV - сохранить справочник в формате CSV')
    print('importCSV - импортировать контакты из CSV-файла')
    print('saveJSON - сохранить справочник в формате JSON')
    print('importJSON - импортировать контакты из JSON-файла')
    print('quit - Закончить работу')


def Show(inp_list):
    for i in inp_list:
        res = ''
        res = f'{i["name"]} - '
        res = res + f'{i["surname"]} - '
        res = res + f'{i["tel"]} - '
        res = res + f'{i["assignment"]} - '
        res = res + f'{i["wage"]}'
        print(res)


def Peek(inp_list, query):
    i = inp_list[query]
    res = ''
    res = f'{i["name"]} - '
    res = res + f'{i["surname"]} - '
    res = res + f'{i["tel"]} - '
    res = res + f'{i["assignment"]} - '
    res = res + f'{i["wage"]}'
    print(res)