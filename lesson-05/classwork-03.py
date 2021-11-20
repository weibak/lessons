"""
Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент func_type.
В зависимости от func_type вернуть минимальное либо максимальное значение.
Написать программу в виде трех функций.
"""


my_list = input("введите список чисел через пробел: ").split()
print("ввденый список: ", my_list)
num_list = list(map(int, my_list))

input_func_type = input("Если нужно максимльное значение: 1, если минимальное: 2 ")
func_type = int(input_func_type)

def my_max_min(func_type, my_list):
    if func_type == 1:
        print(max(num_list))
    elif func_type == 2:
        print(min(num_list))
    else:
        print("error")
    return

my_max_min(func_type, my_list)


#print(my_sum(my_list))
#print(max(num_list))