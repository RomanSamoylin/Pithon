# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

inp_list = list(map(int, input('Введите числа через пробел: ').split()))
print(inp_list)
targets=[]
for i in range(len(inp_list)):
    if inp_list.count(inp_list[i])>1:
        targets.append(i)
for i in range(len(inp_list)):
    if i in targets:
        print('',end=' ')
    else:
        print(inp_list[i],end=' ')