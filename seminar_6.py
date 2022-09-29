#1.Вводится список целых чисел в одну строчку через пробел. 
#Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter. 
# Результат отобразить на экране в виде последовательности оставшихся чисел в одну строчку через пробел.
#пример - 8 11 0 -23 140 1 => 11 -23

#lst = [1, 20, 3, 40, 5, 60, 7]
#print(list(filter(lambda x: 9<abs(x)<100, lst))) #len abs(x,2)

# 2.Дан список, вывести отдельно буквы и цифры.
# a = ( "a", 'b', '2', '3' ,'c')
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3') 

# lst = ["a", 'b', '2', '3' ,'c']
# word = list(filter(lambda x: x.isdigit(), lst))
# number = list(filter(lambda x: x.isalpha(), lst))
# print(word, list)

# 3. Преобразовать набора списков
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]

# a, b, c = map(list, zip (users, ids, salary))
# print(a, b, c, sep = '\n')
# a, b, c = map(list, zip(a, b, c))
# print(a, b, c, sep = '\n')



# 4.Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

#     *Пример:* 

#     1+2*3 => 7; 

#     (1+2)*3 => 9;

def parse(s: str) -> list:
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        elif symbol in ['(', ')']:
            if digit:
                result.append(float(digit))
                digit = ""
            result.append(symbol)
        else:
            if digit:
                result.append(float(digit))
                digit = ""
                result.append(symbol)
    else:
        if digit:
            result.append(float(digit))
    return result

def calculate(lst: list) -> float:
    result = 0.0
    while '*' in lst:
        index = lst.index('*')
        result = lst[index - 1] * lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '/' in lst:
        index = lst.index('/')
        result = lst[index - 1] / lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '+' in lst:
        index = lst.index('+')
        result = lst[index - 1] + lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    while '-' in lst:
        index = lst.index('-')
        result = lst[index - 1] - lst[index + 1]
        lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result


def brackets(lst:list) -> list:
    while '(' in lst:
        opening = lst.index('(')
        closing = lst.index(')')
        lst = lst[:opening] + [calculate(lst[opening + 1:closing])] + lst[closing + 1:]
    return lst

s = "(1+1) + 20"
result = parse(s)
print(result)
result = brackets(result)
print(result)
print(calculate(result))


