# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def day_1(day):
    if day >= 1 and day <= 5:
        return('Нет!')
    elif day >= 6 and day <= 7:
        return('Да!')
    else: 
        return('Число не обозначает день недели!')
                    
print(day_1(int(input("Введите чило: "))))


# _______________________________________________________________________________________________________________________________________________
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой 
# находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите чило X: "))
y = int(input("Введите чило Y: "))

def coordinate_plane(x,y):
    if x == 0 or y == 0:
        return("X или Y == 0!") 
    if x >= 1 and y >= 1:
        return('Четверть 1')
    elif x <= -1 and y >= 1:
        return('Четверть 2')
    elif x <= -1 and y <= -1:
        return('Четверть 3')
    elif x >= 1 and y <= -1:
        return('Четверть 4')
    
print(coordinate_plane(x,y))

# _______________________________________________________________________________________________________________________________________________
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

coordinate_plane = int(input("Введите номер четверти: "))

if coordinate_plane == 1:
    print("Дипазон x >= 1; y >= 1 ")
elif coordinate_plane == 2:
        print("Дипазон x <= -1; y >= 1 ")
elif coordinate_plane == 3:
        print("Дипазон x <= -1; y <= -1 ")          
elif coordinate_plane == 4:
        print("Дипазон x >= 1; y <= -1 ")
else:
    print('Число не является номером четверти!')

# _______________________________________________________________________________________________________________________________________________
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Введите координаты точки А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Введите координаты точки B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

from math import sqrt
print('Distance between A and B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))

