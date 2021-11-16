"""
Ввести с клавиатуры строку, проверить является ли строка палиндромом и вывести результат (yes/no) на экран. Палиндром - это слово или фраза, которые одинаково читаются слева направо и справа налево

"""

my_list_01 = list(input("write some word or string: "))
my_list_02 = my_list_01[::-1]

if my_list_01 == my_list_02:
    print("Palindrome")
else:
    print("Not a Palindrome")

