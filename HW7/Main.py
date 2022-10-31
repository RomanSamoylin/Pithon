import impex as i
import read as r
import RF as rf

booted = True
book = []

while booted:
    inp_cmd = input('Введите команду или help:\n')
    if inp_cmd == 'quit':
        booted = False
    elif inp_cmd == 'help':
        r.Help()
    elif inp_cmd == 'showAll':
        r.Show(book)
    elif inp_cmd == 'findByName':
        n = rf.find_name(book, input('Введите имя: '))
        if n == -1:
            print('Контакт не найден')
        else:
            r.Peek(book, n)
    elif inp_cmd == 'findByTel':
        n = rf.find_tel(book, int(input('Введите номер телефона: ')))
        if n == -1:
            print('Контакт не найден')
        else:
            r.Peek(book, n)
    elif inp_cmd == 'addContact':
        rf.add_one(book)
    elif inp_cmd == 'save':
        i.export_phonebook(book)
    elif inp_cmd == 'import':
        book = i.import_phonebook(book)
    else:
        print('Некорректный ввод. Попробуйте ещё раз.')
