
class Avto:
    def __init__(self, model, year, manufacture, power, color, price):
        self.model = model
        self.year = year
        self.manufacture = manufacture
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print("Данные автомобиля".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacture}\nМощность двигателя: {self.power}\nЦвет: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacture(self, manufacture):
        self.manufacture = manufacture

    def get_manufacture(self):
        return self.manufacture

    def set_power(self, power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


h1 = Avto("X7 M50i", 2021, "BMW", "530 л.с", "white", 10790000)
h1.print_info()
