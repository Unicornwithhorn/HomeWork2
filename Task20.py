# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка;
# B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12
newDictionary = {}
# здесь забиты все значения в словарь
newDictionary['A']=1
newDictionary['E']=1
newDictionary['I']=1
newDictionary['O']=1
newDictionary['U']=1
newDictionary['L']=1
newDictionary['N']=1
newDictionary['S']=1
newDictionary['T']=1
newDictionary['R']=1

newDictionary['D']=2
newDictionary['G']=2

newDictionary['B']=3
newDictionary['C']=3
newDictionary['M']=3
newDictionary['P']=3

newDictionary['F']=4
newDictionary['H']=4
newDictionary['V']=4
newDictionary['W']=4
newDictionary['Y']=4

newDictionary['K']=5

newDictionary['J']=8
newDictionary['X']=8

newDictionary['Q']=10
newDictionary['Z']=10

newDictionary['А']=1
newDictionary['В']=1
newDictionary['Е']=1
newDictionary['И']=1
newDictionary['Н']=1
newDictionary['О']=1
newDictionary['Р']=1
newDictionary['Т']=1

newDictionary['Д']=2
newDictionary['К']=2
newDictionary['Л']=2
newDictionary['М']=2
newDictionary['П']=2
newDictionary['У']=2

newDictionary['Б']=3
newDictionary['Г']=3
newDictionary['Ё']=3
newDictionary['Ь']=3
newDictionary['Я']=3

newDictionary['Й']=4
newDictionary['Ы']=4

newDictionary['Ж']=5
newDictionary['З']=5
newDictionary['Х']=5
newDictionary['Ц']=5
newDictionary['Ч']=5

newDictionary['Ш']=8
newDictionary['Э']=8
newDictionary['Ю']=8

newDictionary['Ф']=10
newDictionary['Щ']=10
newDictionary['Ъ']=10
wordInGame = input('Введите слово ').upper()
counter = 0
for i in wordInGame:
    counter +=newDictionary[i]
print('сумма очков за слово - {}'.format(counter))
