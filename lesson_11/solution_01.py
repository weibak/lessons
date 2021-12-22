"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию и
вводить необходимые данные.
"""


import sqlite3


def create_products_table():
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                price INTEGER,
                count INTEGER,
                comment VARCHAR
            );
            """,
        )
        session.commit()


def create_product(name: str, price: int, count: int, comment: str):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO products (name, price, count, comment)
            VALUES (?, ?, ?, ?);
            """,
            (name, price, count, comment),
        )
        session.commit()


def search_product(query: str):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT name, price, count 
            FROM products 
            WHERE name = ?;
            """,
            (query,),
        )
        session.commit()
        return cursor.fetchall()


def search_product_price(from1: int, to: int):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT name, price, count 
            FROM products 
            WHERE (price >= ? and price <= ?);
            """,
            (from1, to)
        )
        session.commit()
        return cursor.fetchall()


def update_product(id: int, name: str):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE products
            SET name = ?
            WHERE id = ?;
            """,
            (name, id)
        )
        session.commit()


def delete_product(query: str):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM products
            WHERE comment = ?;
            """,
            (query,),
        )
        session.commit()

if __name__ == "__main__":
    #create_products_table()
    #create_product("Milk", 2, 5, "I need More Milk")
    #create_product("Popcorn", 1, 3, "For my Party")
    #create_product("Cheese", 5, 2, "Say: cheese")
    #create_product("IPhone", 1000, 1, "Expensive gift")
    #create_product("IPhone13", 1, 2000, "Don't Need")
    #print(search_product(input("Which name of product you do you want to find: ")))
    #from1, to = [int(x) for x in input("Enter price from and to: ").split()]
    #print(search_product_price(from1, to))
    #update_product(3, "Milk replace cheese")
    #delete_product("Don't Need")

    choise = input("What operation do you want to do: ")
    if choise == "create":
        name = input("Insert name of product: ")
        price = int(input("Insert price of product: "))
        count = int(input("Insert quantity of product: "))
        comment = input("Insert your product comment: ")
        create_product(name, price, count, comment)
        print("Product created")
    elif choise == "search":
        name = input("Insert name of product: ")
        print(search_product(name))
    elif choise == "search(price)":
        from1 = int(input("Search price from: "))
        to = int(input("Search price to: "))
        print(search_product_price(from1, to))
    elif choise == "update":
        id = int(input("Insert your ID: "))
        comment = input("What name you want to update: ")
        update_product(id, comment)
        print("Well done update!")
    elif choise == "delete":
        query = input("Product with which comment would you like to delete: ")
        delete_product(query)
        print("Product removed")
    else:
        print("Something wrong!")
