# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

size = int(input('Введите число: '))
numeros = []
sum=0
for i in range (size):
    numeros.append(random.randint(0,11))
    if i%2 == 1:
        sum+=numeros[i]
print(numeros, '\n', sum)