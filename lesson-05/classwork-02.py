"""
Создать функцию, которая принимает на вход неопределенное количество аргументов и возвращает их
сумму и максимальное из них.

"""


my_list = input("введите список чисел через пробел: ").split()
print("ввденый список: ", my_list)

num_list = list(map(int, my_list))

def my_sum(my_list):
    result = 0
    for x in num_list:
        result += x
    return result

print(my_sum(my_list))
print(max(num_list))