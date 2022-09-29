 # Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

num=int(input('Введите число: '))
for i in range(-num, num+1):
    print(i, end=' ')

# print('введите числа')
# value = int(input())
# print (list (range(-value, value+1)))