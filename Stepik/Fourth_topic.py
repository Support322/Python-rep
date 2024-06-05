# Цикл for
for i in range(10):
    print('Привет')


# Цикл for
for i in range(5):
    num = int(input())
    print("Квадрат вашего числа равен:", num * num)

print("Цикл завершен")


# Цикл for
print("A")
print("B")

for i in range(5):
    print("C")
    print("D")

print("E")


# Цикл for
print('A')
print('B')

for i in range(5):
    print('C')

for i in range(5):
    print('D')

print('E')


# Задача 1
for i in range(10):
    print("Python is awesome!")


# Задача 2
a = str(input())
b = int(input())

for i in range(b):
    print(a)


# Задача 3
for i in range(6):
    print("AAA")
for i in range(5):
    print("BBBB")
print("E")
for i in range(9):
    print("TTTTT")
print("G")


# Задача 4
a = int(input())

for i in range(a):
    print("*******************")


# Цикл for
for i in range(10):
    print(i)


# Задача 5
a = input()

for i in range(10):
    print(i, a)


# Задача 6
a = int(input())

for i in range(a):
    print("Квадрат числа" , i , "равна", i ** 2)


# Задача 7
a = int(input())

for i in range(a + 1):
    print("Квадрат числа" , i , "равен", i ** 2)


# Задача 8
a = int(input())
k = a

for i in range(a + 1):
    print("*" * k)
    k-= 1


# Задача 9
m, p, n = int(input()), int(input()),int(input())

for i in range(n):
    if i == 0:
        print(i + 1, m)
    else:
        print(i + 1, m * (1 + p / 100) ** (i))


# Range с 2 переменными
for i in range(100, 1000):  # перебираем числа от 100 до 999
    if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
        print(i)


# Range с 3 переменными
for i in range(56, 171, 2):
    print(i)

for i in range(56, 171):
    if i % 2 == 0:
        print(i)


# Отрицательный for
for i in range(5, 0, -1):
    print(i, end=' ')
print('Взлетаем!!!')


# Задача 10
a, b = int(input()), int(input())

for i in range(a, b+1):
    print(i)

# Задача 11
min, max = int(input()), int(input()) # 8 1

if min > max:
    for i in range(min, max - 1, -1):
        print(i)
else:
    for i in range(min, max + 1):
        print(i)

# Задача 12
a, b = int(input()), int(input()) # 8 1
if a % 2 == 0:
    a = a - 1

for i in range(a, b - 1, -2):
    print(i)


# Задача 13
m, n = int(input()), int(input()) # 2 11

for i in range(m, n+1):
    if (i % 17 == 0) or (i % 10 == 9) or ((i % 3 == 0) and (i % 5 == 0)):
        print(i)


# Задача 14
n = int(input())

for i in range(1, 11):
    print(n , "x", i, "=", i * n)


# Счётик в for
counter = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1

print('Было введено', counter, 'чисел, больших 10.')


# Счётчики в for
counter1 = 0
counter2 = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1

print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )


# Подсчёт
counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1

print(counter)


# Подсчёт суммы
total = 0
for _ in range(10):
    num = int(input())
    if num > 10:
        total = total + num

print('Сумма чисел больших 10 равна',  total)


# Подсчёт натуральных чисел
total = 0
for i in range(1, 101):
    total = total + i

print('Сумма равна', total)


# Подмсчёт среднего значения
total = 0
for _ in range(10):
    num = int(input())
    total = total + num

average = total / 10
print('Среднее значение равно', average)


# обмен значениями
x , y = 15
x, y = y, x


# Натуральное ли число
num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False

if num == 1:
    print('Это единица, она не простая и не составная')
elif flag == True:
    print('Число простое')
else:
    print('Число составное')


# Поиск максимума
largest = 0
for _ in range(10):
    num = int(input())
    if num > largest:
        largest = num

print('Наибольшее число равно', largest)


# Аналогичная задача
largest = int(input())  # принимаем первое число за максимальное
for _ in range(9):
    num = int(input())
    if num > largest:
        largest = num

print('Наибольшее число равно', largest)


# Задача 15
a, b = int(input()), int(input()) # 3 9

total = 0
for i in range(a, b + 1):
    env = i ** 3
    if (env % 10 == 4) or (env % 10 == 9):
        total += 1
print(total)


# Задача 16
n = int(input()) # 5

total = 0
for i in range(n):
    tmp = int(input())
    total += tmp
print(total)


# Задача 17
import math

n = int(input()) # 2

total_br = 0
for i in range(1, n + 1):
    total_br += (1 / i)
res = total_br - math.log(n)
print(res)


# Задача 18
n = int(input())

total = 0
for i in range(1, n + 1):
    sqr = i ** 2
    if (sqr % 10 == 2) or (sqr % 10 == 5) or (sqr % 10 == 8):
        total += i
print(total)


# Задача 19
n = int(input())

total = 1
for i in range(1, n + 1):
    total *= i
print(total)


# Задача 20
total = 1

for i in range(1, 11):
    tmp = int(input())
    if tmp != 0:
        total *= tmp
print(total)


# Задача 21
n = int(input()) # 10

summ = 0
for i in range(1, n + 1):
    if (n % i == 0):
        summ += i
print(summ)


# Задача 22
n = int(input()) # 5 | 1 - 2 + 3 - 4 + 5

summ = 0
for i in range(1, n + 1):
    if (i % 2 == 0):
        summ -= i
    else:
        summ += i
print(summ)


# Задача 23
n = int(input())

a = []
for i in range(1, n + 1):
    tmp = int(input())
    a.append(tmp)
a.sort()
length = len(a)
print(a[length-1])
print(a[length-2])


# Задача 24
flag = True
for i in range(1, 11):
    tmp = int(input())
    if (tmp % 2 == 1):
        flag = False

if flag == True:
    print("YES")
else:
    print("NO")


# Задача 25
n = int(input())  # 3 | 1 1 2

a = []
for i in range(0, n):
    if (i == 0):
        a.append(i + 1)
    if (i == 1):
        a.append(i)
    if (i >= 2):
        tmp = a[i - 1] + a[i - 2]
        a.append(tmp)

for i in range(len(a)):
    print(a[i], end=" ")