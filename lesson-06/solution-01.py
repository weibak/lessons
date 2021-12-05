"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
"""


word_list = input("Введите слова через пробел: ").split()
print("Введеный список слов: ", word_list)


new_word_list = {i: word_list.count(i) for i in word_list}
maxcnt = 0
theltr = 0
for ltr in new_word_list:
    ltrfoud = ltr
    foundcont = new_word_list[ltr]
    if foundcont > maxcnt:
        maxcnt = foundcont
        theltr = ltrfoud
print('Наиболее часто повторяющееся: ' + theltr)


longword = []
for i in word_list:
        longword.append(len(i))
print('Самое длинное слово: ', word_list[longword.index(max(longword))])