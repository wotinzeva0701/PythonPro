# print("Вносим изменения"
# import csv

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
# print(bin(18)) # 0b10010 - 0b - 2 система
# print(oct(18)) # Oo22 => Oo - 8
# print(hex(18)) # Ox12 => Ox - шестнадцатеричная
#
# print(0b10010 + 0o22)
# print(0o22)
# print(0x12 + 18)
#
# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e) # python => Python
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
# print("ABC abc".isalpha())  #  Состоит ли строка только из букв
#
# print("abc123!@#". islower())  # определяет, являются ли буквенные символы строки в нижнем регистре
# print("ACV123!@#". isupper())  # определяет, являются ли буквенные символы строки в верхнем регистре

# print('py'.center(10))
# print('py'.center(11, "-"))
# print('py'.center(1))

# print("  py  ". ())
# print("  py  ". ())
# print("  py  ".strip())
#
# print("https://www.python.org".("/:pths"))
# print("https://www.python.orgw".strip("/:"))
# print("https://www.python.orgw".("/:pths").("w"))
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
# print(check("!#3"))


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
# print("count =", len(f.readline()))
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
# f.write("Замена строки в текстовом файле;\n изменить строку в списке;\n записать список в файл;")
# f.close()
#
#
# f = open(file, "r")
# read_line = f.readline()
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
# f.write("Замена строки в текстовом файле;\n изменить строку в списке;\n записать список в файл;")
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
#          max_length = len(max(w, key=len))
#          res = [word for word in w if len(word) == max_length]
#          print(max_length)
#          if len(res) == 1:
#             return res[0]
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
#     a = f1.readline()
#     b = f2.readline()
#     c = []
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     print(a)
#     print(b)
#     print(c)
#     f3.writelines(c)


# Модули
#
# import os
#
# дописать  и исправить!!!

#
# for root, dirs, in os.walk("nested1", topdown=False):
#     print("Root:", root)
#     print("\:", dirs)
#     print("\tFiles:", files)
#
#
# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#         print(f"Директория {root} удалена")
#     print("-" * 50)
#
#
# remove_empty_dirs("nested1")
#
#
#
# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)
#
# files = {
#     'Work': ['w.txt'],
#      r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#      r'Work\F2\F21': ['f11.txt', 'f12.txt']
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, "w").close()
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_with_text:
#     with open(file, 'w') as f:
#          f.write(f"Текст для файла {file}")

#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'Сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, files in os.walk(root, topdown):
#
#           print(root)
#           print(dirs)
#           print(files)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)
#
#
# print(os.path.exists(r"D:\Python318\318\nested1\nested2\nested3\text.txt"))  # возвращает True если путь существует в
# # файловой системе

#
# import time
#
# path = "main.ry"
# print(os.path.getsize(path) / 1024) # размер файла 81693 байт(79.826171875 КB)
#
#
# print(os.path.getctime(path)   #  время создания файла
# print(os.path.getctime(path)   #  время последнего доступа к файлу
# print(os.path.getctime(path)   #  время последнего изменения файла (в секундах)
#
#
# time.("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path)))
# time.("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getmtime(path)))
#
#
# print(os.path.isdir(r"D:\Python318\318\nested1\nested2\nested3"))
# print(os.path.isfile(r"D:\Python318\318\nested1\nested2\nested3\text.txt"))


# class Point:

#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 30
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
#
#
# p2 = Point()
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)
#
#
# print(id(Point))
# print(id(p1))
# print(id(p2))
#
#
# print(Point.__dict__)
# print(Point.__doc__)

#
# домашняя работа
# import os
#
# dir_name = "nested1"
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     print(p)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(P)} bytes")
#
#     elif os.path.isdir(p):
#         print(f"{obj} - dir")
#
# 7.04
#
#
# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# Point.set_coord(5, 10)
#
# p2 = Point()
# p2.x = 3
# p2.y = 7
# p2.set_coord(3, 7)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print("Персональные данные ".center(48, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)

