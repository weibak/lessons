"""
Написать функцию которая возвращают случайным образом одну карту из стандартной колоды в 36 карт,
где на первом месте номинал карты номинал (6 - 10, J, D, K, A), а на втором название масти
(Hearts, Diamonds, Clubs, Spades).
"""


import random

denomination = ['6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

my_string = f"Your card is: , {random.choice(denomination)} {random.choice(suit)}"
print(my_string)