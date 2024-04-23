class Student:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop

    def show_info(self):
        print(f"{self.name} {self.laptop.model} {self.laptop.processor} {self.laptop.memory}")


class Laptop:
    def __init__(self, model, processor, memory):
        self.model = model
        self.processor = processor
        self.memory = memory


Roman_laptop = Laptop("HP", "i7", 16)
Vladimir_laptop = Laptop("HP", "i7", 16)

Roman = Student("Roman", Roman_laptop)
Vladimir = Student("Vladimir", Vladimir_laptop)

Roman.show_info()
Vladimir.show_info()
