# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


import random
from random import randint

newList = []
N = int(input('Введите число элементов массива'))
for _ in range(0,N):
    newList.append(random.randint(0,10))

print(newList)

X = int(input('Введите число от 1 до 10'))
counter = 0
for _ in range(0,N):
    if newList[_] == X:
        counter+=1

print(f'число {X} встречается в массиве {counter} раз')