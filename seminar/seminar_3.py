# СПИСКИ И СЛОВАРИ
#--------------------------------------------------------
print("TASK 1")
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

list = [1, 1, 2, 0, -1, 3, 4, 4]
list_1 = []

for i in list:
    if i not in list_1:
        list_1.append(i)
res = len(list_1)
print(res)

#--------------------------------------------------------
print("TASK 2")
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

lst = [1, 2, 3, 4, 5]
# print(lst.pop(2))
# print(lst.remove(4))

k = 2
for i in range(k):
    num = lst.pop()
    lst.insert(0, num)
print(lst)

#--------------------------------------------------------
print("TASK 3")
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

x = {"123": 123, (1,1,3): "123", (1,2,3): [1,2,3]}
print(x)

for i in x:
    print(i)
    print(x[i])

for i,j in x.items():
    print(i,j)

for i in x.values():
    print(i)


liist = [1,2,3,4,5]
print(liist.count(3))       #считает сколько встречается цифр 3 в списке
print(max(liist))


#--------------------------------------------------------
print("TASK 4")
# Требуется найти в массиве list_1 самый близкий по значению элемент 
# к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. 
# Если значение k совпадает с этим элементом - выведите его.
# Пример:
list_1 = [1, 2, 3, 4, 5, 6]
k = 6
# # 5

result = []

min = max(list_1)

for i in list_1:
    diff = abs(i - k)
    if min > diff:
        min == diff
        result = [i]
    elif min == diff:
        result.append(i)
for i in result:
    print(f'-> {i}')


#--------------------------------------------------------
print("TASK 5")
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:
k = 'ноутбук'
# # 12

alphabet = { "а": 1, "в": 1, "е": 1, "и": 1, "н": 1, "о": 1, "р": 1, "с": 1, "т": 1, "д": 2, "к": 2, "л": 2, "м": 2, "п": 2, "у": 2, "б": 3, "г": 3, "ё": 3, "ь": 3, "я": 3, "й": 4, "ы": 4, "ж": 5, "з": 5, "х": 5, "ц": 5, "ч": 5, "ш": 8, "э": 8, "ю": 8, "ф": 10, "щ": 10, "ъ": 10, "a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "s": 1, "t": 1, "r": 1, "d": 2, "g": 2, "b": 3, "c": 3, "m": 3, "p": 3, "f": 4, "h": 4, "v": 4, "w": 4, "y": 4, "k": 5, "j": 8, "x": 8, "q": 10, "z": 10}

result = 0
for i in range(len(k)):
    for (key, value) in alphabet.items():
        if k[i] == key:
            result = result + value
print(result)
    