"""Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой
системе, функция имеет два параметра: ссылка на файл и имя на файловой системе. В качестве
примера ссылки на файл можно использовать лицензию из ГитХаба из вашего репозитория:
https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE
"""

from pathlib import Path
import requests


def load_file(link, name_in_system):
    filename = Path(name_in_system)
    url = link
    response = requests.get(url)
    filename.write_bytes(response.content)

load_file('https://github.com/weibak/lessons/blob/master/LICENSE.txt', 'load_license_file.txt')
