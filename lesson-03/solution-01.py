"""Пользователь делает вклад в размере 2130 рублей сроком на 5 лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты). Рассчитать сумму на счету пользователя по окончании вклада и вывести на печать, если в конце каждого года ему начисляется бонус в размере 120 рублей.
"""

money = 2130
period = 5
tax = 0.1
bonus = 120

"""year_01 = money + money * tax + bonus
year_02 = money + money * tax + bonus
year_03 = money + money * tax + bonus
year_04 = money + money * tax + bonus
year_05 = money + money * tax + bonus
"""
while period > 0:
    money = money + money * tax + bonus
    period -= 1



print(money)

