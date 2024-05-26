import json

data = {}


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f"{self.country}: {self.capital}"

    @staticmethod
    def add_country(filename):
        country_name = input("Введите страну: ")
        capital_name = input("Введите столицу: ")

        try:
            date = json.load(open(filename))
        except FileNotFoundError:
            date = {}

        date[country_name] = capital_name

        with open(filename, "w") as f:
            json.dump(date, f, indent=2)

    @staticmethod
    def delete_country(filename):
        country_name = input("Введите страну для удаления: ")

        try:
            with open(filename, 'r') as f:
                date = json.load(f)
        except FileNotFoundError:
            return

        if country_name in date:
            del date[country_name]

        with open(filename, 'w') as f:
            json.dump(date, f, indent=2)

    @staticmethod
    def search_country(filename):
        country_name = input("Введите страну для поиска: ")
        try:
            with open(filename, 'r') as f:
                date = json.load(f)
                capital = date.get(country_name)
                if capital:
                    print(f"Столица {country_name}: {capital}")
        except FileNotFoundError:
            print("Файл не существует.")

    @staticmethod
    def edit_country(filename):
        country_name = input("Введите страну для редактирования: ")

        try:
            with open(filename, 'r') as f:
                date = json.load(f)
        except FileNotFoundError:
            print("Файл не существует.")
            return

        if country_name in data:
            capital_name = input(f"Текущая столица для {country_name}: {data[country_name]}\nВведите новую столицу: ")
            data[country_name] = capital_name
            with open(filename, 'w') as f:
                json.dump(date, f, indent=2)
            print(f"Страна {country_name} не найдена.")

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as f:
            print(json.load(f))


file = 'list_capital.json'
index = ''
while index != '6':
    index = input("Действие:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование данных\n"
                  "5 - просмотр данных\n6 - завершение работы\nВвод: ")
    if index == "1":
        CountryCapital.add_country(file)
    if index == "2":
        CountryCapital.delete_country(file)
    if index == "3":
        CountryCapital.search_country(file)
    if index == "4":
        CountryCapital.edit_country(file)
    if index == "5":
        CountryCapital.load_from_file(file)
