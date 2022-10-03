# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
#  стоящих на нечётной позиции.
# Пример:
# o [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# x = [2, 3, 5, 9, 3]


def num_odd(a):
    num = 0
    for i in a[1::2]:
        num += i
    return num


print(num_odd(x))


# ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#  Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# o [2, 3, 4, 5, 6] => [12, 15, 16];
# o [2, 3, 5, 6] => [12, 15]

from sys import flags
import os
import random
os.system('cls')

l1 = []


def fill_list(list):
    rand = random.randint(1, 10)
    for i in range(rand):
        list.append(random.randint(0, 10))
    return list


def find_pairs_product(list):
    l2 = []
    i = 0
    j = -1
    while i < len(list)/2:
        l2.append(list[i]*list[j])
        i += 1
        j -= 1
    return l2

print(fill_list(l1))
print(find_pairs_product(l1))

# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19


os.system('cls')

l1 = []


def fill_list(list):
    rand = random.randint(1, 5)
    for i in range(rand):
        list.append(float(input("Enter Number: ")))
    return list


def find_fraction_difference(list):
    for i in range(len(list)):
        list[i] = list[i] % 1
    maximum = list[0]
    minimum = list[0]
    diff = 0
    for i in range(len(list)):
        if list[i] == 0.0:
            continue
        if minimum == 0.0:
            minimum = list[i]
        if list[i] > maximum:
            maximum = list[i]
        if list[i] < minimum:
            minimum = list[i]
    print(maximum, minimum)
    diff = maximum - minimum
    return round(diff, 3)


print(fill_list(l1))
print(find_fraction_difference(l1))


#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10

import os
os.system('cls')

n = int(input())

def convert_to_binary(number):
    b_num = ''
    while number > 0:
        b_num = str(number%2) + b_num
        number = number // 2
    return int(b_num)
print(convert_to_binary(n))


