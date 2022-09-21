# Анонимные, lambda функции
def sum(x):
 return x+10
def mult(x):
 return x**2
sum(mult(2))

def sum1(x):
 return x+22
def mult2(x):
 return x**3
sum1(mult2(2))

def sum3(x):
 return x+242
def mult4(x):
 return x**5
sum3(mult2(2))

sum = lambda x: x+10
mult = lambda x: x**2
sum(mult(2))

sum1 = lambda x: x+22
mult2 = lambda x: x**3
sum1(mult2(2))

sum4 = lambda x: x+242
mult4 = lambda x: x**5
sum3(mult2(2))

f(g(x))
def h(f, g, x): return f(g(x))h = lambda f, g, x: f(g(x))
h(sum, mult, 5)
h(lambda x: x+10, lambda x: x**2, 5)

f = open('f.txt', 'r')
data = f.read() + ' '
f.close()
numbers = []
while data != '':
 space_pos = data.index(' ')
 numbers.append(int(data[:space_pos]))
 data = data[space_pos+1:]
out = []
for e in numbers:
 if not e % 2:
 out.append((e,e **2))
print(out)

def select(f, col):
 return [f(x) for x in col]
def where(f, col):
 return [x for x in col if f(x)]
data = '1 2 3 5 8 15 23 38'.split()
data = select(int, data)
data = where(lambda e: not e % 2, data)
data = list(select(lambda e: (e, e**2), data))

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
data = list(map(lambda e: (e, e**2), data))
print(data)

