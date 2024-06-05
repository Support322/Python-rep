# Вывод данных
print("Привет, мир")

print(421)

print("Первое", "Второе", "Третье", sep="**")

print("Первое", "Второе", "Третье", end=" add ")
print("Четвертое", "Пятое", "шестое", end="\n")
print("New line")


# Ввод данных
a = input()
a, b, c = input(), input(), input()
a, b = b, a


# Целые числа и преобразования
a = 6
b = 15
c = int(input())
d = str(a)


# Возведение, остаток, деление
a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)

a = 5 ** 3
b = (7 * 3 - 2 + 8 * 5) / 13


# Задача 1
a, b = int(input()), int(input())

print("Квадрат суммы", a, "и", b, "равен", (a + b) ** 2)
print("Сумма квадратов", a, "и", b, "равна", a ** 2 + b ** 2)


# Задача 2
a, b, c, d = int(input()), int(input()), int(input()), int(input()),

print(a ** b + c ** d)


# Задача 3
a = int(input())

aa = a
bb = aa * 10 + aa
cc = aa * 100 + bb

print(aa + bb + cc)


# Задача 4
first = input ()

print(first)
print(int(first) + 1)
print(int(first) + 2)


# Задача 5
temp = int(input())

temp1 = temp * temp * temp
temp2 = 6 * temp * temp

print('Объем =', temp1)
print('Площадь полной поверхности =', temp2)

# Задача 6
temp1 = int(input())
temp2 = int(input())

res = 3 * (temp1 + temp2) * (temp1 + temp2) * (temp1 + temp2) + 275 * (temp2 * temp2) - 127 * temp1 -41

print(res)


# Задача 7
temp1 = int(input())

print("Следующее за числом", temp1, "число:", temp1 + 1)
print("Для числа", temp1, "предыдущее число:", temp1 - 1)


# Задача 8
a, b, c, d = int(input()), int(input()), int(input()), int(input())

print(3 * (a + b + c + d))


# Задача 9
a, b = int(input()), int(input())

print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)


# Задача 10
a, b, c = int(input()), int(input()), int(input())

print(a + b * (c - 1))


# Задача 11
a = int(input())

print(a, 2 * a, 3 * a, 4 * a, 5 * a, sep='---')


# Задача 12
a, b, c = int(input()), int(input()), int(input())

print(a * b ** (c - 1))


# Задача 13
a = int(input())

print(a // 2 + a % 2)


# Задача 14
a = int(input())

print((a + 3)//4)


# Задача 15
a = int(input())

print(a, 'мин - это', a // 60, 'час', a % 60, 'минут.')


# Задача 16
a = int(input()) #523

a1 = a // 100 #5
a12 = a % 100 #23
a2 = a12 // 10 #2
a3 = a12 % 10 #3

print("Сумма цифр =", a1 + a2 + a3)
print("Произведение цифр =", a1 * a2 * a3)


# Задача 17
temp = int(input()) # 732

a = temp // 100 # 7
temp12 = temp % 100 # 32
b = temp12 // 10 # 3
c = temp12 % 10 # 2

print(a, b, c, sep = '')
print(a, c, b, sep = '')
print(b, a, c, sep = '')
print(b, c, a, sep = '')
print(c, a, b, sep = '')
print(c, b, a, sep = '')