def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title} ".center(50, "="))
            choice = func(*args, **kwargs)
            print("=" * 50)
            return choice
        return wrap
    return wrapper


class UserFilm:

    @add_title("Редактирование данных каталога фильмов ")
    def reg_user_uber(self):
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_uber = input("Выберите вариант действия: ")
        return user_uber

    @add_title(" Создание фильма ")
    def add_user_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссера": None,
            "год": None,
            "длительность": None,
            "студию": None,
            "актеров": None
        }
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
        return dict_film

    @add_title(" Каталог фильмов ")
    def show_all_films(self, films):
        for ind, film in enumerate(films, 1):
            print(f"{ind}. {film}")

    @add_title("Ввод названия фильма")
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_title("Просмотр фильма")
    def show_ping_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @add_title("Сообщение об ошибке")
    def show_correct_film(self, title_film):
        print(f"Фильма с названием {title_film} не существует")

    @add_title("Удаление статьи")
    def answer_ping_film(self, film):
        print(f"Фильм {film} - был удален")

    @add_title("Сообщение об ошибке")
    def dump_show_incorrect(self, uber):
        print(f"Варианта {uber} не существует")

