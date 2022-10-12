# Напишите программу, которая будет преобразовывать десятичное число в двоичное

number = int(input('Введите число: '))
ones_and_zeros=[]
while number>0:
    ones_and_zeros.append(number%2)
    number//=2
for i in range(len(ones_and_zeros)):
    print(ones_and_zeros[len(ones_and_zeros)-1-i], end='')