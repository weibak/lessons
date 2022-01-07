"""
Создать модель пользователя, атрибуты - id, email и
модель товара, атрибуты - id, название, цена.
Создать модель покупок, атрибуты - id, ссылка на пользователя (Foreign key),
ссылка на товар (Foreign key), количество и дата покупки.
Добавить функции создания пользователя, товара и покупки.
Добавить функцию вывода всех товаров, купленных определенным пользователем.
Создать программу с пользовательским интерфейсом позволяющим выбирать определенную
функцию и вводить необходимые данные.
"""
from datetime import datetime

from sqlalchemy import create_engine, DateTime, ForeignKey, Integer, String, Column
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


# Настройки доступа к БД
DB_USER = "weibak"
DB_PASSWORD = "weibak"
DB_NAME = "weibak"
DB_ECHO = True


# Базовый класс для работы с БД
Base = declarative_base()


# Класс/модель описывающий пользователя
# Если в модель вносятся изменения,
# необходимо удалить старую таблицу в БД
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user = relationship("Purchase", backref="user")
    email = Column(String)


# Класс/модель описывающий товар
# Если в модель вносятся изменения,
# необходимо удалить старую таблицу в БД
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    product = relationship("Purchase", backref="product")
    price = Column(Integer)


# Класс/модель описывающий покупку
# Если в модель вносятся изменения,
# необходимо удалить старую таблицу в БД
class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    id_usr = Column(Integer, ForeignKey("user.id"), nullable=False)
    price = Column(Integer)
    id_prod = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer)
    date_of_purchase = Column(DateTime(), default=datetime.now())


def create_user(name_usr: str, email: str):
    # Создание объектов пользователей и добавление их в сессию
    user = User(name=name_usr, email=email)
    session.add(user)

    # Отправка данных в БД
    session.commit()
    return print("User successfully added!")


def create_product(name_prod: str, price: int):
    # Создание объектов товаров и добавление их в сессию
    products = Product(name=name_prod, price=price)
    session.add(products)
    # Отправка данных в БД
    session.commit()
    return print("Product successfully added!")


def create_purchase(name_prod, ):
    # Создание объектов покупок и добавление их в сессию
    print()
    by = input("What product you want to by? ")

    purchase = Purchase(id_usr=name_usr)
    user_name = Column(String, ForeignKey("user.name"))
    user = relationship("User", back_populates="purchases")
    price = Column(Integer)
    product_name = Column(String, ForeignKey("products.name"))
    product = relationship("Product", back_populates="purchases")
    quantity = Column(Integer)
    date_of_purchase = Column(DateTime, default=datetime.date)
    products = Product(name=name_prod, price=price)
    session.add(purchase)

    # Отправка данных в БД
    session.commit()


if __name__ == "__main__":
    # Создание подключения к БД
    engine = create_engine(
       f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    # Проверка существования БД
    if not database_exists(engine.url):
        # Создание БД
        create_database(engine.url)

    # Создание таблиц в БД для всех классов/моделей
    Base.metadata.create_all(engine)
    # Создание новой сессии для добавления/удаления записей
    Session = sessionmaker(bind=engine)
    session = Session()


#name_usr = input("Insert your Name: ")
#email = input("Insert your email: ")
#name_prod = input("Insert product Name: ")
#price = int(input("Insert price of product: "))
#create_user(name_usr, email)
#create_product(name_prod, price)


