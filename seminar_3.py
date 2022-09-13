# Создать текстовый файл, записать в него построчно данные,
# которые вводит пользователь. Окончанием ввода пусть служит пустая строка.

fname= input('файл')
f = open(fname, 'w')
while True:
    s=input()
    if s ==' ':
        break
    f.write(s + '\n')
f.close()


#В текстовом файле посчитать количество строк, 
# а также для каждой отдельной строки определить 
# количество в ней символов и слов.

count = 0
with open ('file.txt') as file:
    for line in file:
        count += 1
        symbols = 0
        words = 0
        for s in line:
            symbols += 1
            if s != ' ' and symbols == 0:
                words += 1
                symbols = 1
            elif s == ' ':
                symbols = 0
print(count)
print(len(line))
print(words)

f = open('textfile.txt','r')
countLines = 0
countwordsInLines = []
countCharsInLines = []
for line in f:
    countLines+=1
    if line != '\n':
        countwordsInLines.append(line.count(' ') + 1)
    else:
        countwordsInLines.append(0)
    countCharsInLines.append(line.count('') -2)
f.close()
print(countLines)
print(countwordsInLines)
print(countCharsInLines)

# f = open('article.txt','r')
# line = 0
# for i in f:
#     line += 1
#
#     flag = 0
#     word = 0
#     for j in i:
#         if j != ' ' and flag == 0:
#             word += 1
#             flag = 1
#         elif j == ' ':
#             flag = 0
#
#     print(len(i), 'симв.', word, 'сл.')
# print(line, 'стр.')
# f.close()


# Иван решил создать самый большой словарь в мире. 
# Для этого он придумал функцию biggest_dict(**kwargs), 
# которая принимает неограниченное количество параметров «ключ: 
# значение» и обновляет созданный им словарь my_dict, 
# состоящий всего из одного элемента «first_one» со значением 
# «we can do it». Воссоздайте эту функцию. 
# тесты
# k1=22, k2=31, k3=11, k4=91
# name='Елена', age=31, weight=61, eyes_color='grey'
def biggest_dict(**kwargs):
    my_dict.update(**kwargs)

biggest_dict(k1=22, k2=31, k3=11, k4=91)
biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey')
print(my_dict)


# Напишите функцию to_dict(lst), которая принимает 
# аргумент в виде списка и возвращает словарь, 
# в котором каждый элемент списка является и ключом и значением. 
# Предполагается, что элементы списка будут 
# соответствовать правилам задания ключей в словарях.
# Тесты
# print(to_dict([1, 2, 3, 4]))
# print(to_dict(['grey', (2, 17), 3.11, -4]))


def to_dict(lst):
    return {element: element for element in lst}

# Тесты
print(to_dict([1, 2, 3, 4]))
print(to_dict(['grey', (2, 17), 3.11, -4]))

# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке 
# строк некое число.



spisok = ['строка1', 'строка2', 'строка3', 'строка1']
find_str = 'строка1'
if spisok.count(find_str) < 2:
    print(f'Второго вхождения строки {find_str} нет в заданном списке')
else:
    spisok1 = spisok[spisok.index(find_str) + 1:] # отрезаем первой вхождение
    print(spisok1.index(find_str) + (len(spisok) - len(spisok1))) # ищем строку в оставшемся списке и прибавляем то количество элементов, которое отрезали




# Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.

# *Пример:*

#- список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
#- список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
#- список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
#- список: [], ищем: "123", ответ: -1

strings = ["1", "another string", "string 3", "hello world", "123"]
x = input('Введите число: ')
if x in strings:
    print('Есть')
else:
    print('Нет')


