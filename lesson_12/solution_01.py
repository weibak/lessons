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


def create_purchase(choice, quan, email):
    q = session.query(User.id, User.email).all()
    e = email

    def get_key(q, value):
        for k, v in q:
            if v == value:
                return k

    user_id = get_key(q, e)
    purchase = Purchase(id_usr=user_id, id_prod=choice, quantity=quan)
    session.add(purchase)
    # Отправка данных в БД
    session.commit()
    return print("You by this product!")


""" еще одна попытка из миллиона
    #for u in q: #A цикл для вычисленяи айди равный почте
        #b = {u.email: u.id} # словарь для нахождения айди, через ключ-значение
        #print(b)

        #user_id = b.get(e)
        #print(user_id)
        #result = user_id
        #return print(result)
    #print(user_id)
    одна из миллиона попыток вынять фйди юзера
    usrid = (user.id, user.email)
    print(usremail, usrid)
    mail = input("Email: ")
    iddd = user.id[0]
    user_id = session.query(User).filter(User.id == email)"""


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

    email = input("Insert your email: ")
    user = session.query(User.email).filter(User.email == email).first()
    users = session.query(User.email).all()
    print(user)
    for email in user:
        if email == user.email:
            print(email)
            qus = input("You want to buy or add product?(Buy/Add) ")
            if qus == "Buy":
                prod = session.query(Product.id, Product.name, Product.price)
                prods = prod.all()
                for product in prods:
                    print(
                        f"Product number: {product[0]}, product name: {product[1]}, product price: {product[2]}"
                    )
                choice = int(input("Enter number of product, what you want buy: "))
                quan = int(input("Enter how many pieces you want to buy:  "))
                # user_id = session.query(User.id).one()
                # email = input("email: ")
                create_purchase(choice, quan, email)
                # buy = Purchase(id_usr=user.id, id_prod=choice, quantity=quan)
            if qus == "Add":
                prod = input("Enter name of product: ")
                price = int(input("Enter price of product: "))
                create_product(prod, price)
                break
        if email not in users:
            qus2 = input("Do you wont to register? (Yes/No) ")
            if qus2 == "Yes":
                name_usr = input("Enter your name: ")
                email = input("Enter your email: ")
                create_user(name_usr, email)
                break
            if qus2 == "No":
                break
            else:
                break

"""
        if email != user:
            qus2 = input("Do you wont to register? (Yes/NO) ")
            if qus2 == "Yes":
                name_usr = input("Enter your name: ")
                email = input("Enter your email: ")
                create_user(name_usr, email)

            if qus2 == "No":
                continue
"""



# name_prod = input("Insert product Name: ")
# price = int(input("Insert price of product: "))
#create_user("aaaa", "@com")
# create_product(name_prod, price)


