"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""


import sqlite3 as sql
from hashlib import sha256

con = sql.connect('lesson_3.sqlite')

with con:

    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS "hash"("password" STRING, "hash" STRING)')
    con.commit()


def write_to_db(password, hash):

    with con:
        cur = con.cursor()
        cur.execute('SELECT password FROM "hash"')
        res = [x[0] for x in cur.fetchall()]
        if password not in res:
            cur.execute(f'INSERT into "hash" VALUES ("{password}", "{hash}")')


def get_hash_db(password):

    with con:
        cur = con.cursor()
        cur.execute(f""" SELECT hash FROM 'hash' WHERE password="{password}" """)
        res = cur.fetchall()
        return res[0][0]


def create_hash(password: str):

    salt = "simple_salt"
    hash_obj = sha256(password.encode() + salt.encode())
    res = hash_obj.hexdigest()

