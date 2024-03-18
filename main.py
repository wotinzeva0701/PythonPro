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

