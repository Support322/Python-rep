import math
from math import *

# Операторы
a = 13_000_000
b = 7

total = a + b
diff = a - b
prod = a * b
div1 = a / b
div2 = a // b
mod = a % b
exp = a ** b

print(a, '+', b, '=', total)
print(a, '-', b, '=', diff)
print(a, '*', b, '=', prod)
print(a, '/', b, '=', div1)
print(a, '//', b, '=', div2)
print(a, '%', b, '=', mod)
print(a, '**', b, '=', exp)


# Задача 1
a, b = float(input()), float(input())

print(a * b / 2)


# Задача 2
s, v1, v2 = float(input()), float(input()), float(input())

print(s / (v1 + v2))


# Задача 3
a = float(input())

if (a == 0):
    print("Обратного числа не существует")
else:
    print(a ** -1)


# Задача 4
t = float(input())

print((t - 32) * (5 / 9))


# Задача 5
year = float(input())

if (year == 1):
    print(10.5)
elif (year == 2):
    print(21)
else:
    print(21 + ((year - 2) * 4))

# Задача 6
a = float(input())

print(int(a * 10) % 10)


# Задача 7
a = float(input())
b = int(a)

print(a - b)


# Max and min
a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8)
print(a)
print(b)
print(c)


# Absolute
print(abs(10))
print(abs(-7))
print(abs(0))
print(abs(-17.67))


# Задача 8
a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())

max_a = int(max(a,b,c,d,e))
min_a = int(min(a,b,c,d,e))
print("Наименьшее число =", min_a)
print("Наибольшее число =", max_a)


# Задача 9
a, b, c = int(input()), int(input()), int(input())

if (a >= b and a >= c):
    print(a)
    if (b >= c):
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif (b >= a and b >= c):
    print(b)
    if (a >= c):
        print(a)
        print(c)
    else:
        print(c)
        print(a)
else:
    print(c)
    if (a >= b):
        print(a)
        print(b)
    else:
        print(b)
        print(a)


# Задача 10
a = int(input())

a1 = a // 100
a2 = a // 10 % 10
a3 = a % 10

a_max = max(a1, a2, a3)
a_min = min(a1, a2, a3)

if (a1 >= a2 and a1 >= a3):
    if (a2 >= a3):
        a_average = a2
    else:
        a_average = a3
elif (a2 >= a1 and a2 >= a3):
    if (a1 >= a3):
        a_average = a1
    else:
        a_average = a3
else:
    if (a1 >= a2):
        a_average = a1
    else:
        a_average = a2

if (a_max - a_min == a_average):
    print("Число интересное")
else:
    print("Число неинтересное")


# Задача 11
a, b, c, d, e = float(input()),  float(input()),  float(input()),  float(input()),  float(input())

print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))



# Задача 12
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())

print(abs(p1 - q1) + abs(p2 - q2))


# Длина строки
s1 = 'abcdef'
length1 = len(s1)               # считаем длину строки из переменной s1
length2 = len('Python rocks!')  # считаем длину строкового литерала
print(length1)
print(length2)


# Конкатенация
s1 = 'ab' + 'bc'
s2 = 'bc' + 'ab'
s3 = s1 + s2 + '!!'
print(s1)
print(s2)
print(s3)


# Задача 13
a ,b = input(), input()
s = "Hello " + a + " " +  b + "! You have just delved into Python"
print(s)


# Задача 14
name = input()
s = "Футбольная команда " + name + " имеет длину " + str(len(name)) + " символов"
print(s)


# Задача 15
a, b, c = input(), input(), input()

l_a = len(a)
l_b = len(b)
l_c = len(c)

mmax = max(l_a, l_b, l_c)
mmin = min(l_a, l_b, l_c)

if (len(a) == mmin):
    print(a)
elif (len(b) == mmin):
    print(b)
else:
    print(c)

if (len(a) == mmax):
    print(a)
elif (len(b) == mmax):
    print(b)
else:
    print(c)


# Задача 16
a, b, c = input(), input(), input()

l_a = len(a)
l_b = len(b)
l_c = len(c)

max_real = max(l_a, l_b, l_c)
min_real = min(l_a, l_b, l_c)
average_real = 0

if max_real == l_a:
    if min_real == l_b:
        average_real = l_c
    else:
        average_real = l_b
elif max_real == l_b:
    if min_real == l_a:
        average_real = l_c
    else:
        average_real = l_a
else:
    if min_real == l_a:
        average_real = l_b
    else:
        average_real = l_a

diff_a = int(average_real) - int(min_real)
diff_b = int(max_real) - int(average_real)

if (diff_a == diff_b):
    print("YES")
else:
    print("NO")


# Задача 17
a = input()
s = 'синий'

if (s in a):
    print("YES")
else:
    print("NO")


# Задча 18
a = input()
s1 = "суббота"
s2 = "воскресенье"

if (s1 in a or s2 in a):
    print("YES")
else:
    print("NO")


# Задача 19
a = input()
s1 = "@"
s2 = "."

if (s1 in a and s2 in a):
    print("YES")
else:
    print("NO")


# Использование math
num1 = math.sqrt(2)     # вычисление квадратного корня из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)


# Задача 20
import math

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

p = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
print(p)


# Задача 21
import math

r = float(input())

S = math.pi * r ** 2
C = 2 * math.pi * r

print(S)
print(C)


# Задача 22
import math

a, b = float(input()), float(input())

a1 = (a + b) / 2
a2 = math.sqrt(a * b)
a3 = (2 * a * b) / (a + b)
a4 = math.sqrt((a ** 2 + b ** 2)/2)

print(a1)
print(a2)
print(a3)
print(a4)


# Задача 23
import math

a = float(input())
r_a = (a * math.pi) / 180

value = math.sin(r_a) + math.cos(r_a) + math.tan(r_a) ** 2
print(value)


# Задача 24
import math

x = float(input())

up = math.ceil(x)
down = math.floor(x)

print(up + down)


# Задача 25
import math

a, b, c = float(input()), float(input()), float(input())

D = b ** 2 - 4 * a * c

if (D < 0):
    print("Нет корней")
elif (D == 0):
    print(-b / (2 * a))
else:
    xa = (-b - math.sqrt(D)) / (2 * a)
    xb = (-b + math.sqrt(D)) / (2 * a)
    if (xa >= xb):
        print(xb)
        print(xa)
    else:
        print(xa)
        print(xb)


# Задача 26
import math

n, a = int(input()), float(input())
S = (n * a ** 2) / (4 * math.tan(math.pi/n))

print(S)