#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем новое имя
#         self.name = name  # получаем имя
#
#     def get_name(self):
#         return self.name
#
#     def set_birthday(self, value):
#         self.birthday = value
#
#     def set_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Юлия")
# print(h1.get_name)
# h1.set_birthday("25.05.1986")
# print(h1.get_birthday())
# #
#
# class Person:
#     skill = 10  # статические свойства
#
#
# def __init__(self, name, surname):  Инициализатор
#
#
# self.name = name  # динамические свойства
# self.surname = surname
# print("Инициализатор Person")
# value = 5
#
#
# def __del__(self):
#     print("Удаление экземпляра класса")
#
#
# def print_info(self, name, surname):
#     self.name = name
#     self.surname = surname
#     print("Данны о сотрудника:", self.name, self.surname)
#
#
# def add_skill(self, k):
#     self.skill += k
#     print("Квалификация сотрудника:", self.skil, end="\n\n")
#
#
# p1 = Person()
# p1.print_info("Виктор", "Резник")
# p1.add_skill(3)
#
# p2 = Person()
# p2.print_info("Анна", "Долгих")
# p2.add_skill(2)
#
#
# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def get_coord(self)
#         print(self.__dict__)
#
#
# p1 = Point(5, 10)
# p1.get_coord()
#
# p2 = Point(3, 7)
# p2.get_coord()
#
# p3 = Point(8, 16)
# p3.get_coord()
#
# print(p1.count)
# print(p2.count)
# print(p3.count)
#
# print(Point.count)
#
#
# class Robot:
#     k = 0
#
#
# def __init__(self, name):
#     self.name = name
#
#
# print("Инициализация робота:", self.name)
# Robot.k += 1
#
#
# def say_hi(self):
#     print(f"Приветствую! Меня зовут:", self.name)
#
#
# def __del__(self):
#     print(self.name, "выключается!")
#
#
# Robot.k -= 1
#
# if Robot.k == 0:
#     print(self.name, "был последним")
# else:
#     print("Работающих роботов осталось:", Robot.k)
#
# droid1 = Robot("R2-02")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid3 = Robot("ТО-Р30")
# droid3.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
#
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов:", Robot.k)
#
#
# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def say_hi(self):
#         print(f"Приветствую! Меня зовут:", self.name)
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
#
# print("Численность роботов:", Robot.k)

#
# 13.04.2024
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y  # _Point__y
#
#     def __check_value(s):  # _Point__check_value
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить новые значения
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координата X должны быть числами")
#
#     def get_coord(self):  # получаем значения
#         return self.__x, self.__y
#
#
# def set_x(self, x):
#     if Point.__check_value(y):
#         self.__y = y
#     else:
#         print("Координата Y должны быть числами")
#
#
# p1 = Point(5, "abc")
# print(p1.__dict__)
# # p1.set_coord(100, "abc")
# # p1.set_coord(100, 500.5)
# print(p1.get_coord())
# # # print(p1.__x, p1.__y)
# # # p1.__x = 100
# # # p1.__y = "abc"
# # # print(p1.__x, p1.__y)
# # print(p1.__dict__)
# # # print(Point.__check_value())
# # print(Point.__dict__)

