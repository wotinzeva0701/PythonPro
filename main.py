# print("Вносим изменения"

# print("Данные переносим на GitHub!")

#
# Занятие 16.03
#
# t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
# print(t2)
#
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)
#
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)
#
#
# t = ('abcd', 'abc', 'asdfg', 'def', 'ert')
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
#
# b = [60, 90, 68, 5, 76, 60, 88,74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)
#
#
#
# from random import randint
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
#
# lst2 = list(filter(lambda t: 10 <= t <= 20, lst))
# print(lst2)
#
# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)
#
#
#
#
#
# дописать
#
#
#
# Занятие 17.03
#
# Строки
#
# print(01)
# print(bin(18)) # 0b10010 - 0b - двоичная система
# print(oct(18)) # Oo22 => Oo - восьмиричная
# print(hex(18)) # Ox12 => Ox - шестнадцатеричная
#
# print(0b10010 + 0o22)
# print(0o22)
# print(0x12 + 18)
#
# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e) # python => Pytton
# print(e * 3)
# print("y" in e)
# print("l" in e)
# print(e[1])
# print(e[-1])
# print(e[1:4])
# print(e[::-1])
#
# e = e[:3] + 't' + e[4:]
# print(e)
#
#
# print("Привет")
# print(u"Привет")
#
# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
# print(r"C:\folder\\"[:-1])
# print(r"C:\folder" + "\\")
# print("C:\\folder\\")
#
#
# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + "лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")
# print(a)
# print(f"Число: {round(12.2564)}, {5 + 3}")
# print(f"Число: {12.2564:.2f}")
#
#
# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")
#
#
# dir_name = "folder"
# file_name = file.txt
# print(fr"home\{dir_name}\{file_name}")
# print("home" +"\\" + dir_name + "\\" + file_name)
#
# s = """Строка символов"""
# print(s)
#
# s1= '''Строка символов'''
# print(s1)
#
# s2 = "Строка символов"
# print(s2)
#
#
# def square(n):
#     """Принимает число  n, возвращает число n"""
#     return n ** 2
#
#
# print(square(5))
#
#
#
# from math import pi
#
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :param: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)
# print(sum.__doc__)
# print(len.__doc__)
# print(int.__doc__)
# print(type.__doc__)
#
# print(ord('a'))
# print(ord('й'))

# while True:
#       n = input("->")
#       if n != "-1":
#            print(ord(n))
#       else:
#           break
#


# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr +=[ord(x) for x in input("->")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) -1)
# arr.sort(reverse=True)
# print(arr)


# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 97
# b = 122
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# if b > a:
#     a, b = b, a  # a = 122, b = 97
#
# for i in range(b, a + 1):
#     print(chr(i), end=" ")


# print("apple" == "Apple")
# print("apple" > "Apple")  # 97 > 65

# from random import randint

# min_ascii = 33
# max_ascii = 126
# shortest = 6
# longest = 16
#
#
# def random_password():
#     res = ""
#     for i in range(randint(shortest, longest)):
#         res += chr(randint(min_ascii, max_ascii))
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# Методы строк

# s = "hello, WORlD! I am learning Python."
# print(s)
# a = s.capitalize()
# print(a)  # Hello, WORlD! I am learning Python.
# print(s.lower())  # hello, WORlD! I am learning Python.
# print(s.upper())  # HELLO, WORlD! I AM LEARNING Python.


# s = "hello, WORlD! I am learning Python."
# print(s)
#
# print(s.count('l'))
# print(s.lower(). count('l'))


# Методы строк
#
# s = "hello, WORLD! I am learning Python."
# print(s)
# a = s.capitalize()
# print(a)
# print(s.lower())  # hello, world! I am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.count('l'))
# print(s.lower().count('l'))

# print(s.count('h', 1, -4))
# print(s.count('h'))

# print(s.find("Python"))  # поиск подстроки в строке, возвращает индекс совпадения, если совпадение нет вернет "-1"
# print(s.index("Python"))  # поиск подстроки в строке, возвращает индекс совпадения, если совпадение нет вернет
# исключение "ValueError"

# print(s.find("h", 1, -4))
# print(s.rfind("h1"))
# print(s.rindex("h1"))


# st = input("Введите два слова через пробел: ")
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
#
# print(second + " " + first)


# s = "hello, WORLD! I am learning Python."
# print(s)
#
# print(s.endswith("on.")) # заканчивается ли строка на заданную подстройку -  (True, False)
# print(s.endswith("I am", 14))  # начинается ли строка на заданной подстроки - (True, False)
# print(s.find("I am"))


# a = input("Введите число: ")
# ty:
#    a = int(a)
#    print(a ** 2)
# except ValueError:
#     print("Нужно ввести число")
#
# #
# print('123'. isdigit())  # состоит ли строка только из чисел
# print('123a'. isdigit())
#
# a = input("Введите число: ")
# b = 2
# if a.isdigit():
#     a = int(a)
#     print(a + b)
# else:
#     print(a + str(b))

