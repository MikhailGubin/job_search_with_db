# Программа для поиска вакансий

## Описание:      
    Данная программа получает данные о компаниях и вакансиях с платформы hh.ru, сохраняет ее в таблицы в БД PostgreSQL. 
    Также в данной программе реализован класс DBManager, который позволяет работать с данными в БД.  
---

## Содержание:
* ## <a id="title1">Описание</a>
* ## <a id="title1">Установка</a>
* ## <a id="title1">Описание файлов</a>
* ## <a id="title1">Команда проекта</a>
* ## <a id="title1">Источники</a>

---

## Установка:
1. #### Клонируйте репозиторий:
```commandline
python
git clone git@github.com:MikhailGubin/banking_operations.git
```

2. #### Установите зависимости:
```commandline
python
pip install -r requirements.txt
```

---

## Описание файлов:

1. #### main.py 
##### Описание:
    Cодержит функцию main для взаимодействия с пользователем, с помощью которой можно получить 
    результат всех реализованных в проекте функциональностей. Находится в корневой папке проекта.

2. #### config.py
##### Описание:
    В данном файле содержится функция config, которая получает словарь с данными для подключения к БД 
    из файла database.ini. Находится в директории src.

3. #### database.ini
##### Описание:
    В данном файле содержится словарь с данными для подключения к БД. 
    Находится в директории data.
    Пример данных в файле:
```commandline
python
[postgresql]
host=localhost
user=postgres
password=password
port=5432
```

4. #### head_hunter_api.py
##### Описание:
    В данном файле реализован класс HeadHunterAPI, который нужен для работы с API HeadHunter.  
    Находится в директории src.

5. #### get_hh_data.py
##### Описание:
    Содержит функцию get_hh_data, которая собирает данные о фирмах и их вакансиях, 
    полученные с помощью API hh.ru, в один список. Находится в директории src.

6. #### create_db.py
##### Описание:
    Содержит функцию create_db, которая создает БД и таблицы для сохранения данных о работодателях и вакансиях.
    Находится в директории src.

7. #### save_data_to_db.py
##### Описание:
    Содержит функцию save_data_to_db, которая сохраняет данные о работодателях и вакансиях в базу данных.
    Находится в директории src.

8. #### vacancy.py
##### Описание:
    Содержит содержит класс Vacancy для работы с вакансиями. Находится в директории src.

9. #### dbmanager.py
##### Описание:
    Содержит содержит класс DBManager для работы с данными в БД. Находится в директории src.

---

## Команда проекта:
* Губин Михаил — Back-End Engineer

---

## Источники:
* курс лекций и учебных материалов учебного центра "SkyPro"
