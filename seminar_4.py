#lang = {'а': 'a',
#         'б': 'b',
#         'в': 'v',
#         'г': 'g',
#         'д': 'd',
#         'е': 'e',
#         'ё': 'e',
#         'ж': 'zh',
#         'з': 'z',
#         'и': 'i',
#         'й': 'y',
#         'к': 'k',
#         'л': 'l',
#         'м': 'm',
#         'н': 'n',
#         'о': 'o',
#         'п': 'p',
#         'р': 'r',
#         'с': 's',
#         'т': 't',
#         'у': 'u',
#         'ф': 'f',
#         'х': 'kh',
#         'ц': 'ts',
#         'ч': 'ch',
#         'ш': 'sh',
#         'щ': 'shch',
#         'ъ': '',
#         'ы': 'y',
#         'ь': '',
#         'э': 'e',
#         'ю': 'yu',
#         'я': 'ya',
#         ' ': ' '
#}

#value = 'Мама мыла раму'
#result = ''

#for i in value:
#    result += lang[i.lower()]

#print(result)


#t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

#start_index = ord('а')
#title = 'Переводим этот текст, сейчас!'
#print(title.lower())

#slug = ""
#for s in title.lower():

#	if "а" <= s <= "я":
#		slug += t[ord(s) - ord('а')]
	# elif s == "ё":
	# 	slug = 'yo'
	# elif s in " !?;:.,":
	# 	slug = "-"
#	else:
#		slug += s

# while slug.count('--'):
# 	slug = slug.replace('--', '-')

#print(slug)

#1. Задайте строку из набора чисел. Напишите программу, 
#которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

#n= '3 5 1 7 9 2 5'
# min=int(n[0])
# max=int(n[0])
# for i in n.split(sep= ' '):
#     if int(i)<min:       
#         min=int(i)
#     if int(i)>max:
#         max=int(i)
# print (min,max)


str = '12 32 0 15'
lst = [int(i) for i in str.split()]
print(min(lst))
print(max(lst))

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
# 1) с помощью математических формул нахождения корней квадратного уравнения
    
# 2) с помощью дополнительных библиотек Python

def discriminant(a: float, b: float, c: float) -> float:
    return b * 2 - 4  a * c


def solve_quadratic(a: float, b: float, c: float) -> str:
    if a == 0:
        raise ValueError("Not quadratic equation")

    d = discriminant(a, b, c)
    if d < 0:
        return "No roots"
    elif d == 0:
        return f"One root x = {-b / (2 * a)}"
    else:
        x1 = (-b + d * 0.5) / (2  a)
        x2 = (-b - d * 0.5) / (2  a)
        return f"Two roots: x1 = {x1}, x2 = {x2}"

if _name_ == "__main__":
    print(solve_quadratic(5, -9, -2))
    print(solve_quadratic(1, -4, 4))
    print(solve_quadratic(1, -5, 9))
    print(solve_quadratic(0, 1, 2))

#3. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
    #1) с помощью математических формул нахождения корней квадратного уравнения
    
    #2) с помощью дополнительных библиотек Python

#4. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
#5. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
#6. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#    1) с помощью математических формул нахождения корней квадратного уравнения
    
#    2) с помощью дополнительных библиотек Python

