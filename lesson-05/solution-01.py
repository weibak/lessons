"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра. В результате
ее работы на печать выводятся значения переданных переменных, но только если они не равны
None. Получим, например, следующее сообщение: Переданы аргументы: var1 = 2, var3 = 10.
"""
#попытка дать возможность пользователю ввести данные
#numbers = input("Введите 3 числа: ").split()
#print("ввденый список: ", numbers)
#numbers = list(map(int, numbers)


def three_args(*numbers):
    var_01 = numbers[0]
    var_02 = numbers[1]
    var_03 = numbers[2]
    if var_01 and var_02 and var_03 != None:
        my_string_01 = f"Переданы аргументы: Var1 = , {var_01} , Var2 = {var_02}, Var3 = {var_03}"
        print(my_string_01)
    elif var_01  == None:
        my_string_02 = f"Переданы аргументы:Var2 = {var_02}, Var3 = {var_03}"
        print(my_string_02)
    elif var_02 == None:
        my_string_03 = f"Переданы аргументы:Var1 = , {var_01}, Var3 = {var_03}"
        print(my_string_03)
    elif var_03 == None:
        my_string_04 = f"Var1 = , {var_01} , Var2 = {var_02}"
        print(my_string_04)
    else:
        print("Что-то пошло не так!")

three_args(None, 6, 8)