#
# import math
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     def set_width(self, value):
#         if Rectangle.__check_value(value):
#             self.__width = value
#
#     def set_length(self, value):
#         if Rectangle.__check_value(value):
#             self.__length = value
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_perimeter(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(math.sqrt(self.__length ** 2 + self.__width ** 2), 2)

#     def draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# a = Rectangle(4, 12)
# a.set_length(3)
# a.set_width(9)
# print("Длинна прямоугольника", a.get_length())
# print("Щирина прямоугольника", a.get_width())
# print("Площадь прямоугольника", a.get_area())
# print("Периметр прямоугольника", a.get_perimeter())
# print("Гипотенуза прямоугольника", a.get_hypotenuse())
# a.draw()

#
# class Point:
#     __slots__ = "__x", "__y", "z"
#
#     def __init__(self, x, y, z):
#         self.__x = x
#         self.__y = y
#         self.z = z
#
#
# p1 = Point(5, 10)
# p1.z = 15
# print(p1.__dict__)
# print(p1.z)
#
#
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#         print("__set_x")
#
#     def __get_x(self):
#         print("__get_x")
#         return self.__x
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.x = 9
# print(p1.x)
# print(p1.__dict__)
#
#
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def __get_x(self):
#         print("__get_x")
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         self.__x = x
#         print("__set_x")
#
#
# p1 = Point(5, 10)
# p1.x = 9
# print(p1.x)
# print(p1.__dict__)
#
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числом")
#
#     def __check_value(s):
#         if isinstance(s, int) or isinstance(s, float):
#             return True
#         return False
#
#     # x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.x = 9
# # print(p1.x)
# print(p1.__dict__)
#
#
# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.deleter
#     def kg(self):
#         print("Удаление свойства")
#         del self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг =>", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг =>", end=" ")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 'десять'
# del weight.kg

#
# class Point:
#     __count__ = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point(5, 10)
# p2 = Point(5, 10)
# p3 = Point(5, 10)
#
# print(Point.get_count())
# print(p1.get_count())
#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def inc(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# 14.04.2024

# class Numbers:
#
#     @staticmethod
#     def max(a, b, c):
#         mx = a
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if b > mx:
#             mx = b
#         return mx
#
#
#
#
#
#     @staticmethod
#     def average(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         mul = 1
#         for i in range(1, n + 1):
#             mul *= i
#         return mul
#
#
# print("Максимальное число:", Numbers.max(3, 5, 7, 9))
# print("Минимальное число:", Numbers.min(3, 5, 7, 9))
# print("Среднее арифметическое:", Numbers.average(3, 5, 7, 9))
# print("Факториал числа:", Numbers.factorial(5))
#
#
# # 5! = 1 * 2 * 3 * 4 * 5
#
# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#

#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#
#     date = cls(day, month, year)
#     return date
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#
# dates = [
#     "23.10.2024",
#     "21/12/2023",
#     "01/01/2022",
#     "12/31/2021"
#
# ]
#
# for i in dates:
#     if Date.is_date_valid(i):
#         date = Date.from_string(i)
#         print(date.string_to_db())
#     else:
#         print(f"Неправильная дата или формат строки с датой")
#
# date1 = Date.from_string("23.10.2024")
# print(date1.string_to_db)
# date2 = Date.from_string("21.12.2023)
# print(date2.string_to_db)
#
# data = Date(23, 10, 2024)
# string_date = "23.10.2024"
# print(day, month, year)
# print(date.string_to_db())
#
# lass
# Account:
# rate_usd = 0.013
# rate_eur = 0.011
# suffix = 'RUB'
# suffix_usd = 'USD'
# suffix_eur = 'EUR'
#
#
# def __init__(self, surname, num, percent, value):
#     self.num = num
#     self.surname = surname
#     self.percent = percent
#     self.value = value
#     print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#     print("*" * 50)
#
#
# def __del__(self):
#     print(f"Остаток средств с текущего счета {self.value} был переведен на правопреемника")
#     self.value = 0
#     self.print_balance()
#     print("*" * 50)
#     print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#
# @classmethod
# def set_usd_rate(cls, rate):
#     cls.rate_usd = rate
#
#
# @classmethod
# def set_eur_rate(cls, rate):
#     cls.rate_eur = rate
#
# @staticmethod
# def convert(value, rate):
#     return value * rate
#
#
# def convert_to_usd(self):
#     usd_val = Account.convert(self.value, Account.rate_usd)
#     print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#
# def convert_to_eur(self):
#     eur_val = Account.convert(self.value, Account.rate_eur)
#     print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#
# def print_balance(self):
#     print(f"Текущий баланс {self.value} {Account.suffix}")
#
#
# def print_info(self):
#     print("Информация о счете:")
#     print("-" * 20)
#     print(f"#{self.num}")
#     print(f"Владелец: {self.surname}")
#     self.print_balance()
#     print(f"Проценты: {self.percent:.0%}")
#     print("-" * 20)
#
#
# def edit_owner(self, surname):
#     self.surname = surname
#
#
# def add_percents(self):
#     self.value += self.value * self.percent
#     print("Проценты были успешно начислены")
#     self.print_balance()
#
#
# def withdraw_money(self, val):
#     if val > self.value:
#         print(f"К сожалению, у вас нет {val} {Account.suffix}")
#     else:
#         self.value -= val
#         print(f"{val} {Account.suffix} было успешно снято!")
#     self.print_balance()
#
#
# def add_money(self, val):
#     self.value += val
#     print(f"{val} {Account.suffix} было успешно добавлено!")
#     self.print_balance()
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.__fio = fio
#         self.__old = old
#         self.__ps = ps
#         self.__weight = weight
#
# 20.04
# дописать
#
# if len(f) != 3:
#     raise TypeError("Неверный формат ФИО")
#     # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
# letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))  # Волков-ПетровИгорьНиколаевич
# # print(letters)
# for s in f:
#     if len(s.strip(letters)) != 0:
#         raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#
# @staticmethod
# def verify_old()
#     if not isinstance(old, int) or old < 14 or old > 120:
#         raise TypeError("Возраст должен быть числом в диапозоне от 14 до 120")
#
#
# @staticmethod
# def verify_weight(w):
#     if not isinstance(w, float) or w < 20:
#         raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#
# @staticmethod
# def verify_ps(ps):
#     if not isinstance(ps, str):
#         raise TypeError("Паспорт должен быть строкой")
#     s = ps.split()
#     print(s)
#     if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#         raise TypeError("Неверный формат паспорта")
#     for p in s:
#         if not p.isdigit():
#             raise TypeError("Серия и номер паспорта должны быть числами")
#
#
# @property
# def fio(self):
#     return self.__fio
#
#
# @fio.settr
# def fio(self, fio):
#     self.verity_fio(fio)
#     self.__fio = fio
#
#
# @property
# def old(self):
#     return self.__old
#
#
# @old.setter
# def old(self, year):
#     self.
#     self.__old = year
#
#
# @property
# def password(self):
#     return self.__password
#
#
# @password.setter
# def password(self, ps):
#     self.verify_ps(ps)
#     self.__password = ps
#
#
# @property
# def weight(self):
#     return self.__weight
#
#
# @weight.setter
# def weight(self, w):
#     self.verify_weight(w)
#     self.__weight = w
#
#
# p1 = UserData("Волков-Петров Игорь Николаевич", 26, "1234 567890", 80.8)
# p1.fio = "Соболев Игорь Николаевич"
# print(p1.fio)
# p1.old = 30
# p1.password = '0987 654321'
# p1.weight = 50.5
# print(p1.__dict__)
#
# НАСЛЕДОВАНИЕ
#
#
# class Point(self, x.y):  # class Point(object)
#     def __init__(self, x, y):
#         self.__x = x
#
#     self.__y = y
#
#
# print(issubclass(Point, list))
#
#
# class Point():
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")
#         Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self) -> None:
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color} {self.__width}")
#
#
# class Rect(Prop):
#     def draw_rect(self) -> None:
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 5)
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
#
# print(line._sp)
#
#
# class Fiqure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Fiqure):
#     def __init__(self, width, height, color):
#         self.__width = width
#         self.__height = height
#         super().__init__(color)
#
#     def area(self):
#         print(f"Прямоугольник {self.color}. Площадь: ", end="")
#         return self.__width * self.__height
# class Vector(list):

