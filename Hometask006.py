# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# list = [1, 2, 3, 5, 1, 5, 3, 10]
# print(list(filter(lambda s: lst.count(s) == 1, list)))

# Напишите программу, которая принимает на
# вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0, 56 -> 11

# def sum_num(num: str) -> int:
#     return sum(map(int, filter(lambda i: i.isdigit(), str(num))))


# print(sum_num(6782))
# print(sum_num(0.56))

#Второй способ 

# print(sum(map (int, [item for item in input('Введите вещественное число ') if item != '.'])))

# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

# # import math

# # def fact(n: int) -> list:
# #     li = [i for i in range(1, n+1)]
# #     fact = list(map(lambda x: math.factorial(x), li))
# #     return fact

# # print(fact(4))

# # Второй способ

# def fun(x):
#     return 1 if x == 1 else x * fun(x - 1)
# print(list(fun(i) for i in range(1, int(input('Введите натуральное число ')) + 1)))

# # Задайте список из n чисел последовательности
# # $(1 +\frac 1 n) ^ n$ и выведите на экран их сумму.


# def seq(n: int) -> float:
#     li = [i for i in range(1, n + 1)]
#     sum_sq = sum((map(lambda x: (1 + 1/x)**x , li)))
#     return sum_sq

# print(round(seq(6),2))

# # Задайте список из нескольких чисел. Напишите программу,
# # которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# # Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_odd_index(lst: list) -> int:
#     l = enumerate(lst)
#     l1 = filter(lambda e: e[0] % 2 == 1, l)
#     l2 = list(zip(*l1))
#     l3 = list(l2[1])
#     return sum(l3)
# print(sum_odd_index([2, 3, 5, 9, 3]))


# #Напишите программу, которая найдёт произведение пар чисел списка. 
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# #Пример:

# #- [2, 3, 4, 5, 6] => [12, 15, 16];
# #- [2, 3, 5, 6] => [12, 15]

# from math import ceil
# input = [2, 3, 4, 5, 6]
# print(list(input[i] * input[-i - 1] for i in range(ceil(len(input)/2))))