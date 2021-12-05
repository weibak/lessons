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


def prime_numbers(n: int, m: int) -> list:
    result = []
    for element in range(n, m + 1):
        # Check if this element is the prime number
        is_prime = True
        for divider in range(2, element):
            # If we've found any divider the remainder of which is zero
            # So current element is not the prime number
            if divider > 1 and element % divider == 0:
                is_prime = False
                break
        if is_prime:
            result.append(element)
    return result


if __name__ == "__main__":
    n = int(input("N: "))
    m = int(input("M: "))

    print(prime_numbers(n, m))