#
# rect = Rectangle(10, 20, "green")
# print(rect.area())


#
# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# v.append(4)
# print(v)
# print(type(v))
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"x = {self.x}, y = {self.y}"
#
#     def set_coord(self, x=None, y=None):
#         if y is None:
#             self.x = x
#         elif x is None:
#             self.y = y
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(10, 20)
# print(p1)
# p1.set_coord(1, 3)
# print(p1)
# p1.set_coord(5)
# print(p1)
# p1.set_coord(y=30)
# print(p1)
#
#
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImpLementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color} {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color} {self._width}")

#
# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self.width = self.length = width
#             else:
#                 self.width = width
#                 self.length = length
#         else:
#             self.radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть реализован метод calc_area()")
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = SqTable(20)
# print(t1.__dict__)
# print(t1.calc_area())
#
# t2 = RoundTable(radius=20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# from abc import ABC
#
#
# class Chess(ABC):  # абстрактный класс
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abctractmethod  # абстрактный метод
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на е2е4")
#
#
# q = Queen()
# q = draw()
# q = move()
#
# q = Chess()  # экземпляр абстрактного класса создать нельзя
#
# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     suffix = "RUB"
#
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#     def draw(self):
#         print(f"= {self.convert_to_rub():.2f} {Currency.suffix}")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
#
# print('*' * 30)
# for elem in d:
#     elem.print_value()
#     elem.draw()
#
# print('*' * 30)
# for elem in e:
#     elem.print_value()
#     elem.draw()
#
# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Display_1")
#
#
# class GrandChild(Child):
#     def def display2(self):
#
#     print("Display_2")
#
#
# gc = GrandChild()
# gc = display2()
# gc = display1()
#
# Вложеные
# классы
#
#
# def outer():
#     x = 5
#
#
# def inner():
#     y = 10
#     print(x)
#
#
# inner()
# print(y)
#
# outer()
#
#
# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_method():
#         print("outer_method")
#
#     def instance_method(self):
#         print("instance_method")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Метод во сложенном классе", MyOuter.age, self.obj.name)
#             MyOuter.outer_method()
#             self.obj.instance_method()
#
#
# out = MyOuter("внешний")
# inner = out.MyInner("внутренний", out)
# # inner = MyOuter.MyInner("внутренний")
# print(inner.inner_name)
# inner.inner_method()

#
# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = "Light Green"
#
#         def display(self):
#             print("Name:", self.name)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()

# 27.04.2024
# class Intern:
#     def __init__(self):
#         self.name = "Smith"
#         self.id = "657"
#
#     def show(self):
#         print("Name:", self.name)
#         print("Id:", self.id)
#         print("*" * 20)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Name:", self.name)
#         print("*" * 20)
#
#     class Head:
#         def __init__(self):
#             self.name = "Boss"
#             self.id = "789"
#
#         def show(self):
#             print("Name:", self.name)
#             print("Id:", self.id)
#             print("*" * 20)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# # d1 = Employee.Intern()
# # d2 = Employee.Head()
#
# d1.show()
# d2.show()
#
#
# class Point:
#     def __init__(self, *args):
#         self.__coord = args
#
#     def __len__(self):
#         return len(self.__coord)
#
#
# p = Point(5, 7)
# print(len(p))
# p1 = Point(4, 6, 8)
# print(len(p1))
#
#
# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(10, 20)
# print(p1.x, p1.y)
# p1.z = 30
# print(p1.z)
#
#
# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(10, 20)
# p2 = Poin2D(10, 20)
# print("pt1 = ", p1.__sizeof__())
# print("pt2 = ", p2.__sizeof__() + p2.__dict__.__sizeof__())
#
#
# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = ('z')
#
#
# pt = Point(1, 2)
# pt3 = Point3D(10, 20)
# pt.z = 30
# print(pt3.x, pt3.y, pt3.z)
#
# Множественное
# наследование
#
#
# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is slipping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking"))
#
#
#
#         dog = Dog("Buddy")
#         dog.bark()
#         dog.sleep()
#         dog.play()
#
#         удалила
#         классы
#         авс
#
#
# class Point:
#     def __inint__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# def __str__(self):
#     return f"({self.__x}, {self.__y})"
#
#
# class Styles:
#     def __inint__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         self._sp = sp
#         self._ep = ep
#         # Styles.__inint__(self, *args)
#         super().__inint__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
#
#
# # Миксины
#
# class Goods:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         MixinLog.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class Notebook(Goods, MixinLog):
#     pass
# 
#
# n = Notebook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()

