"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами
1, 2, 3. На стержень 1 надета пирамидка из n дисков различного диаметра в порядке
возрастания диаметра. Диски можно перекладывать с одного стержня на другой строго
по одному, при этом диск нельзя класть на диск меньшего диаметра. Необходимо
переложить всю пирамидку со стержня 1 на стержень 3 за минимальное число
перекладываний.
Необходимо написать программу, которая для данного числа дисков n печатает
последовательность перекладываний, необходимую для решения головоломки.
"""

#один из вариантов решения, но как по мне работает кривовато
"""
def hanoi (n, first = 1, last = 3):
    if n == 1:
        print(f"Переложит диск {n} со стержня {first} на стержень {last}")
    else:
        hanoi(n - 1, first, 6 - first - last)
        print(f"Переложит диск {n} со стержня {first} на стержень {last}")
        hanoi(n - 1, 6 - first - last, last)


count = int(input("Введите количество дисков: "))
hanoi(count)
"""

def hanoi(height, fromePole, toPole, withPole):
    if height >= 1:
        hanoi(height -1, fromePole, withPole, toPole)
        move_disk(fromePole, toPole)
        hanoi(height - 1, withPole, toPole, fromePole)

def move_disk(fp, tp):
    print("Перемещение диска с ",fp,"на ",tp)

n = int(input("Введите количество дисков: "))
hanoi(n, "A", "B", "C")