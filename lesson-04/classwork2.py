"""
Написать программу, которая выведет на экран все числа от 1 до 100 которые кратные n (n вводится с клавиатуры).
"""

n = int(input("Enter number: "))

for x in range(1, 101):
    if x % n == 0:
        print(x)
