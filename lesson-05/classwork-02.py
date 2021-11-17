"""
Создать функцию, которая принимает на вход неопределенное количество аргументов и возвращает их
сумму и максимальное из них.

"""

def my_sum(func_type, *args):
    result = 0
    for x in args:
        result += x
    return result

print(my_sum(1, 4, 5, 11, 43))