# 28.04


# Число секунд в одном дне: 24 * 60 * 60 = 86400
#
# class Clock:
#     __DAY = 86400  # Число секунд в дне
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.sec % other.sec)
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# c3 = c1 + c2
# print(c3.get_format_time())
# c4 = Clock(300) + c3
# print(c4.get_format_time())
# c5 = c4 - c2
# print(c5.get_format_time())
# c6 = c5 * c2
# print(c6.get_format_time())
# c7 = c6 // c2
# print(c7.get_format_time())
# c8 = c7 % c2
# print(c8.get_format_time())

# c1 = Clock(80000)
# print(c1.get_format_time())
#
# print(c1["hour"], c1["min"], c1["sec"])
#
# rrom
# randon
# import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif:
#             self.pol == "F"
#         return f"{self.name} is good girl!!!"
#      else:
#      return f"{self.name} is good Kitty!!!"
#
#
# def __repr(self):
#     return f"Cat(name='{self.name}')"
#
#
# def __add__(self, outher):
#     if self.pol != outher.pol:
#         return [Cat("No name", 0, choice(['M', 'F'])) for in range(randint(1, 5))]
#
#     else:
#         raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Else", 5, "F")
# cat3 = Cat("Murzic", 3, "M")
# print(cat1)
# print(cat2)
# print(cat3)
#
#
#
# class Student:
#     def __init__(self, name, *args):
#         self.name = name
#         self.marks = list(args)  # [5, 5, 3, 4, 5]
#
#     def __getiten__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть цулым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 10 + 1 - 6 => 5
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть цулым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
# print(s1.marks)
#
# print([5, 5, 3, 4, 5].extend(ch))


# 4.05.

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimeter())
#
# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @abstractmethod
#     def info(self):
#         print(f"Меня зовут {self.name}. Мой возраст {self.age}.")
#
#     @abstractmethod
#     def make_sound(self):
#         ...
#
#
# class Cat(Animal):
#     def info(self):
#         print(f"Я кот.", end=" ")
#         super().info()
#
#     def make_sound(self):
#         print(f"{self.name} мяукает.")
#
#
# class Dog(Animal):
#     def info(self):
#         print(f"Я собака.", end=" ")
#         super().info()
#
#     def make_sound(self):
#         print(f"{self.name} гавкает.")
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
#
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()
#
#
# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"\n{self.surname} {self.name} {self.age}", end=" ")
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, speciality, group, rating):
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#         super().__init__(surname, name, age)
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, speciality, skill):
#         super().__init__(surname, name, age)
#         self.speciality = speciality
#         self.skilly = skill
#
#
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.skill}", end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, speciality, group, rating, topic):
#     self.topic = topic
#     super().__init__(surname, name, age, speciality, group, rating)
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end="")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()
#
#
# # Функторы
#
#
# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c1()
# c1()
#
#
# # функция
#
# def string_strip(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chaps)
#
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1(" Hello World!  "))
#
#
# # класс
#
# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, string):  # *args, **kwargs
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(self.__chars)
#
#
# s2 = StringStrip("?:!.; ")
# print(s2(" ? Hello World! ; "))
#
#
# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __cal__(self, *args, **kwargs):
#         print("-" * 40)
#         print("*args", args)
#         print("*kwargs", kwargs)
#         return self.func(*args, **kwargs))
#
#         @Power
#
#
# def mult(a, b):
#     return a * b
#
#
# @Power
# def mult(a, b, c):
#     return a * b * c
#
#
# print(mult(2, 3))
# print(mult1(2, 3, 4))
# print(mult1(2, c=3, b=4))


# def outer(arg):
#     def my_decorator(fn):
#         def wrap():
#             print(f"Перед вызовом функции, выведем {arg}")
#             fn()
#             print("После вызова функции")
#
#         return wrap
#
#     return my_decorator
#
#
# @outer("test")
# def func():
#     print("func")
#
#
# func()
#
#
# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, fn):
#         def wrap(a, b):
#             return fn(a, b) ** self.arg
#
#         return wrap
#
#
# @Power(5)
# def mult(a, b):
#     return a * b
#
#
# print(mult(2, 2))
#
# from abc import ABC, abstractmethod
#
#
# # Декорирование методов
#
#
# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))


# Дескриптор

# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         if isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#
#     @name.setter
#     def surname(self, value):
#         if isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__name = value

