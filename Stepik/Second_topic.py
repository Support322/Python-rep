# Условный оператор if-else
answer = input('Какой язык программирования мы изучаем?')
if answer == 'Python':
    print('Верно! Мы ботаем Python =)')
    print('Python - отличный язык!')
else:
    print('Не совсем так!')


# Задача 1
num1 = int(input())
num2 = int(input())

if num1 < num2:
    print(num1, 'меньше чем', num2)
if num1 > num2:
    print(num1, 'больше чем', num2)

if num1 == num2:  # используем двойное равенство
    print(num1, 'равно', num2)
if num1 != num2:
    print(num1, 'не равно', num2)


# Задача 2
age = int(input())
if 3 <= age <= 6:
    print('Вы ребёнок')


# Задача 4
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('числа равны')
else:
    print('числа не равны')



# Задача 5
word = input()

if word == 'Python':
    print('ДА')
else:
    print('НЕТ')


# Задача 6
num = int(input())

last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')


# Задача 7
num1, num2, num3 = int(input()), int(input()), int(input())

counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)


# Задача 8
first = input()
second = input()
if (first == second):
    print("Пароль принят")
else:
    print("Пароль не принят")


# Задача 9
temp = int(input())
if (temp % 2 == 0):
    print("Четное")
else:
    print("Нечетное")


# Задача 10
main = int(input())
a = main // 1000
b = main // 100 % 10
c = main // 10 % 10
d = main % 10
if a + d == b - c:
    print("ДА")
else:
    print("НЕТ")


# Задача 11
age = int(input())
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")


# Задача 12
a, b, c = int(input()), int(input()), int(input())
ab = b - a
bc = c - b
if (ab == bc):
    print("YES")
else:
    print("NO")


# Задача 13
a, b = int(input()), int(input())

if (a > b):
    print(b)
else:
    print(a)


# Задача 14
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (a <= b) and (a <= c) and (a <= d):
    print(a)
elif (b <= a) and (b <= c) and (b <= d):
    print(b)
elif (c <= a) and (c <= b) and (c <= d):
    print(c)
else:
    print(d)


# Задача 15
age = int(input())

if (age <= 13):
    print("детство")
elif (age > 13) and (age <= 24):
    print("молодость")
elif (age > 24) and (age <= 59):
    print("зрелость")
else:
    print("старость")


# Задача 16
a, b, c = int(input()), int(input()), int(input())
sum = 0

if a > 0:
    sum += a
if b > 0:
    sum += b
if c > 0:
    sum += c
print(sum)


# Задача 17
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))

if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')


# Задача 18
city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')


# Задача 19
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')

if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')


# Задача 20
num = int(input())
if 100 <= num <= 999:     # num >= 100 and num <= 999
    print('Число является трёхзначным')
else:
    print('Число не является трёхзначным')


# Задача 21
num = int(input())
d3 = num % 10
d2 = num % 100 // 10
d1 = num // 100
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')


# Задача 22
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1 четверть')
if x < 0 and y > 0:
    print('2 четверть')
if x < 0 and y < 0:
    print('3 четверть')
if x > 0 and y < 0:
    print('4 четверть')


# Задача 23
num1 = 34
num2 = 81
if num1 // 9 == 0 or num2 % 9 == 0:
    print('число', num1, 'выиграло')
else:
    print('число', num2, 'выиграло')


# Задача 24
a = int(input())

if a >= 2 and a <= 17:
    b = 3
    p = a * a + b * b
else:
    b = 5

p = (a + b) * (a + b)
print(p)

# Задача 25
a = int(input())

if (-30 < a <= -2) or (7 < a <= 25):
    print("Принадлежит")
else:
    print("Не принадлежит")


# Задача 26
a = int(input())

