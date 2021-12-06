"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода:
jump, run, bark. Каждый метод выводит сообщение на экран. Создать объект класса Dog,
вызвать все методы объекта и вывести на экран все его свойства.
"""


class Dog:
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

    def bark(self):
        print(f"Bark {self.name}")


if __name__ == "__main__":
    dog = Dog(100, 100, "Bob", 10)
    dog.jump()
    dog.run()
    dog.bark()
    #атрибуты. свойства
    print(dog.name)
    print(dog.height)
    print(dog.weight)
    print(dog.age)

