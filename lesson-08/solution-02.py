"""
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите,
какое наибольшее число подряд идущих элементов этой последовательности равны
друг другу и что это за элемент.
Т.е. если программе на вход подать последовательность [1, 2, 2, 3, 7, 4, 4, 4,
0, 5, 5, 5], то на печать программа должна вывести числа 4 и 3, где 4 -
повторяющийся элемент, 3 - количество повторений
"""

previosly = -1
curr_reply = 0
max_reply = 0
element = int(input("Insert elements: "))
while element != 0:
    if previosly == element:
        curr_reply += 1
    else:
        previosly = element
        max_reply = max(max_reply, curr_reply)
        curr_rep = 1
    element = int(input("Insert elements: "))
max_reply = max(max_reply, curr_reply)

print(previosly)
print(max_reply)