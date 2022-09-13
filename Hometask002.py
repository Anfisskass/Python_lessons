#1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#6782 -> 23
#0,56 -> 11

n = float(input('Введите число - '))
while n % 1 > 0:
    n *= 10
summ = 0
while n > 0:
    summ += n % 10
    n //= 10
print(int(summ))

#s = '0.56'
# summ = 0
# for i in s:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

#2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input())
res = [1]
for i in range(2, n + 1):
    res.append(res[-1] * i)
print(res)

#3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Input a number: '))
sum = 0
for n in range(1, n+1):
    sum = sum + round((1 + 1 / n)**n, 2)
print(sum)

#Второй способ решения
n = int(input('Введите число: ')) 
def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print('Сумма последовательности =', round(sum(sequence(n)), 2))

#Третий способ решения
n = int(input("Введите число : "))
sum = 0
for i in range (1, n + 1):
    a = (1 + 1 / i)**i 
    sum += a
    print(a, end=" ")
print(f"Сумма равна:  {sum}")

#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
n = int(input('Введите число N - '))
numbers = []
for i in range(n):
    numbers.append(randint(-n, n))
print(numbers)


f = open('file.txt', 'w') # создаем файл
while True:
    s = input('Укажите позицию для вычисления - ')
    if s == "":
        break
    f.write(s+"\n")
f.close()

result = 1
f = open('file.txt', 'r') #если файл загружен, то открываем имеющийся
for line in f:
    if line == "":
        break
    result *= numbers[int(line)]
f.close()
print(result)

#5. Реализуйте алгоритм перемешивания списка.

from random import shuffle
some_list = ['a', 'b', 'c', 'd', 'f']
shuffle(some_list)
print(some_list)

# второй метод

import random
list = ["Anna", "Alex", 3.14159, 0]
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    temp = list[i] #list[i], list[index_a] = list[index_a], list[i] можно таким образом вместо 100-102
    list[i] = list[index_a] 
    list[index_a] = temp
print(list)
