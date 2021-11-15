"""
Написать программу, которая будет выводить на экран случайные числа от 1 до 10 до тех пор, пока не выпадет 7.
"""

import random

while True:
    x = random.randint(1, 10)
    if x == 7:
        break
    print(x)
    
"""
x = None
while x!=7:
    x = random.randint(1,10)
    print(x)
"""
