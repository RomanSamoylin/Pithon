# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части

import random

def FindMax (inp_list):
    max=inp_list[0]
    for i in range (len(inp_list)):
        if inp_list[i]>max:
            max=inp_list[i]
    return max

def FindMin (inp_list):
    min=inp_list[0]
    for i in range(len(inp_list)):
        if inp_list[i]<min:
            min=inp_list[i]
    return min

size = int(input('Введите число: '))
numeros = []
nums=[]
result=0

print('Ваша последовательность: ')
for i in range (size):
    numeros.append(random.randint(0,11)+round(random.random(),2))
    print(numeros[i], end=' ')
    num=round(numeros[i] - int(numeros[i]),2)
    nums.append(num)

min_el=FindMin(nums)
max_el=FindMax(nums)
result=round(min_el+max_el,2)
print ('Сумма максимальной и минимальной дробной части: ', result)