# модуль импорта и экспорта

def import_phonebook(inp_list) -> list:
    with open('phonebook.txt', 'r') as file:
        item = {"name": '', "surname": '', "tel": ''}
        for i in file:
            tmp = list(map(str, i.split('-')))
            item["name"] = tmp[0]
            item["surname"] = tmp[1]
            item["tel"] = tmp[2]
            inp_list.insert(0, item)
    return inp_list


def export_phonebook(inp_list):
    with open('phonebook.txt', 'w+') as file:
        for i in range(len(inp_list)):
            file.write(f'{inp_list[i]["name"]} - {inp_list[i]["surname"]} - {inp_list[i]["tel"]}\n')