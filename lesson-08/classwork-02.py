"""
Оформить предыдущую задачу в виде программы, вынести функцию в отдельный файл, добавить комментарии с описанием.

"""


#импорт функции и списка в работу из библиотечки
from library import car_list, filter_cars


if __name__ == "__main__":
    year = int(input(("Year: ")))
    print(filter_cars(car_list, year))


#написать короче используя лямбду
    print(list(filter(lambda x: x["year"] < year, car_list)))
#написать без фильтра, легко читается, но медленно работает из-за цикла и постояной работы списка
    print(list(y for y in car_list if y["year"] < year))