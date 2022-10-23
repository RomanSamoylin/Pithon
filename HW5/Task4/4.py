# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = input('Введите строку: ')


def Squash(inp_text):
    result = []
    i=0
    while i in range(len(inp_text) - 1):
        counter = 1
        key = inp_text[i]
        for j in range(i + 1, len(inp_text)):
            if key == inp_text[j]:
                counter += 1
            else:
                i += counter
                if counter == 1:
                    result.append((key, 1))
                else:
                    result.append((key, counter))
                break
    result.append((inp_text[-1], 1))
    return result

def Unpack (inp_list):
    result=''
    for i in inp_list:
        result = result + i[0]*i[1]
    return result

a = Squash(text)
print(a)
print (Unpack(a))