#
#     @property
#     def surname(self):
#         return self.__surname
#
#
#     @name.setter
#     def surname(self, value):
#         if isinstance(value, str):
#             raise TypeError(f"{value} должно быть строкой")
#         self.__surname = value


# class String:
#     def __init__(self, value):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f"{value} должны быть строкой")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.__name = String(name)
#         self.__surname = String(surname)
#
#
# p = Person(12, "Petrov")
# p.name.set("Petr")
# print(p.name.get())


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value,str):
#             raise ValueError(f"{self.__name}  должно быть строкой")
#         isinstance.__dict__[self.__name] = value
#
# class Person:
#     firs_name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, first_name, surname):
#         self.first_name = first_name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# p.surname = "Sidorov"
# print(p.first_name)
# print(p.surname)


# class Integer:
#     @staticmethod
#     def verify_coord(coord):
#         if not isinstance(coord, int):
#             raise ValueError(f"Координата {coord} должно быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.__name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.__name]
#         return getattr(instance, self.__name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.__name] = value
#         setattr(instance, self.__name, value)
#
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)

# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# MyList = type(
#      'MyList',
#      (list,),
#      dict(get_length=lambda self: len(self))
#
# )
#
#
# lst = MyList()
# lst.append(5)
# lst.append(7)
# lst.append(9)
# print(lst, lst.get_length())

# Создание модулей

# import math
# import random

# import geometry.rect
# import geometry.sq
# import geometry.trian
#
# r1 = geometry.rect.Rectangle(1, 2)
# r2 = geometry.rect.Rectangle(3, 4)
#
# s1 = geometry.sq.Square(10)
# s2 = geometry.sq.Square(20)
#
# t1 = geometry.trian.Triangle(1, 2, 3)
# t2 = geometry.trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimeter())


# from geometry import rect, sq, trian

# from geometry import *

#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimeter())
#
#
# if __name__ == '__main__':
#     run()


# from car import electrocar
# from car.electrocar import ElectroCar

# e_car = electrocar.ElectroCar ("Tesla", "T", 2018, 99000)
# e_car = ElectroCar ("Tesla", "T", 2018, 99000)
# e_car.show_car()
# e_car.description_battery()


# Упаковка данных(сериализация)
# Распаковка данных(десериализация)

# marshal (.рус)
# pickle
# json

# dump() сохраняет данные в открытый файл
# dumps()сохраняет данные в строку
#
# load() считывает данные из открытого файла
# loads()считывает данные из строки


# import pickle
#
# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "груши"],
#     "овощи": ("морковь",),
#     "бюджет": 1000
# }
#
# with open(file_name, "wb") as f:
#     pickle.dump(shop_list, f)
#
#
# with open(file_name, "rb") as f:
#     shop_list_2 = pickle.load(f)
#
#
# print(shop_list_2)
#
# import pickle
# class Test:
#     num = 35
#     string = "Привет"
#     lst = [1, 2, 3]
#     tpl = (25, 98)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.string}\nСписок: {Test.lst}\nКортеж{Test.tpl}"
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# new_obj = pickle.loads(my_obj)
# print(new_obj

#
# class Test2:
#     def __init__(self):
#         self.a = 35  # тип данных int
#         self.b = "test"  # тип данных str
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# # print(item1) # 35 test 4
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3)

# import json
#
# data = {
#     'name': 'Olga',
#     'age': 20,
#     20: None,
#     1: True,
#     False: 0,
#     'hobbies': ('running', 'singing'),
#     'children': {
#         'first_name': ['Alice', 'Bob'],
#         'age': [6, 12]
#     }
# }
#
# with open("data_file.json", "w") as f:
#     json.dump(data, f, indent=4)
#
#
# with open("data_file.json", "r") as f:
#     data2 = json.load(f)
#
# print(data2)

# json_string = json.dumps(data)
# print(json_string)
# print(type(json_string))
#
# data3 = json.loads(json_string)
# print(data3)
# print(type(data3))


# x = {"name": "Виктор"}
# a = json.dumps(x)
# print(a)
# b = json.dumps(x, ensure_ascii=False)
# print(b)
# print(json.loads(a))
#
# import json
# from random import choice
# 
# 
# def gen_person():
#     name = ''
#     tel = ''
# 
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# 
#     while len(name) != 7:
#         name += choice(letters)
# 
#     while len(tel) != 10:
#         tel += choice(nums)
# 
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
# 
# 
# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except (FileNotFoundError, json.JSONDecodeError):
#         data = {}
# 
#     data[len(data)+1] = person_dict
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
# 
# 
# for _ in range(5):
#     write_json(gen_person())

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
# def __str__(self):
#     st = ''
# for i in self.marks:
#     st += str(i) + ', '
# return f"{self.name}: {st[:-2]}"
#
#     def add_mark(self, new_mark):
#         self.marks.append(new_mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         return sum(self.marks) / len(self.marks)
#
#     def dump_to_json(self, file_name):
#         data = {"name": self.name, "marks": self.marks}
#         with open(file_name, "w") as f:
#             json.dump(data, f, indent=2)
#
#     def load_from_file(self, file_name):
#         with open(file_name, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         #     st = ''
#         #     for i in self.students:
#         #         st += str(i) + '\n'
#         st = "\n".join(map(str, self.students))
#         return f"Group: {self.group}\n{st}"

