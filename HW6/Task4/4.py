# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве

a = tuple(map(int, input('Введите координаты точки А через пробел: ').split()))
b = tuple(map(int, input('Введите координаты точки B через пробел: ').split()))

dist = lambda x1,x2,y1,y2: round(((x2-x1)**2 + (y2-y1)**2)**0.5,3)

print (a, b, dist(a[0],b[0], a[1],b[1]), sep='\n')