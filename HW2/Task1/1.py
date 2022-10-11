# Напишите программу, которая принимает вещественное число и считает сумму его цифр

def DigitSum (chislo_list):
    sum = 0
    for i in range(len(chislo_list)):
        while chislo_list[i]>0:
            sum+=chislo_list[i]%10
            chislo_list[i]=chislo_list[i]//10
    return sum

def DigitSumInt (chislo):
    sum = 0
    while chislo>0:
        sum+=chislo%10
        chislo=chislo//10
    return sum

user_inp = input('Введите вещественное: ')
if ('.' or ',' in user_inp):
    user_inp=user_inp.replace(',','.')
    chislo = list(map(int, user_inp.split('.')))
    print(DigitSum(chislo))
else:
    print(DigitSum(DigitSumInt(int(user_inp))))