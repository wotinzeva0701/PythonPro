
class PositiveValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value <= 0:
            print(f"Ошибка: {self.name} должно быть положительным числом.")
        else:
            instance.__dict__[self.name] = value


class Order:
    price = PositiveValue()
    quantity = PositiveValue()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


order = Order('apple', 5, 10)
# print("Order('apple', 5, 10)")
print(order.total_price())
