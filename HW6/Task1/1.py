# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.

chisla = list(map(str, input('Введите вещественное числа через пробел: ').split()))
sep_floats= lambda x: list(map(str, x.split('.')))
numbers = [sep_floats(i) for i in chisla]
for i in numbers:
    i[1] = 10**(-len(i[1]))*int(i[1])
numbers.sort(key=lambda x: x[1], reverse=True)
print(numbers[0][1]-numbers[-1][1])