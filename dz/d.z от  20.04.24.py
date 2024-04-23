class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w >= 0:
            self.__width = w
        else:
            self.width = 0
            print("Ширина не может быть отрицательной.")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h >= 0:
            self.__height = h
        else:
            self.height = 0
            print("Высота не может быть отрицательной.")

    def area(self):
        print(f"Прямоугольник {self.color}. Площадь: ", end="")
        return self.__width * self.__height


rect = Rectangle(10, 20, "green")
print(rect.area())
