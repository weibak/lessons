"""
Создать функцию, которая создает таблицу user, для примера использовать слайд №12.
Запустить функцию и проверить, что создался файл базы данных.
"""

import sqlite3


def create_user_table():
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname VARCHAR,
                lastname VARCHAR,
                email VARCHAR,
                password VARCHAR,
                age INTEGER,
                datetime DATETIME
            );
            """,
        )
        session.commit()



def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
   with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()


def search_user(query: str):
   with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT firstname, lastname, age 
            FROM user 
            WHERE firstname = ?;
            """,
            (query,), #запятая специально, чтобы показать что один элемент
        )
        session.commit()
        return cursor.fetchall()


def search_user_age(from1: int, to: int):
   with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT firstname, lastname, age 
            FROM user 
            WHERE (age >= ? and age <= ?);
            """,
            (from1, to)
        )
        session.commit()
        return cursor.fetchall()


if __name__ == "__main__":
    """create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass", 36)
    create_user("ARTEM", "Sheibak", "sheibakaa@gmail.com", "TestPass1", 22)
    create_user("Evgesha", "Eidelman", "eidelman@gmail.com", "TestPass2", 25)
    create_user("Anastasia", "Pris", "nastya@gmail.com", "TestPass3", 36)
    create_user("Mark", "Kalinin", "kalinin@gmail.com", "TestPass4", 18)"""
    print(search_user("ARTEM"))
    print(search_user("Anastasia"))
    print(search_user_age(17, 23))