"""
Создать функцию, которая создает таблицу user.
Запустить функцию и проверить наличие таблицы.
"""


from sqlalchemy import create_engine,  Integer, String, Column
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    email = Column(String)
    age = Column(Integer)


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

    # Создание объектов пользователей и добавление их в сессию
    for index in range(5):
        user = User(name=f"user-{index}", email=f"user-{index}@email.com", age=index+20)
        session.add(user)

    # Отправка данных в БД
    session.commit()

    # Поиск пользователя по имени
    user = session.query(User).filter(User.name == "user-1").first()
    print(f"Search by name, found used #{user.id}")

    # Поиск пользователей по возрасту
    users = session.query(User).filter(User.age >= 21, User.age < 23).all()
    for user in users:
        print(f"Search by age, found user #{user.id}")
