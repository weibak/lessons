"""
Создать класс Point, описывающий точку (атрибуты: x, y).
Создать класс Figure. Создать три дочерних класса Circle
(атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра), Square
(атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""


class Point:

    def __init__(self, coordinate_x: int, coordinate_y: int):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y


class Figure(Point):

    def figure(self, coordinate_y, coordinate_x, coordinate_z):
        super().__init__(coordinate_x, coordinate_y)
        self.coordinate_z = coordinate_z
#def __str__(self):
    #return (f" Perim: {self.perim}, Area: {self.area}")


class Circle(Figure):

    #def __str__(self):
        #return (f" Perim: {self.perim}, Area: {self.area}")
    def circle(self, center, radius, coordinate_x, coordinate_y):
        super().__init__(coordinate_x, coordinate_y)
        self.center = center
        self.radius = radius

    def perim(self):
        perim_circle = 2 * 3.14 * self.radius
        return perim_circle

    def area(self):
        area_circle = 2 * 3.14 * (self.radius ** 2)
        return area_circle

    #def __str__(self):
        #return (f" Perim: {self.perim}, Area: {self.area}")


class Triangle(Figure):

    #def __str__(self):
        #return (f" Perim: {self.perim}, Area: {self.area}")

    def triangle(self, stor_1: int, stor_2: int, stor_3: int, coordinate_x, coordinate_y):
        super().__init__(coordinate_x, coordinate_y)
        self.stor_1 = stor_1
        self.stor_2 = stor_2
        self.stor_3 = stor_3

    def perim(self):
        perim_triangle = (self.stor_1 + self.stor_2 + self.stor_3) / 2
        print(perim_triangle)

    def area(self):
        p = (self.stor_1 + self.stor_2 + self.stor_3) / 2
        geron = (p * (p - self.stor_1) * (p - self.stor_2) * (p - self.stor_3)) ** 0.5
        print(geron)

    #def __str__(self):
        #return (f" Perim: {self.perim}, Area: {self.area}")

class Square(Figure):

    #def __str__(self):
        #return (f" Perim: {self.perim}, Area: {self.area}")

    def squre(self, stor_square_1: int, stor_square_2: int, coordinate_x, coordinate_y):
        super().__init__(coordinate_x, coordinate_y)
        self.stor_square_1 = stor_square_1
        self.stor_square_2 = stor_square_2

    def perim(self):
        perim_square = self.stor_square_1 + self.stor_square_2
        print(perim_square)

    def area(self):
        area_square = self.stor_square_1 * self.stor_square_2
        print(area_square)

    #def __str__(self):
        #return (f" Perim: {self.perim}, Area: {self.area}")


if __name__ == "__main__":
    circle = Circle(7, 5)

    square = Square(19, 20)


    circle.perim()
    print(circle)
    print(triangle)
    print(square)