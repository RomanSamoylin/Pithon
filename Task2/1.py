# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

fiver = list(map(int, input('Введите 5 чисел через пробел: ').split()))
max_num=fiver[0]
for i in range(len(fiver)):
    if fiver[i]>max_num:
        max_num=fiver[i]
print(max_num)

# print(max(1, 4, 998, 7, 5))