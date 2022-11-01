# импрота и экспорта модуль

import json
import csv
def import_txt() -> list:
    with open('database.txt', 'r+') as file:
        items = []
        for i in file:
            item = {"name": '', "surname": '', "tel": '', "assignment": '', "wage": ''}
            i=i.strip('\n')
            item["name"] = tmp[0]
            item["surname"] = tmp[1]
            item["tel"] = tmp[2]
            item["assignment"] = tmp[3]
            item["wage"] = tmp[4]
            tmp = list(map(str, i.split('-')))
            items.append(item)
    return items

def export_txt(inp_list):
    with open('database.txt', 'w+') as file:
        for i in range(len(inp_list)):
            file.write(f'{inp_list[i]["name"]} - {inp_list[i]["surname"]} - {inp_list[i]["tel"]} - {inp_list[i]["assignment"]} - {inp_list[i]["wage"]}\n')
def export_json (database):
    with open('db.json', 'w', encoding='utf-16') as f:
        for i in database:
            f.write(json.dumps(i) + '\n')

def import_json() -> list:
    items =[]
    with open('db.json','r', encoding='utf=16') as f:
        for i in f:
            items.append(json.loads(i))
    return items

def export_csv (database):
    with open('database.csv', 'w') as cf:
        for i in database:
            row = []
            row.append(i["name"])
            row.append(i["surname"])
            row.append(i["tel"])
            row.append(i["assignment"])
            row.append(i["wage"])
            add_row = csv.writer(cf)
            add_row.writerow(row)

def import_csv() -> list:
    with open('database.csv', 'r') as cf:
        reader = csv.reader(cf)
        res=[]
        for i in reader:
            tmp = list(map(str,i[0].split('-')))
            item = {"name": '', "surname": '', "tel": '', "assignment": '', "wage": ''}
            item["name"] = tmp[0]
            item["surname"] = tmp[1]
            item["tel"] = tmp[2]
            item["assignment"] = tmp[3]
            item["wage"] = tmp[4]
            res.append(item)
        return res