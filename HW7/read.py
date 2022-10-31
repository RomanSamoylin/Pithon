# модуль чтения отображения
# 1. Отобразить весь справочник\n"
# "2. Найти абонента по фамилии\n"
# "3. Найти абонента по номеру телефона\n"
# "4. Добавить абонента в справочник\n"
# "5. Сохранить справочник в текстовом формате\n"
# "6. Закончить работу")

def Help():
    print('showAll - Отобразить весь справочник')
    print('findByName - Найти абонента по фамилии')
    print('findByTel - Найти абонента по номеру телефона')
    print('addContact - Добавить абонента в справочник')
    print('save - сохранить справочник в текстовом формате')
    print('import - импортировать контакты из файла')
    print('quit - Закончить работу')


def Show(inp_list):
    for i in inp_list:
        res = ''
        res = f'{i["name"]} - '
        res = res + f'{i["surname"]} - '
        res = res + f'{i["tel"]}'
        print(res)


def Peek(inp_list, query):
    i = inp_list[query]
    res = ''
    res = f'{i["name"]} - '
    res = res + f'{i["surname"]} - '
    res = res + f'{i["tel"]}'
    print(res)
