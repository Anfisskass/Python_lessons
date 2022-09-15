# Задача 1. 
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму 
# элементов списка, стоящих на нечётной позиции.

#Пример:

#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list = [2, 3, 5, 9, 3]
sum = 0
j = 1
for i in range(0,len(list) - 1):
    if j % 2 != 0:
        sum = sum + list[j]
        j += 1
    else:
        j +=1   
print(sum)


#Второй способ
my_list = [2, 3, 5, 9, 3]
print(sum(my_list[1::2]))



# Задача 2.
#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
n = len(list1)
list2 = []
k = int(len(list1)/2+len(list1)%2)
len(list2)==k
for i in range(k):
    list2.append((list1[i]*list1[n-1-i]))
print(list2)


#Второй способ
my_list = [2, 3, 4, 5, 6]
result_list = []
for i in range((len(my_list)+1)//2):
    result_list.append(my_list[i] * my_list[len(my_list)-1-i])
print(result_list)


#Третий способ
import random

b = int(input('Введите кол-во чисел в списке for 2# = '))
list_b = list((i-i+1)*randint(0, 10) for i in range(b))
print(list_b)
proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
print(proiz_b)


# Задача 3.
#Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

#Пример:

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

list1 = [1.1, 1.2, 3.1, 5, 10.01]
list2 = []
for i in range(len(list1)):
    a = round(list1[i]*10 % 10, 2)
    if a > 0:
        list2.append(a)
b = round(float((max(list2)-min(list2))*10/100), 2)
print(b)
  
#Второй способ
# 
# from unittest import result
my_list = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in my_list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print('%.2f' % (max-min))  


# Задача 4.
#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

#Пример:

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10


a=int(input('Введите число: '))
b=bin(a)
print(b[2:])

#Второй способ

s = ""
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)


# Задача 5.
#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#Пример:

#- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

a = int(input('Enter the number: '))
print(a)
negofibonacci = [1,-1]
fibonacci = [1,1]

for i in range(2,a):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_nego = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list_nego)

negofibonacci.reverse()
negofibonacci.append(0)

print(f' for a = {a} =>{negofibonacci+fibonacci}')

#Второй способ

n = int(input('Введите число: '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1)+fib(n-2)


set1 = [0]
set2 = []
for i in range(1, 10):
    set1.append(fib(i))
    set2.append(fib(i)*-1)
for i in range(len(set2)):
    if i%2==0:
        set2[i]= -set2[i]
set3 = set2[::-1]
print(set3+set1)

#Второй способ
def lst_fibonacci_num():
    num = int(input('Введите любое натуральное число: '))
    fib = []
    a, b = 1, 1
    for i in range(num):
        fib.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for j in range(num + 1):
        fib.insert(0, a)
        a, b = b, a - b
    print(f'Список чисел Фибоначчи для {num}: {fib}')


lst_fibonacci_num()