"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. Унаследовать
Dog и Cat от класса Animal и Удалить в дочерних классах те методы, которые имеются у
родительского класса. Создать объект каждого класса и вызвать все его методы.
"""


class Animal:
    # свойства, атрибуты
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
    # методы
    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"Run {self.name}")


class Dog(Animal):
    #методы
    def bark(self):
        print(f"Bark {self.name}")


class Cat(Animal):
    def meow(self):
        print(f"Meow {self.name}")


if __name__ == "__main__":
    cat = Cat(50, 6, "Andy", 4)
    dog = Dog(70, 15, "Arni", 5)
    print(cat.name)
    print(cat.height)
    print(cat.weight)
    print(cat.age)
    print("-----------")
    cat.run()
    cat.jump()
    cat.meow()
    print("-----------")
    print(dog.name)
    print(dog.height)
    print(dog.weight)
    print(dog.age)
    print("-----------")
    dog.run()
    dog.jump()
    dog.bark()