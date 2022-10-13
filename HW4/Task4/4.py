# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

import random


def GeneratePoly (pow):
    x=''
    first=pow
    while pow>0:
        k= random.randint(0,101)
        if pow==1:
            x=x+f'+{k}x'
        elif pow==first:
            x=x+f'{k}x^{pow}'
        else:
            if k!=0:    
                x=x+f'+{k}x^{pow}'
            else:
                x=x+'+'
        pow-=1
    x=x + '+' + str(random.randint(0,101))
    return x    
    

power = int(input('Введите степень многочлена: '))

path='Pol.txt'
with open(path, 'w') as f:
    f.write(GeneratePoly(power)+'=0')