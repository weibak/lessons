"""
Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10.
"""
my_list = [5, 3, 7, 15, 22, 4, 18]
result = 0

for x in my_list:
    if x > 10:
        result += x
        
print(result)
    
