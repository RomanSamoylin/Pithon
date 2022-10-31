# модуль записи, поиска

def add_one(inp_list):
    item = {"name": '', "surname": '', "tel": 0}
    item["name"] = input('Введите имя контакта: ')
    item["surname"] = input('Введите фамилию контакта: ')
    item["tel"] = input('Введите номер телефона контакта: ')
    inp_list.append(item)


def find_name(inp_list, inp_string) -> int:
    res = -1
    for i in range(len(inp_list)):
        if inp_string == inp_list[i]["name"]:
            res = i
            break
    return res


def find_tel(inp_list, inp_tel) -> int:
    res = -1
    for i in range(len(inp_list)):
        if inp_tel == inp_list[i]["tel"]:
            res = i
            break
    return res