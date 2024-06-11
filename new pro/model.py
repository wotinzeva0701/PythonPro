import pickle
import os.path


class Film:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title}({self.genre})"


class FilmModel:
    def __init__(self):
        self.aw_name = "aw.txt"
        self.films = self.load_data()

    def add_films(self, dict_films):
        film = Film(*dict_films.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_ping_film(self, user_title):
        film = self.films[user_title]
        dict_film = {
            "название": film.title,
            "жанр": film.genre,
            "режиссера": film.director,
            "год": film.year,
            "длительность": film.duration,
            "студию": film.studio,
            "актеров": film.actors
        }
        return dict_film

    def answer_film(self, user_film):
        return self.films.pop(user_film)

    def save_data(self):
        with open(self.aw_name, "wb") as f:
            pickle.dump(self.films, f)

    def load_data(self):
        if os.path.exists(self.aw_name):
            with open(self.aw_name,"rb") as f:
                return pickle.load(f)
        else:
            return dict()