# print("abc123!".isalnum())  #  Состоит ли строка только из букв и цифр
# print("ABCabc".isalpha())  #  Состоит ли строка только из букв
#
# print("abc123!@#". islower())  # определяет, являются ли буквенные символы строки в нижнем регистре
# print("ACV123!@#". isupper())  # определяет, являются ли буквенные символы строки в верхнем регистре

# print('py'.center(10))
# print('py'.center(11, "-"))
# print('py'.center(1))

# print("  py  ".lstrip())
# print("  py  ".rstrip())
# print("  py  ".strip())
#
# print("https://www.python.org".lstrip("/:pths"))
# print("https://www.python.orgw".strip("/:pthsw"))
# print("https://www.python.orgw".lstrip("/:pths").rstrip("w"))
#
# s = "hello, Python ! I am learning Python. Python"
# print(s.replace("Python", "Java", 2))  # поиск и замена
#
#
# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '2']))  # объединяет итерируемый объект в строку через символ разделитель
#
# print(":".join("Hello"))

# print("a b c".split())
# print("www.python.org".split(".", 1))
# print("www.python.org".rsplit(".", 1))

# Регулярное выражение

# import re

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r"\."
# print(re.findall(reg, s))  # возвращает список, содержащий все совпадения шаблонов
# print(re.search(reg, s))   # возвращает первое совпадение с  шаблоном
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))  # поиск по шаблону в начале строки
# print(re.split(reg, s, 3))  # возвращает список, в котором строка разбита по шаблону
# print(re.sub(reg, "!", s, 1))  # поиск и замена

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счё_та. 198765. Hello"
# reg = r"[204]"
# reg = r"[2-4]"
# reg = r"[A-Za-z]\."
# print(re.findall(reg, s))
# print(ord("Ё"))  # 1025
# print(ord("А"))  # 1040
# print(ord("Я"))  # 1071
# print(ord("а"))  # 1072
# print(ord("я"))  # 1103
# print(ord("ё"))  # 1105

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т91:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т04:09"
# pattern = "[0-2][0-3]:[0-5][0-9]"
# print(re.findall(pattern, st))


# недописала
# pattern = r"^[A-Za-z0-9 _@-]{6,18}$"
# print(pattern)
# def valid_login(name):
#     return re.findall("^[A-Za-z0-9_-]{3,16}$", name)
#
#
# print(valid_login("Python_master"))
# print(valid_login("#@!Python"))


# def check(password):
#     return re.findall(r"[A-Za-z0-9_@-]{6,18}$", password)
#
#
# print(check("Pas_12@"))
# print(check("Pasw!#3"))


#
# 30.03.24
#
#
# text = """Python,
# python,
# PYTHON"""
# reg = "(?mi)^python"
# print(re.findall(reg, text))
#
# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*>", text))  # [<body>, </body>]
#
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
#
# s1 = "12 сентября 2024 года 4567897"
# reg1 = r"\d{2,4}"
# print(re.findall(reg1, s1))
#
#
# s = "Петр, Ольга и  Виталий отлично учатся!"
# reg = r"Ольга|Виталий"
# print(re.findall(reg, s))
#
#
# s = "int = 4, float = 4.0f, double = 8.0, float"
# reg = r"int\w+\s*=\s*[.\w+]*|float"\s*=\s*[.\w+]*
# reg = r"(?:int|float)\s*=\s*[.\w+]*"
# print(re.findall(reg, s))
# print(re.search(reg, s))
#
# #(?:...) - обозначает, что эта группирующая скобка является не сохраняющей
#
#
# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))
#
#
# a = "08-08-2021"
# pattern = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19\d\d|20[0-9][0-9])"
# print(re.findall(pattern, a))
# print(re.search(pattern, a).group())
# m = re.search(pattern,a))
# print(m([0]))
# print(m([1]))
# print(m([2]))
# print(m([3]))
#
# s = "Самолет прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024" № 23.10.2024
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))
#
#
# s = "yandex.com and yandex.com.ru"
# reg = r"((a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))
#
#
# # Рекурсия
#
# def elevator(n)  # 5
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1) # стек: 5 4 3 2 1
#     print(n, end=" ")
#
#
#
# n1 = int(input("На каком вы этаже: "))  # 5
# elevator(n1)
#
#
#
# def = sum_lst(lst):
#       res = 0
#       for i in lst:
#           res += 1
#       return res
#
#
# def = sum_lst(lst):  # [3, 5, 7, 9]
#       if len(lst) == 1:
#       print(lst, "=> lst[0]:", lst[0])
#          return lst[0]  # 9
#       else:
#           print(lst, "=> lst[0]:", lst[0])
#           return lst[0] + sum_list(lst[1:]) # 1 + 3 + 5 + 7 +
#
#
# print(sum_lst[1, 3, 5, 7, 9])) # 25
#
#
#
# def to_str(n, base):  # n = 3
#     convert = "012345679ABCDEF"
#     if n < base:
#          return convert[n] # convert[3] => '3'
#     else:
#         return to_str(n // base, base) + convert[n % base]  #  convert[5] => [4 остаток] => '5' + '4'
#
#
# print(to_str(354, 10))
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#            count += item_list(item)
#         else:
#             count += 1
#      return count
#
#
# names = ['Adam', ['Bob', ['Chat', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], "Ann"]
# print(names)
# print(len(names))
# print(isinstance(names, list))
# print(isinstance(names[0], list))
# print(isinstance(names[1][0][0], list))
#
# print(count_items(names))
#
#
# def remove(text):
#     if not text:
#          return ""
#     if text[0] == "\n" or text[0] == " ":
#        return remove(text[1])
#     else:
#         return text[0] + remove(text[1:])
#
#
#
# print(remove("Hello\nWord"))
#
#
# print(bool(""))
#
#
#
# 31.03.

