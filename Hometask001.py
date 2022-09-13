# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет
# является ли этот день выходным.
# Пример:
# - 6 - да
# - 7 - да
# - 1 - нет

# a = int(input('Enter the number of day: '))
# if a == 7 or a == 6:
#    print('Да')
# else:
#    print('Нет')

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(not (x or y or z) == (not x and not y and not z))


# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
# эта точка (или на какой оси она находится).

# Пример:

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

#a = int(input('Enter the coordinates of X: '))
#b = int(input('Enter the coordinates of Y: '))
#if a > 0 and b > 0:
#    print('It is 1 quarter')
#elif a < 0 and b > 0:
#    print('It is 2 quarter')
#elif a < 0 and b < 0:
#    print('It is 3 quarter')
#else:
#    print('It is 4 quarter')


# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

#number = (input('Enter the number of quarter: '))
#if number == 1:
#    print('Possible coordinates are x > 0 and y > 0')
#elif number == 2:
#    print('Possible coordinates are x < 0 and y > 0')
#elif number == 3:
#    print('Possible coordinates are x < 0 and y < 0')
#else:
#    print('Possible coordinates are x > 0 and y < 0')


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
#  между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

a = [int(i) for i in input('Enter the coordinates the first dot A: ').split(',')]
b = [int(i) for i in input('Enter the coordinates the second dot B: ').split(',')]

len_line = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(0.5)