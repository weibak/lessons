"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорость (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задний ход (изменение
знака скорости).
"""


class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speed(self):
        self.speed += 5
        print(f"Increased speed: {self.speed}")

    def decrease_speed(self):
        self.speed -= 5
        print(f"Decreased speed: {self.speed}")

    def stop_speed(self):
        self.speed = 0
        print(f"Speed: {self.speed}")

    def show_speed(self):
        print(f"Your speed: {self.speed}")

    def reverse_speed(self):
        self.speed = -self.speed
        print(f"Reverse speed: {self.speed}")


if __name__ == "__main__":
    car = Car("Mersedes", "S500", 2000, 0)
    print(car.speed)
    print(car.brand)
    print(car.model)
    print(car.year)
    car.increase_speed()
    car.reverse_speed()
    car.stop_speed()