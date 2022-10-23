# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = list(map(str, input('Введите строку: ').split()))
text = filter(lambda x: 'абв' not in x, text)

for i in text:
    print(i, end=' ')