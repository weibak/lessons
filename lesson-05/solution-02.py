"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с
именами участников. Затем каждый играющий по очереди вытягивает бумажку с именем того, кому
предстоит вручить презент. Ваша программа должна используя список имен участников выдать на
выходе пары, кто и кому будет дарить, причем сам себе человек не может подарить, дубликаты
тоже не допустимы.
"""

import random


my_list = input("Введите список имен через пробел: ").split()
print("Ввденый список: ", my_list)


random.shuffle(my_list)
offset = [my_list[-1]] + my_list[:-1]
for santa, receiver in zip(my_list, offset):
     print(santa, "дарит подарок", receiver)

"""другой вариант решения который я так и не смог допилить
random.shuffle(new_my_list_1)
new_my_list = my_list + new_my_list_1

for i in range(len(new_my_list)):
    if i % 2 == 0:
        list1 = new_my_list
        list2 = new_my_list[i-1]
        for n in range(len(list1)):
            new_my_list.append([list1[n], list2[n]])

print(new_my_list)

"""