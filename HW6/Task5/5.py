# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена

import random

def WritePoly (inp_list):
    res = ''
    for i in inp_list:
        if i[0] == 0:
            res = res+''
        else:
            if i[1]>1:
                if i[0] == 1:
                    res = res+f'+x^{i[1]}'
                elif i[0]<0:
                    res = res+f'-{abs(i[0])}x^{i[1]}'
                else:
                    res = res + f'+{i[0]}x^{i[1]}'
            elif i[1]==1:
                if i[0] == 1:
                    res = res+f'+x'
                elif i[0]<0:
                    res = res+f'-{abs(i[0])}x'
                else:
                    res = res + f'+{i[0]}x'
            else:
                if i[0]<0:
                    res = res+f'-{abs(i[0])}'
                else:
                    res = res + f'+{i[0]}'
    res = res+'=0'
    res.strip('+')
    return res
k = int(input('Задайте натуральную степень: '))

is_it_in = lambda x, b: x if b else 0
pow = [i for i in range(k+1)]
koefs = [is_it_in(random.randint(-9,10), bool(random.randint(0,2))) for i in range(k+1)]
poly = list(zip(koefs,pow))
poly.sort(key=lambda x: x[1], reverse=True)

print(WritePoly(poly))