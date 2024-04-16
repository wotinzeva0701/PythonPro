import math


class Calculator:
    count = 0

    @staticmethod
    def count_triangle(a, b, c):
        Calculator.count += 1
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def count_sides(y, z):
        Calculator.count += 1
        p = (y * z) / 2
        return p

    @staticmethod
    def count_rectangle(length, width):
        Calculator.count += 1
        return length * width

    @staticmethod
    def count_square(x):
        Calculator.count += 1
        return x ** 2

    @staticmethod
    def get_count():
        return Calculator.count


print("Площадь треугольника по формуле Герона:", Calculator.count_triangle(3, 4, 5))
print("Площадь треугольника через основание и высоту:", Calculator.count_sides(6, 7))
print("Площадь квадрата:", Calculator.count_square(7))
print("Площадь прямоугольника:", Calculator.count_rectangle(2, 6))
print("Количество подсчетов площади:", Calculator.get_count())