if ((a % 7 == 0) or (a % 17 == 0)) and ( 1 <= a // 1000 <= 9):
    print("YES")
else:
    print("NO")


# Задача 27
a, b, c = int(input()), int(input()), int(input())

if (a + c > b) and (a + b > c) and (b + c > a):
    print("YES")
else:
    print("NO")


# Задача 28
year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("YES")
else:
    print("NO")


# Задача 29
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (a == c) or (b == d):
    print("YES")
else:
    print("NO")


# Задача 30
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if ((c + 1 == a or c - 1 == a or c == a)) and ((d + 1 == b or d - 1 == b or d == b)):
    print("YES")
else:
    print("NO")



# Задача 31
x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print('Первая четверть')
    else:
        print('Четвертая четверть')
else:
    if y > 0:
        print('Вторая четверть')
    else:
        print('Третья четверть')


# Задача 32
grade = int(input('Введите вашу отметку по 100-балльной системе: '))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70:
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)

grade = int(input('Введите вашу отметку: '))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)


# Задача 33
traffic_light_signal = input("Введите сигнал светофора: ")

if traffic_light_signal == "красный":
    print("Стой!")
elif traffic_light_signal == "желтый":
    print("Приготовься...")
elif traffic_light_signal == "зеленый":
    print("Иди!")


# Задача 34
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)


# Задача 35
a, b = int(input()), int(input())

if (a > b):
    print("NO")
elif (b > a):
    print("YES")
else:
    print("Don't know")



# Задача 36
a, b, c = int(input()), int(input()), int(input())

if (a == b == c):
    print("Равносторонний")
elif (a == b or a == c or b == c):
    print("Равнобедренный")
else:
    print("Разносторонний")



# Задача 37
a, b, c = int(input()), int(input()), int(input())

if ((b < a < c) or (c < a < b)):
    print(a)
if ((a < b < c) or (c < b < a)):
    print(b)
if ((a < c < b) or (b < c < a)):
    print(c)


# Задача 38
month = int(input())

if (month == 1 or month == 12 or month == 5 or month == 3 or month == 7 or month == 8 or month == 10):
    print(31)
if (month == 6 or month == 4 or month == 9 or month == 11):
    print(30)
if (month == 2):
    print(28)


# Задача 39
weight = int(input())

if (weight < 60):
    print("Легкий вес")
elif (60 <= weight < 64):
    print("Первый полусредний вес")
elif (64 <= weight < 69):
    print("Полусредний вес")


# Задача 40
a, b, line = int(input()), int(input()), str(input())

if (line == '/'):
    if b == 0:
        print("На ноль делить нельзя!")
    else:
        print(a / b)
elif (line == '*'):
    print(a * b)
elif (line == '+'):
    print(a + b)
elif (line == '-'):
    print(a - b)
else:
    print("Неверная операция")


# Задача 41
a, b = str(input()), str(input())

if ((a == b) and (a == 'красный' or a == 'синий' or a == 'желтый')):
    print(a)
