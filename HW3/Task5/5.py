# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов

def Fib (n):
    if n==1 or n==2:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)

def NFib (n):
    if n == -1:
        return 1
    elif n==-2:
        return -1
    else:
        return NFib(n+2)-NFib(n+1)

def Reverse (inp_list):
    for i in range(len(inp_list)//2):
        inp_list[i], inp_list[len(inp_list)-1-i] = inp_list[len(inp_list)-1-i], inp_list[i]

number = int(input('Введите число: '))
pos_fib = []
neg_fib = []
for i in range (1, number+1):
    pos_fib.append(Fib(i))
    neg_fib.append(NFib(-i))
Reverse(neg_fib)
neg_fib.append(0)
print(number,'->',neg_fib+pos_fib)