# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random


N = int(input('введите натуральное число'))
newlist = []
for i in range(0,N):
    newlist.append(random.randint(-100,100))
print(newlist)
X = int(input('введите целое число'))
moreClose = 0
for j in range(0,N):
    if abs(newlist[j]-X) < abs(newlist[moreClose]-X):
        moreClose = j
print(f'самый близкий к значению {X} элемент массива - №{moreClose} (значение - {newlist[moreClose]}')


