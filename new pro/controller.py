from view import UserFilm
from model import FilmModel


class Controller:
    def __init__(self):
        self.film_model = FilmModel()
        self.user_film = UserFilm()

    def run(self):
        uber = None
        while uber != "q":
            uber = self.user_film.reg_user_uber()
            self.check_user_uber(uber)

    def check_user_uber(self, uber):
        if uber == "1":
            film = self.user_film.add_user_film()
            self.film_model.add_films(film)
        elif uber == "2":
            film = self.film_model.get_all_films()
            self.user_film.show_all_films(film)
        elif uber == "3":
            film_title = self.user_film.get_user_film()
            try:
                film = self.film_model.get_ping_film(film_title)
            except KeyError:
                self.user_film.show_correct_film(film_title)
            else:
                self.user_film.show_ping_film(film)
        elif uber == "4":
            film_title = self.user_film.get_user_film()
            try:
                film = self.film_model.answer_film(film_title)
            except KeyError:
                self.user_film.show_correct_film(film_title)
            else:
                self.user_film.answer_ping_film(film)
        elif uber == 'q':
            self.film_model.save_data()
        else:
            self.user_film.dump_show_incorrect(uber)



