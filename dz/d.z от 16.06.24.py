import sqlite3

users = [
    ('Алиса', 25),
    ('Павел', 30),
    ('Алена', 35),
    ('Петр', 45),
    ('Василий', 65),
    ('Максим', 15),
    ('Владимир', 25),
    ('Наталья', 5),
]

with sqlite3.connect('example.db') as con:
    cur = con.cursor()
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS users(
            users_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
     """)


cur.executemany("INSERT INTO users VALUES(NULL, ?, ?)", users)


