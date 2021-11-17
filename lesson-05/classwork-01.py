"""
Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}".
Создать список из 5 имен. Вызвать функцию для каждого элемента списка в цикле.
"""


def my_format(name):
    result_string = f"{name}"
    return result_string

my_list = ["Olga", "Alex", "Dima", "Roma", "Denis"]

for name in my_list:
    print(my_format(name))

"""можно написать вот так
result = my_format(name)
print(result)
"""