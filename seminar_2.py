#Искусственный интеллек Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он
# использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные 
#холодильники.
#Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней 
#присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
#то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
#
#Формат входных данных
#В первой строке подается число n - количество холодильников. В последующих n строках вводятся строки, соде
#жащие латинские строчные буквы и цифры, в каждой строке от 5 до 100 символов.
#Формат выходных данных
#Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, 
#ничего выводить не нужно.

#n = int(input())
#list1 = []
#for i in range(n):
#    a = input()
#    if 'a' in a:
#        a = a[a.find('a'):]
#        if 'n' in a:
#            a = a[a.find('n'):]
#            if 't' in a:
#                a = a[a.find('t'):]
#                if 'o' in a:
#                    a = a[a.find('o'):]
#                    if 'n' in a:
#                        list1.append(i + 1)
#print(*list1)

#  Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов

#*Пример:*

#- Для N = 5: 1, -3, 9, -27, 81

number_N = int(input('введите число N - '))
for i in range(number_N):
    print((-3)**i, end = '')

#Напишите программу, в которой пользователь будет задавать две строки, а программа - 
# определять количество вхождений одной строки в другой

string_1 = input()
string_2 = input()
if string_1 > string_2:
    print(string_1.count(string_2))
else:
    print(string_2.count(string_1))