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

if __name__ == "__main__":
    print(previosly)
    print(max_reply)

"""
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих
элементов этой последовательности равны друг другу и что это за элемент. Т.е. если программе на вход подать
последовательность [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5], то на печать программа должна вывести числа 4 и 3,
где 4 - повторяющийся элемент, 3 - количество повторений.
"""


def get_list_most_common_element(number_list: list) -> tuple:
    result = {}

    # Iterate over list and calculate max repetitions
    previous_number = None
    current_sequence = 0
    for number in number_list:
        if number == 0:
            # Save last found result and break the loop
            result[previous_number] = current_sequence
            break

        # Check if start new sequence
        if previous_number == number:
            current_sequence += 1
        else:
            # Check previous sequence and if current bigger - save it
            # or simply set current value
            if previous_number not in result:
                result[previous_number] = current_sequence
            elif result[previous_number] < current_sequence:
                result[previous_number] = current_sequence

            # restart current sequence
            current_sequence = 1

        # Remember number for the next iteration
        previous_number = number

    # Assume that the first element is max and try to find a bigger element
    max_number = list(result.keys())[0]
    max_repetitions = result[max_number]
    for key, value in result.items():
        if value > max_repetitions:
            max_number = key
            max_repetitions = value
    return max_number, max_repetitions


def main():
    number_list = [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5]
    max_number, max_repetitions = get_list_most_common_element(number_list)
    print(max_number, max_repetitions)


if __name__ == "__main__":
    main()