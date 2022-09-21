#1. Вычислить число c заданной точностью d

#Пример:

#- при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

#import math

#d = input('Задайте число d: ')
#p = float(input ('Задайте число для вычисления: '))
#count1 = 0
#count2 = 0
#for i in str(d):
#    if i != ".":
#        count1 +=1
#    else:
#        break
#for i in str(d):
#    count2 += 1
#T = count2 - count1 - 1

#print(round(p, T)

#Второй способ

#import math
#d = input('Введите число d указывающее степень округления pi ')
#d = d[2:len(d)]
#print(round(math.pi, len(d)))

#2. Задайте натуральное число N. Напишите программу, которая составит 
#список простых множителей числа N.


#Первый способ
#N = int(input('Введите число: '))
#list1 = []
#for i in range(2, N + 1):
#    if N % i == 0:
#        count = 1
#        for j in range(2, (i // 2 + 1)):
#            if i % j == 0:
#                count = 0
#        if (count == 1):
#            list.append(i)
#print(list1)

#Второй способ

#n = int(input('Введите число N: '))
#i = 2
#list = []

#while i <= n:
#    if n % i == 0:
#        list.append(i)
#        n //= i
#        i = 2
#    else:
#        i += 1
#print(f"Простые ножители введенного числа указаны в списке: {list}")

#3. Задайте последовательность чисел. Напишите программу, которая выведет
#список неповторяющихся элементов исходной последовательности.

#numbers = [1, 2, 3, 4, 4, 4, 5]
#list = []
#for i in numbers:
#    if numbers.count(i) == 1:
#        list.append(i)
#print(list)
 
#Второй способ

#def elements(num):
#    nums = [int(i) for i in nums.split()]
#    return list(set(nums))

#numbers = '1 1 2 2 3 455 66 66 2 1'
#print(elements(numbers))



#4. Задана натуральная степень k. Сформировать случайным образом 
#список коэффициентов (значения от 0 до 100) многочлена и записать
#в файл многочлен степени k.

#Пример:

#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#import random
#from random import randint

#def create_polynomia(k):
#    coefs = []
#    for i in range (k + 1):
#        coefs.append(randint(0, 100))
#    return coefs

#def format_polynomia(coefs):
#    output = ""
#    for i in range(k, -1, -1):
#        c = coefs[i]
#        if c != 0:
#            if output != "": output += (" + " if c > 0 else " - ")
#            else:
#                if c < 0: output += "-"
#            if c != and c != -1:
#                output += str(abs(c))
#                if i > 0: output += "*"
#            if i > 0: output += ("x" if i == 1 else "x^" + str(i))
#    return output

#k = int(input("Задайте степень k: "))
#coefs = create_polynomia(k)
#output = format_polynomia(coefs)
#print(coefs)
#print(output + " = 0")

#with open ('polynomials.txt', 'w') as file:
#    file.write(output)

#Второй способ

#from random import randint

#k = int(input('Insert equation power: '))
#koefs = list()
#for i in range(1, k + 2):
#    koefs.append(randint(1, 100))

#ans = list()
#for i in range(len(koefs)):
#    if k == 1:
#        ans.append(f'{koefs[i]}*x')
#    elif k == 0:
#        ans.append(f'{koefs[i]}')
#    else:
#        ans.append(f'{koefs[i]}*x**{k}')
#    flag = randint(0, 1)
#    if flag == 1:
#        ans.append('+')
#    elif flag == 0:
#        ans.append('-')
#    k -= 1

#ans.pop(-1)
#ans.append('=0')
#fout = open('output.txt', 'w')
#fout.write(''.join(ans))
#fout.close


#5. Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов

import random
def nmnogochlen1(a = random.randint(1, 100), b = random.randint(0, 100), c = random.randint(0, 100), res = '') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res

def nmnogochlen2(a = random.randint(1, 100), b = random.randint(0, 100), c = random.randint(0, 100), res = '') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res
f = open('dz40.txt', 'w')
f.write(nmnogochlen1())
print(nmnogochlen1)
f.close()

f = open('dz41.txt', 'w')
f.write(nmnogochlen2())
print(nmnogochlen2)
f.close()

f = open('dz40.txt', 'r')
list_5 = str(f.readline()).split('x')
c1 = b1 = a1 = 0
if len(list_5) == 3:
    c1 = list_5[2][1:]
if len(list_5) >= 2:
    b1 = list_5[1][3:-1]
a1 = list_5[0][:-1]
f.close()

f = open('dz41.txt', 'r')
list_51 = str(f.readline()).split('x')
c2 = b2 = a2 = 0
if len(list_51) == 3:
    c2 = list_51[2][1:]
if len(list_51) >= 2:
    b2 = list_51[1][3:-1]
a2 = list_51[0][:-1]
f.close()

f = open('dz42.txt', 'w')
f.write(nmnogochlen1(int(a1) + int(a2) + int(b1) + int(b2) + int(c1) + int(c2)))
print(nmnogochlen1(int(a1) + int(a2) + int(b1) + int(b2) + int(c1) + int(c2)))
f.close
