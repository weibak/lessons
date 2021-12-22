"""
Создать функцию, которая создает таблицу user.
Запустить функцию и проверить наличие таблицы.
"""


from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.orm import sessionmaker

DB_USER = "weibak"
DB_PASSWORD = "weibak"
DB_NAME = "weibak"
DB_ECHO = True

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)


if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    if not database_exists(engine.url):
        create_database(engine.url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(email="sheibakaa@gmail.com")
    session.add(user)
    session.commit()



