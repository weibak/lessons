"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык.
Написать две функции, одна переводит слово с английского на русский, где слово - это входной параметр,
вторая функция - с русского на английский.

"""


"""dictionary = {
    "sun": 'Солнце',
    "moon": "Луна",
}
"""
def translate_en_to_ru(word):
    return dictionary[word]

def translate_ru_to_en(word):
    for en, ru in dictionary.items():   #items делает список [("k1, 1", "k2", 2)], в переменную en - k1, а в ru 1
        if word == ru:
            return en


if __name__ == "__main__":
    dictionary = {"sun": 'Солнце', "moon": "Луна",}
    print(translate_en_to_ru("sun"))
    print(translate_ru_to_en("Луна"))