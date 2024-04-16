class Person:
    def __init__(self, name, year):
        self.__name = name
        self.__year = year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @year.deleter
    def year(self):
        del self.__year


person = Person("Irina", 26)
print(person.name)
print(person.year)
person.name = "Igor"
person.year = 31
print(person.name)
print(person.year)
del person.name
