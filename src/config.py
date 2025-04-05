from configparser import ConfigParser
import os


# Получаю абсолютный путь к корневой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def config(filename: str ="database.ini", section: str ="postgresql") -> dict:
    # создаю объект класса ConfigParser
    parser = ConfigParser()
    #Задаю путь к файлу
    path_to_file = os.path.join(BASE_DIR, "data", filename)
    # читаю файл с параметрами
    parser.read(path_to_file)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file.'.format(section, filename))
    return db