#     @staticmethod
#     def change_group(gr1, gr2, index):
#         return gr2.add_student(gr1.remove_student(index))
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     def dump_group(self, file_name):
#         with open(file_name, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             json.dump(stud_list, f, indent=2)
#
#     def jornal_groups(self, file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = []
#
#         with open(file_name, 'w') as f:
#             stud_list = []
#             for i in self.students:
#                 stud_list.append([i.name, i.marks])
#             data.append(stud_list)
#             json.dump(data, f, indent=2)
#
#     @staticmethod
#     def upload_group(file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# print(st1)
# st1.add_mark(4)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edit_mark(4, 5)
# print(st1)
# print(st1.average_mark())
# file = "student.json"
# st1.dump_to_json(file)
# st1.load_from_file(file)

# st2 = Student('Nikolaenko', [2, 3, 5, 4, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
# sts1 = [st1, st2]group1.remove_student(1)
# print(group1)
# group1 = Group(sts1, "GK Python")
# group1.add_student(st3)
# print(group1)

# print()
# sts2 = [st2]
# group2 = Group(sts2, "GK Web")
# print(group2)
# print("." * 20)
# Group.change_group(group1, group2, 0)
# print(group1)
# print()
# print(group2)
# file = "group1.json"
# group1.dump_group(file)
# group1.upload_group(file)
#
# file2 = "group2.json"
# group2.dump_group(file2)
# group2.upload_group(file2)

# files_group = "journal.json"
# group1.jornal_groups(files_group)
# group2.jornal_groups(files_group)
#

# import json
#
# data = {}
#
#
# class CountryCapital:
#     def __init__(self, country, capital):
#         self.country = country
#         self.capital = capital
#         data[self.country] = self.capital
#
#     def __str__(self):
#         return f"{self.country}: {self.capital}"
#
#     @staticmethod
#     def add_country(filename):
#         country_name = input("Введите страну: ")
#         capital_name = input("Введите столицу: ")
#
#         try:
#             date = json.load(open(filename))
#         except FileNotFoundError:
#             date = {}
#
#         date[country_name] = capital_name
#
#         with open(filename, "w") as f:
#             json.dump(date, f, indent=2)
#
#     @staticmethod
#     def delete_country(filename):
#         country_name = input("Введите страну для удаления: ")
#
#         try:
#             with open(filename, 'r') as f:
#                 date = json.load(f)
#         except FileNotFoundError:
#             return
#
#         if country_name in date:
#             del date[country_name]
#
#         with open(filename, 'w') as f:
#             json.dump(date, f, indent=2)
#
#     @staticmethod
#     def search_country(filename):
#         country_name = input("Введите страну для поиска: ")
#         try:
#             with open(filename, 'r') as f:
#                 date = json.load(f)
#                 capital = date.get(country_name)
#                 if capital:
#                     print(f"Столица {country_name}: {capital}")
#                 else:
#                     print(f"Страна {country_name} не найдена.")
#         except FileNotFoundError:
#             print("Файл не существует.")
#
#     @staticmethod
#     def edit_country(filename):
#         country_name = input("Введите страну для редактирования: ")
#
#         try:
#             with open(filename, 'r') as f:
#                 date = json.load(f)
#         except FileNotFoundError:
#             print("Файл не существует.")
#             return
#
#     @staticmethod
#     def load_from_file(filename):
#         with open(filename, "r") as f:
#             print(json.load(f))
#
#
# file = 'list_capital.json'
# index = ''
# while index != '6':
# index = input("Действие:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных\n"
#               "5 - просмотр данных\n6 - завершение работы\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     if index == "2":
#         CountryCapital.delete_country(file)
#     if index == "3":
#         CountryCapital.search_country(file)
#     if index == "4":
#         CountryCapital.edit_country(file)
#     if index == "5":
#         CountryCapital.load_from_file(file)


# 19.05
#
# установка
#
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(response.text)
# print(type(response.text))
# todos = json.loads(response.text)
# print(type(todos[0]))

# todos_by_user = {}
#
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             todos_by_user[todo["userId"]] = 1
#
# print(todos_by_user)
#
# top_user = sorted(todos_by_user.items(), key=lambda x: [1], reverse=True)
# print(top_user)
#
# max_complete = top_user[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_user:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
# # users = ["5"]
# max_users = " and ".join(users)
# s = "s" if len(users) > 1 else ""
# print(f"user {users} completed {max_complete} TODOs")
#
#
# def keep(tod):
#     is_completed = tod["completed"]
#     has_max_count = str(tod["userId"]) in users
#     return is_completed and has_max_count
#
#
# with open("filtered_data.json", "w") as f:
#     filtered = list(filter(keep, todos))
#
#     json.dump(filtered, f, indent=2)
#

