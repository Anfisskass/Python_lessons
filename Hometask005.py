# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# f1 = open("words.txt", "r")
# expres = ['Сижу за решеткой в абв темнице сырой. Вскормленный абв в неволе орел абвер молодой']
# f1.close

# with open("words.txt", "r") as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if "абв" in word:
#                 words.remove(word)

#         sentence = " ".join(words)
#         print(sentence)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# from random import randint

# a = int(input('Введите количество конфет'))
# hod = 0
# wins = {0: 'Игрок', 1: 'Бот'}
# while a > 0:
#     if a <= 28:
#         print(f'Выиграл {wins[hod]}')
#         break
#     if hod % 2 == 0:
#         print('Ход Игрока')
#         d = int(input('Введите количество конфет, которое хотите взять'))
#         a -= d
#         print(f'Осталось конфет: {a}')
#     else:
#         print('Ход Бота')
#         d = a % 29
#         a -= d
#         print(f'Осталось конфет: {a} ')
#     hod = (hod + 1) % 2


# 3. Создайте программу для игры в ""Крестики-нолики"".

# doska = list(range(1, 10))

# def draw_board(board):
#     for i in range(3):
#         print("|", doska[0 + i * 3], "|", doska[1 + i * 3], "|", doska[2 + i * 3], "|")

# def stavim_hod(hod):
#  valid = False
#  while not valid:
#     otvet = input("Введите номер клетки куда поставить значения " + hod+"? ")
#     otv = int(otvet)
#     if otv >= 1 and otv <= 9:
#         if (str(doska[otv-1] not in "XO")):
#             doska[otv-1] = hod
#             valid = True
#         else:
#             print("Эта клетка занята")
    

# def kto_viigral(doska):
#     pobeda = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for x in pobeda:
#         if doska[x[0]] == doska[x[1]] == doska[x[2]]:
#             return doska[x[0]]
#     return False

# def igra(doska):
#     count = 0
#     win = False
#     while not win:
#         draw_board(doska)
#         if count % 2 == 0:
#             stavim_hod("X")
#         else:
#             stavim_hod("O")
#         count += 1
#         if count > 4:
#             m = kto_viigral(doska)
#             if m:
#                 print(m, "Победил!")
#                 win = True
#                 break
# draw_board(doska)

# igra(doska)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def write_file(line: str, name:str):
    with open(name, 'w', encoding = "utf-8") as f:
        f.write(line)

def read_file(name: str):
    with open(name, 'r') as f:
         for line in f:
            words = line.spit()

def get_encode(s):
    encoding = ''
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + s[i]
        i += 1
    return encoding

def get_decode(s):
    decoding = ''
    i = 0
    while i < len(s):
        num = ''
        while i + 1 < len(s) and s[i].isdigit() == True:
            num += s[i]
            i += 1
        decoding += int(num) * s[i]
        num = ''
        i += 1
    return decoding


fail_name = 'file_task01.txt'
string_input = read_file(fail_name)
fail_name_encode = 'file_task02.txt'
string_input_encode = get_encode(string_input)
write_file(string_input_encode, fail_name_encode)
string_output = read_file(fail_name_encode)
string_output_decode = get_decode(string_output)
print(string_output_decode)