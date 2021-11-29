"""
Известно, что на шахматной доске 8×8 можно расставить ферзей так, чтобы они не били друг друга
(ферзь может ходить по горизонтали, вертикали и диагонали). Вам дана расстановка двух ферзей на доске,
определите могут ли ферзи бить друг друга. Программа получает на вход две пары чисел, первое число в паре -
координата по горизонтали, второе - координата по вертикали. Если ферзи не бьют друг друга, выведите слово NO,
иначе выведите YES.
"""

import math


def check_coords(coordinate_x1: int, coordinate_y1: int, coordinate_x2: int, coordinate_y2: int) -> bool:
    if coordinate_x1 == coordinate_x2:
        return True
    if coordinate_y1 == coordinate_y2:
        return True
    if math.fabs(coordinate_x1 - coordinate_x2) == math.fabs(coordinate_y1 - coordinate_y2):
        return True
    return False


if __name__ == '__main__':
    coordinate_x1 = int(input("First Line coordinate: "))
    coordinate_y1 = int(input("First Column coordinate: "))
    coordinate_x2 = int(input("Second Line coordinate: "))
    coordinate_y2 = int(input("Second Column coordinate: "))

    if check_coords(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2):
        print("YES")
    else:
        print("NO")





