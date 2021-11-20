"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца - и возвращает название сезона,
к которому относится этот месяц. Например, передаем 2, на выходе получаем "Winter".

"""

month = int(input("Введите номер месяца: "))


def month_to_season(month):
    if (0 < month <= 2 or month == 12):
        print("Winter")
    elif (3 <= month <= 5):
        print("Spring")
    elif (6 <= month <= 8):
        print("Summer")
    elif (9 <= month <= 11):
        print("Autumn")
    else:
        print("Что-то пошло не так!")

month_to_season(month)