"""
Создать класс Point, описывающий точку (атрибуты: x, y).
Создать класс Figure. Создать три дочерних класса Circle
(атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра), Square
(атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""

"""
class Point:

    def __init__(self, coordinate_x: int, coordinate_y: int):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y


class Figure(Point):

    def figure(self, coordinate_y, coordinate_x, coordinate_z):
        super().__init__(coordinate_x = coordinate_x, coordinate_y= coordinate_y)
        self.coordinate_z = coordinate_z



class Circle(Figure):

    def __str__(self):
        return (f"Area: {self.area}, perim: {self.perim}")

    def circle(self, center, radius, coordinate_x, coordinate_y):
        super().__init__(coordinate_x=coordinate_x, coordinate_y=coordinate_y)
        self.center = center
        self.radius = radius

    def perim(self):
        perim_circle = 2 * 3.14 * self.radius
        print(perim_circle)

    def area(self):
        area_circle = 2 * 3.14 * (self.radius ** 2)
        print(area_circle)



class Triangle(Figure):


    def triangle(self, stor_1: int, stor_2: int, stor_3: int, coordinate_x, coordinate_y):
        super().__init__(coordinate_x = coordinate_x, coordinate_y = coordinate_y)
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



class Square(Figure):


    def squre(self, stor_square_1: int, stor_square_2: int, coordinate_x, coordinate_y):
        super().__init__(coordinate_x=coordinate_x, coordinate_y=coordinate_y)
        self.stor_square_1 = stor_square_1
        self.stor_square_2 = stor_square_2

    def perim(self):
        perim_square = self.stor_square_1 + self.stor_square_2
        print(perim_square)

    def area(self):
        area_square = self.stor_square_1 * self.stor_square_2
        print(area_square)


if __name__ == "__main__":
    circle = Circle(7, 5)

    square = Square(19, 20)



    print(circle)
    print(square)
    """


import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure:

    class Meta:
        abstract = True

    @staticmethod
    def segment_length(a: Point, b: Point):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError


class Circle(Figure):
    def __init__(self, a: Point, radius: int):
        self.a = a
        self.radius = radius

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)


class Triangle(Figure):
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

        # Calculate segments length using points
        self.segment_1 = self.segment_length(self.a, self.b)
        self.segment_2 = self.segment_length(self.b, self.c)
        self.segment_3 = self.segment_length(self.c, self.a)

    def perimeter(self):
        return round(self.segment_1 + self.segment_2 + self.segment_3, 2)

    def area(self):
        # Use Heron's Formula to calculate triangle area
        half_pr = self.perimeter() / 2
        return round(math.sqrt(
            half_pr * (half_pr - self.segment_1) * (half_pr - self.segment_2) * (half_pr - self.segment_3)
        ), 2)


class Square(Figure):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

        # Calculate segments length using points
        self.segment_1 = abs(self.a.x - self.b.x)
        self.segment_2 = abs(self.a.y - self.b.y)

    def perimeter(self):
        return round((self.segment_1 + self.segment_2) * 2, 2)

    def area(self):
        return round(self.segment_1 * self.segment_2, 2)