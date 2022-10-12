# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д

import random

size = int(input('Введите число: '))
numeros = []
couple_product = []
for i in range (size):
    numeros.append(random.randint(0,11))
if size%2==0:    
    for i in range (size//2):
        couple_product.append(numeros[i]*numeros[size-1-i])
else:
    for i in range (size//2+1):
        couple_product.append(numeros[i]*numeros[size-1-i])
print(numeros, '\n', couple_product)