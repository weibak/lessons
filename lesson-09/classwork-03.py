"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод
bark на meow.
"""


class Cat:
    #свойства, атрибуты
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
    #методы
    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"Run {self.name}")

    def meow(self):
        print(f"Meow {self.name}")


if __name__ == "__main__":
    cat = Cat(100, 100, "BobCat", 10)
    cat.meow()