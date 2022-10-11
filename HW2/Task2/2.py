# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def Factorial (number):
    if (number == 1):
        return 1
    else:
        return number*Factorial(number-1)

n=int(input('Введите число: '))
fact_list = []
for i in range (1,n+1):
    fact_list.append(Factorial(i))
print(fact_list)