# import csv

# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Год рождения {row[2]}")
#     count += 1

# with open("data.csv") as f:
#     field_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=field_names)
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Год рождения {row['Год рождения']}")
#         count += 1
#
# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])
#
# with open("student1.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 15})
#     writer.writerow({"Имя": "Вова", "Возраст": 14})
#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open("dict_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\n", fieldnames=data[0].keys())
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)
#
#
# print(list(data[0].keys()))

# from bs4 import BeautifulSoup
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", class_="row")
# row = soup.find("div", {class: "row"})
# row = soup.find_all("div", class_="row")[1].find("div", class_="name").text
# row = soup.find_all("div", {"data-set": "salary"})
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

#
# from bs4 import BeautifulSoup
#
#
# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois").text
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
#
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
#
# print(copywriter)

# from bs4 import BeautifulSoup
# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# salary = soup.find_all("div", {"data-set": "salary"})
# print(salary)
# for i in salary:
#     get_salary(i.text)


# import requests
#
#
# r = requests.get("https://ru.wordpress.org/")
# print(r)
# print(r.status_code)
# print(r.headers)
# print(r.content)
# print(r.text)

# import csv
#
# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open("plugins.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("div", class_="entry")
#
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         url = plugin.find("h3").find("a").get("href")
#         rating = plugin.find("span", class_="rating-count").text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     (get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# import csv
#
# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def write_csv(data):
#     with open("market_data.csv", "a") as f:
#         writer = csv.writer(f, lineterminator="\r", delimiter=";")
#         writer.writerow((data['name'], data['url'], data['price']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "html.parser")
#     products = soup.find_all("div", class_="catalog_element")
#
#     for product in products:
#         name = product.find("div", class_="catalog_title").text
#         url = product.find("a", class_="link catalog_image_link").get("href")
#         price = product.find("span", class_="catalog_price").text
#         refined_price = refined(price)
#         data = {'name': name, 'url': url, 'price': refined_price}
#         write_csv(data)
#
#
# def main():
#     url = "https://market-kirov.ru/"
#     (get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

#
# import csv
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def main():
#     for i in range(2, 3):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['active'], data['cy']))
#
#

# import csv
#
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("div", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3", class_="entry-title").text
#         except AttributeError:
#             name = ""
#
#         try:
#             url = el.find("h3", class_="entry-title").find('a')["href"]
#         except AttributeError:
#             url = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except AttributeError:
#             active = ""
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except AttributeError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# if __name__ == '__main__':
#     main()

# from parsers import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()
# import csv

#
# import requests
# from bs4 import BeautifulSoup
#
#
# def main():
#     for i in range(2, 3):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("div", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3", class_="entry-title").text
#         except AttributeError:
#             name = ""
#
#         try:
#             url = el.find("h3", class_="entry-title").find('a')["href"]
#         except AttributeError:
#             url = ""
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except AttributeError:
#             active = ""
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except AttributeError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# if __name__ == '__main__':
#     main()
#
#
#
# class Parser:
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         print(req)
#

#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt"):
#     pars.get_html = BeautifulSoup(reg, "lxml")
#
#
# def parsing(self):
#     news = self.html.find_all("div", class_="caption")
#     for item in news:
#         title = item.find('h3').text
#         href = item.find('a').get('href')
#         author = item.find("a", class_="topic-info-author-link").text.strip()
#         self.res.append({
#             "title": title,
#             "href": href,
#             "author": author,
#         })
#     print(self.res)
#
#
# def save(self):
#     with open(self.path, "w") as f:
#         i = 1
#         for item in self.res:
#             f.write(f"Новость № {i}\n\nНазвание: {item['title']}\nСсылка: {item['href']}\nАвтор: "
#                     f"{item['author']}\n\n{'*' * 40}\n")
#             i += 1
#
#
# def run(self):
#     self.get_html()
#     self.parsing()
#     self.save()
#

#
# class Controller:
#     def __init__(self):
#         self.article_model = None
#         self.user_interface = None
#
#     def run(self):
#         answer = None
#         while anwer != "q":
#             answer = self.user_
#
#
# from controller import Controller
#
#
# def main():
#     app = Controller()
#     app.run()
#
#
# if __name__ == '__main__':
#     main()
#
#
# class UserUnterface:
#     def wait_user_answer(self):
#         print("Ввод пользовательских данных ".center(50, "="))
#         print("Действия со статьями:")
#         print("q - выход из программы ")
#         user_answer = input("Выберите вариант действия: ")
#         print("=" * 50)
#         return user_answer

# import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# cur.execute("""
# """)
#
# con.close()


# with sqlite3.connect("profile.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE users(
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        name TEXT NOT NULL,
#        summa REAL,
#        date BLOB)""")




