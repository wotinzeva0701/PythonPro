from flask import Flask, render_template, request, flash, g
import sqlite3
import os
from FDataBase import FDataBase

DEBUG = True
SECRET_KEY = '11e528675ac949d1ce378ef8e00ba20e3c261aaf'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbbase = FDataBase(db)
    return render_template('index.html',
                           menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html',
                           title="Страница не найдена", menu=[])


if __name__ == '__main__':
    app.run()
