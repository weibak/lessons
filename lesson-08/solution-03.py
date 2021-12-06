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


if __name__ == "__main__":
    n = int(input("Введите количество дисков: "))
    hanoi(n, "A", "B", "C")

"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3. На стержень 1 надета пирамидка
из n дисков различного диаметра в порядке возрастания диаметра. Диски можно перекладывать с одного стержня на другой
строго по одному, при этом диск нельзя класть на диск меньшего диаметра. Необходимо переложить всю пирамидку со
стержня 1 на стержень 3 за минимальное число перекладываний.
Необходимо написать программу, которая для данного числа дисков n печатает последовательность перекладываний,
необходимую для решения головоломки.
"""


def hanoi_tower_loop(n):
    # We assume that the first element on the top of tower
    tower_01 = list(range(1, n + 1))
    tower_02 = []
    tower_03 = []

    # We are moving elements while
    previous_step_target = 0
    while len(tower_01) or len(tower_02):
        if tower_01 and previous_step_target != 1:
            if not tower_02 or tower_02[0] > tower_01[0]:
                print("Move disc", chr(64 + tower_01[0]), "From tower 1 to tower 2")
                previous_step_target = 2

                tower_02.insert(0, tower_01[0])
                del tower_01[0]
                continue

            if not tower_03 or tower_03[0] > tower_01[0]:
                print("Move disc", chr(64 + tower_01[0]), "From tower 1 to tower 3")
                previous_step_target = 3

                tower_03.insert(0, tower_01[0])
                del tower_01[0]
                continue

        if tower_02 and previous_step_target != 2:
            if not tower_03 or tower_03[0] > tower_02[0]:
                print("Move disc", chr(64 + tower_02[0]), "From tower 2 to tower 3")
                previous_step_target = 3

                tower_03.insert(0, tower_02[0])
                del tower_02[0]
                continue

            if not tower_01 or tower_01[0] > tower_02[0]:
                print("Move disc", chr(64 + tower_02[0]), "From tower 2 to tower 1")
                previous_step_target = 1

                tower_01.insert(0, tower_02[0])
                del tower_02[0]
                continue

        if tower_03 and previous_step_target != 3:
            if not tower_02 or tower_02[0] > tower_03[0]:
                print("Move disc", chr(64 + tower_03[0]), "From tower 3 to tower 2")
                previous_step_target = 2

                tower_02.insert(0, tower_03[0])
                del tower_03[0]
                continue

            if not tower_01 or tower_01[0] > tower_03[0]:
                print("Move disc", chr(64 + tower_03[0]), "From tower 3 to tower 1")
                previous_step_target = 1

                tower_01.insert(0, tower_03[0])
                del tower_03[0]
                continue


def hanoi_tower_recursive(n, source, target, buffer):
    if n > 0:
        hanoi_tower_recursive(n - 1, source, buffer, target)
        print("Move disc", chr(64 + n), "From tower", source + 1, "to tower", target + 1)
        hanoi_tower_recursive(n - 1, buffer, target, source)


def main():
    print("Run Hanoi Tower in a loop")
    hanoi_tower_loop(4)

    print("\n ------------------------- \n")

    print("Run Hanoi Tower recursively")
    hanoi_tower_recursive(4, 0, 2, 1)


if __name__ == "__main__":
    main()