def filter_cars(car_list: list, year: int) -> list:
    result = []
    for car in car_list:
        if car["year"] < year:
            result.append(car)
    return result


car_list = [
    {
        "sn": 123456,
        "color": "red",
        "year": 1999,
    },
    {
        "sn": 234567,
        "color": "black",
        "year": 2020,
    },
    {
        "sn": 345678,
        "color": "white",
        "year": 2012,
    },
]