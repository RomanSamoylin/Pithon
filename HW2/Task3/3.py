# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('Введите число: '))
frac_list = []
sum=0
sums=[]
for i in range(1,n+1):
    frac_list.append(round((1+1/i)**i))
    sum+=frac_list[i-1]
    sums.append(sum)
for i in range(len(sums)):
    print(f'{i+1}: {sums[i]},', end=' ')