elif ((a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий')):
    print('фиолетовый')
elif ((a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый')):
    print('оранжевый')
elif ((a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый')):
    print('зеленый')
else:
    print("ошибка цвета")


# Задача 42
a = int(input())

if (0 <= a <= 36):
    if (a == 0):
        print('зеленый')
    elif (a % 2 == 0):
        if (1 <= a <= 10):
            print('черный')
        elif (11 <= a <= 18):
            print('красный')
        elif (19 <= a <= 28):
            print('черный')
        else:
            print('красный')
    else:
        if (1 <= a <= 10):
            print('красный')
        elif (11 <= a <= 18):
            print('черный')
        elif (19 <= a <= 28):
            print('красный')
        else:
            print('черный')
else:
    print('ошибка ввода')


# Задача 43
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if ((a1 < a2 and a1 < b2) and (b1 < a2 and b1 < b2)):
    print('пустое множество')
elif ((a2 < a1 and a2 < b1) and (b2 < a1 and b2 < b1)):
    print('пустое множество')

elif ((a1 < a2 and a1 < b2) and (b1 > a2 and b1 < b2)):
    print(a2, b1)
elif ((a2 < a1 and a2 < b1) and (b2 > a1 and b2 < b1)):
    print(a1, b2)
elif ((a1 < a2 and a1 < b2) and (b1 > a2 and b1 > b2)):
    print(a2, b2)
elif ((a2 < a1 and a2 < b1) and (b2 > a1 and b2 > b1)):
    print(a1, b1)
elif ((a1 == a2 and a1 < b2) and (b1 > a2 and b1 < b2)):
    print(a1, b1)
elif ((a2 == a1 and a2 < b1) and (b2 > a1 and b2 < b1)):
    print(a1, b2)
elif ((a1 > a2 and a1 < b2) and (b1 > a2 and b1 == b2)):
    print(a1, b1)
elif ((a2 > a1 and a2 < b1) and (b2 > a1 and b2 == b1)):
    print(a2, b1)
elif ((a1 == a2 and a1 < b2) and (b1 > a2 and b1 == b2)):
    print(a1, b1)

elif ((a1 < a2 and a1 < b2) and (b1 == a2 and b1 < b2)):
    print(b1)
elif ((a2 < a1 and a2 < b1) and (b2 == a1 and b2 < b1)):
    print(b2)


# Задачка 44
year = int(input()) #5215

if (year % 100 == 0):
    print("YES")
else:
    print("NO")


# Задачка 45
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
p1 = True
p2 = True

if ((x1 % 2 == 0) and (y1 % 2 == 0)):
    p1 = False

if ((x1 % 2 == 1) and (y1 % 2 == 1)):
    p1 = False

if ((x2 % 2 == 0) and (y2 % 2 == 0)):
    p2 = False

if ((x2 % 2 == 1) and (y2 % 2 == 1)):
    p2 = False

if (p1 == p2):
    print("YES")
else:
    print("NO")


# Задачка 46
year = int(input())
sex = str(input())

if ((10 <= year <= 15) and (sex == 'f')):
    print("YES")
else:
    print("NO")


# Задачка 47
value = int(input())

if (value == 1):
    print("I")
elif (value == 2):
    print("II")
elif (value == 3):
    print("III")
elif (value == 4):
    print("IV")
elif (value == 5):
    print("V")
elif (value == 6):
    print("VI")
elif (value == 7):
    print("VII")
elif (value == 8):
    print("VIII")
elif (value == 9):
    print("IX")
elif (value == 10):
    print("X")
else:
    print("ошибка")


# Задачка 48
value = int(input())

if (value % 2 == 0):
    if (2 <= value <= 5):
        print("NO")
    elif (6 <= value <= 20):
        print("YES")
    elif (value > 20):
        print("NO")
else:
    print("YES")


# Задачка 49
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
temp_x = 0
temp_y = 0

if (x1 > x2):
    temp_x = x1 - x2
elif (x1 < x2):
    temp_x = x2 - x1

if (y1 > y2):
    temp_y = y1 - y2
elif (y1 < y2):
    temp_y = y2 - y1

if (temp_x == temp_y):
    print("YES")
else:
    print("NO")


# Задачка 50
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 + 1 == x2 and y1 + 2 == y2):
    print("YES")
elif (x1 + 2 == x2 and y1 + 1 == y2):
    print("YES")
elif (x1 - 1 == x2 and y1 + 2 == y2):
    print("YES")
elif (x1 + 2 == x2 and y1 - 1 == y2):
    print("YES")
elif (x1 - 1 == x2 and y1 - 2 == y2):
    print("YES")
elif (x1 - 2 == x2 and y1 - 1 == y2):
    print("YES")
elif (x1 - 2 == x2 and y1 + 1 == y2):
    print("YES")
elif (x1 + 1 == x2 and y1 - 2 == y2):
    print("YES")
else:
    print("NO")


# Задачка 51
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# вокруг
if ((x1 - 1 == x2 and y1 - 1 == y2) or (x1 == x2 and y1 - 1 == y2) or (x1 + 1 == x2 and y1 - 1 == y2) or (
        x1 + 1 == x2 and y1 == y2) or (x1 + 1 == x2 and y1 + 1 == y2) or (x1 == x2 and y1 + 1 == y2) or (
        x1 - 1 == x2 and y1 + 1 == y2) or (x1 - 1 == x2 and y1 == y2)):
    print("YES")

# параллельно
elif ((x1 + 1 == x2 and y1 == y2) or ((x1 + 2 == x2 and y1 == y2)) or (x1 + 3 == x2 and y1 == y2) or (
        x1 + 4 == x2 and y1 == y2) or (x1 + 5 == x2 and y1 == y2) or (x1 + 6 == x2 and y1 == y2) or (
              x1 + 7 == x2 and y1 == y2)):
    print("YES")
elif ((x1 - 1 == x2 and y1 == y2) or ((x1 - 2 == x2 and y1 == y2)) or (x1 - 3 == x2 and y1 == y2) or (
        x1 - 4 == x2 and y1 == y2) or (x1 - 5 == x2 and y1 == y2) or (x1 - 6 == x2 and y1 == y2) or (
              x1 - 7 == x2 and y1 == y2)):
    print("YES")
elif ((x1 == x2 and y1 + 1 == y2) or ((x1 == x2 and y1 + 2 == y2)) or (x1 == x2 and y1 + 3 == y2) or (
        x1 == x2 and y1 + 4 == y2) or (x1 == x2 and y1 + 5 == y2) or (x1 == x2 and y1 + 6 == y2) or (
              x1 == x2 and y1 + 7 == y2)):
    print("YES")
elif ((x1 == x2 and y1 - 1 == y2) or ((x1 == x2 and y1 - 2 == y2)) or (x1 == x2 and y1 - 3 == y2) or (
        x1 == x2 and y1 - 4 == y2) or (x1 == x2 and y1 - 5 == y2) or (x1 == x2 and y1 - 6 == y2) or (
              x1 == x2 and y1 - 7 == y2)):
    print("YES")

# диагональ
elif ((x1 + 1 == x2 and y1 + 1 == y2) or ((x1 + 2 == x2 and y1 + 2 == y2)) or (x1 + 3 == x2 and y1 + 3 == y2) or (
        x1 + 4 == x2 and y1 + 4 == y2) or (x1 + 5 == x2 and y1 + 5 == y2) or (x1 + 6 == x2 and y1 + 6 == y2) or (
              x1 + 7 == x2 and y1 + 7 == y2)):
    print("YES")
elif ((x1 - 1 == x2 and y1 - 1 == y2) or ((x1 - 2 == x2 and y1 - 2 == y2)) or (x1 - 3 == x2 and y1 - 3 == y2) or (
        x1 - 4 == x2 and y1 - 4 == y2) or (x1 - 5 == x2 and y1 - 5 == y2) or (x1 - 6 == x2 and y1 - 6 == y2) or (
              x1 - 7 == x2 and y1 - 7 == y2)):
    print("YES")
elif ((x1 + 1 == x2 and y1 - 1 == y2) or ((x1 + 2 == x2 and y1 - 2 == y2)) or (x1 + 3 == x2 and y1 - 3 == y2) or (
        x1 + 4 == x2 and y1 - 4 == y2) or (x1 + 5 == x2 and y1 - 5 == y2) or (x1 + 6 == x2 and y1 - 6 == y2) or (
              x1 + 7 == x2 and y1 - 7 == y2)):
    print("YES")
elif ((x1 - 1 == x2 and y1 + 1 == y2) or ((x1 - 2 == x2 and y1 + 2 == y2)) or (x1 - 3 == x2 and y1 + 3 == y2) or (
        x1 - 4 == x2 and y1 + 4 == y2) or (x1 - 5 == x2 and y1 + 5 == y2) or (x1 - 6 == x2 and y1 + 6 == y2) or (
              x1 - 7 == x2 and y1 + 7 == y2)):
    print("YES")
else:
    print("NO")