# f = open("test.txt", "r")
# f = open("test.txt", "r")
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# print(f.closed)
# f.close()

# f = open("test.txt", "r")
# print(f.read(3))
# print(f.read())
# f.close()
#
#
# f = open("test.txt", "r")
# print(f.read())
# f.close()
#
#
# f = open("test1.txt", "r")
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()
#
#
# f = open("test1.txt", "r")
# print(f.readline(26))
# print(f.readline())
# f.close()
#
#
# f = open("test1.txt", "r")
# print("count =", len(f.readlines()))
# f.close()
#
#
#
# f = open("test1.txt", "r")
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print("count =", count)
#
#
# f = open("xyz.txt", "w")
# f.write("Hello\nWorld!")
# f.close()
#
#
# f = open("xyz1.txt", "a")
# f.write("\nNew text")
# f.close()
#
# line = ['This is line 1\n', 'This is line 2\n']
# f = open("xyz.txt", "w")
# f.writelines(line)
# f.close()
#
#
#
# lst = [i for i in range(1, 20)]
# print(lst)
#
# f = open("xyz.txt", "w")
# for index in lst:
# f.write("\t".join(map(str, lst)))
# f.close()
#
#
#
# f = open("xyz.txt", "w")
# d = f.read()
# st = list(map(int, d.split("\t")))
# print(st)
# print(type(st[0]))
# f.close()
#
#
# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
#
# f = open(file, "r")
# read_line = f.readlines()
# print(read_line)
# read_line[1] = "Hello world!"
# print(read_line)
# f.close()
#
# f = open(file, "w")
# f.writelines(read_line )
# f.close()
#
#
#
#
# file = "text2.txt"
#
# f = open(file, "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
#
# f = open(file, "r")
# s = f.writelines()
# f.close()
# print(s)
#
# pos = int(input("pos = "))
# if 0 <= pos < len(s):
#      del s[pos]
# else:
#     print("Индекс введен неверно")
# print(s)
#
#
# f = open(file, "w")
# f.writelines(s)
# f.close()
#
#
#
# f = open("test.txt")
# print(f.read(3))
# print(f.tell()) # позиция условного курсора
# print(f.seek(1)) # перемещение условного курсора в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()
#
#
#
# f = open("test.txt", "r+")
# f.write("I am learning Python")
# print(f.seek(3))
# f.write("-new string-")
# f.close()
#
#
#
#
# f = open("test45.txt", "a+")
# f.write("I am learning Python")
# print(f.seek(3))
# f.write("-new string-")
# f.close()
#
#
#
# with open('test.txt', "w") as f:
#     print(f.write('012\n34567\n89'))
# print(f.closed)
#
#
#
# with open('test.txt', "w") as f:
#     for line in f:
#         print(line[:2])
#
#
# # Файл (англ. file) — именованная область данных на носителе
# # информации, используемая как базовый объект взаимодействия с данными
# #  в операционных системах.
#
# def longest_words(file):
#     with open(file, "r") as text:  # , encoding="utf-8
#          w = text.read().split()
#          print(w)
#          max_lenght = len(max(w, key=len))
#          res = [word for word in w if len(word) == max_length]
#          print(max_lenght)
#          if len(res) == 1:
#             retutn res[0]
#          return res
#
#
# print(longest_words('test.txt'))
#
#
#
# one = "one.txt"
# two = "two.txt"
#
#
# text = "Строка №1\nСтрока №2\n"Строка №3\n"Строка №4\n"Строка №5\n"Строка №6\n"Строка №7\nСтрока №8\n"Строка №9
# \n"Строка №10\n"
# with open(one, 'w') as f:
#     f.write(text)
#
#
# with open(one,"r") as fr, open(two, "w") as fw:
#      for line in fr:
#          line = line.replace("Строка", "Линия -")
#          tw.write(line)
#
# one = "one.txt"
# two = "two.txt"
# three.txt = "three.txt"
#
# with open(one, "r") as f1:
#     a = f1.read()
#     print(a)
#
# with open(two, "r") as f2:
#     b = f2.read()
#     print(b)
#
# c = a + b
# print(c)
#
#
# with open(three, "w") as f3:
#     f3.writelines(c)
#
#
#
# with open(one, "r") as f1, open(two, "r") as f2, open(three, "w") as f3:
#     a = f1.readlines()
#     b = f2.readlines()
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     print(a)
#     print(b)
#     print(c)
#     f3.writelines(c)


