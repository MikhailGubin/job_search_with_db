# Программа для поиска вакансий

## Описание:
    Данная программа получает информацию о вакансиях с платформы hh.ru в России, сохраняет ее в файл. 
    Также данная программа позволяет удобно работать с вакансиями: добавлять в файл, фильтровать и удалять их из файла.  
---

## Содержание:
* ## <a id="title1">Описание</a>
* ## <a id="title1">Установка</a>
* ## <a id="title1">Использование</a>
* ## <a id="title1">Тестирование</a>
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

## Использование:

1. #### Класс Parser 
##### Описание:
    Абстрактный класс для работы с API сервиса с вакансиями, базвоый для класса HeadHunterAPI 
    Атрибутов у класса нет.
    Есть один абстрактный метод get_vacancies

2. #### Класс HeadHunterAPI
##### Описание:
    Класс для работы с API сервиса с вакансиями, наследуется  от абстрактного класса Parser.
    Подключается к API и получает вакансии.
    Атрибуты класса:
    __url: str - приватный атрибут, содержит url API 
    __params: dict - приватный атрибут, содержит параметры, необходимые для запроса API сервиса с вакансиями
    __vacancies: list - приватный атрибут, в который записываются вакансий платформы hh.ru
    В данном классе содержатся два метода:
    __connection_to_api - приватный метод, проверяет правильность подключения к API;
    get_vacancies - метод, который наследуется от родительского класса Parser, получает вакансии с платформы hh.ru.
    В данном методе на вход принимается строка, которая ищется в полях вакансий.
##### Пример работы с объектами и методами класса:

```commandline
python
Пример работы с объектами и методами класса:
    
    #Создаёт объект класса HeadHunterAPI
    hh_api = HeadHunterAPI()  
    
   #Записывает в переменную vacancies_data список вакансий, полученный с платформы hh.ru.
   vacancies_data = hh_api.get_vacancies('Python') 

```

3. #### Класс Vacancy 
##### Описание:
    Класс для работы с вакансиями.
    В классе используется __slots__ для экономии памяти.
    Атрибуты класса:
    name: str - название вакансии
    vacancy_url: str - ссылка на данную вакансию
    salary: dict - словарь, в котором содержится информация о диапазоне заработной платы и о валюте, в которой 
    зарплата будет выплачиваться
    requirement: str - требования к работе, представленной в вакансии
    Класс поддерживает методы сравнения вакансий между собой по зарплате и валидирует данные, которыми инициализируются 
    его атрибуты.
    В данном классе реализованы следующие методы:
    * cast_to_object_list - классовый метод, который преобразует набор данных в список объектов класса Vacancy
    * cast_to_dict - метод, который преобразует объект класса Vacancy в словарь
    * магические метод __str__, __lt__, __eq__.
    Сравнение объектов класса Vacancy производится по нижнему значению диапазона заработной платы
##### Пример работы с объектами и методами класса:

```commandline
python
Пример работы с объектами и методами класса:
    
     #Создаёт объект класса Vacancy:
     Vacancy('Junior Python Developer',
                      'https://api.hh.ru/vacancies/110412720?host=hh.ru',
                      {'currency': 'RUR', 'from': 100000, 'gross': False, 'to': 150000},
                      'Базовые знания <highlighttext>Python</highlighttext>. Опыт написания REST приложений'
                      ' на любом <highlighttext>Python</highlighttext> фреймворке (Flask, FastAPI, Django и др.).'
                      'Понимание основ SQL и...')
     
    #Преобразует объект класса Vacancy в словарь:              
    print(example_vacancy.cast_to_dict())
    
    #Выведет в конссоль:
    {"name": 'Junior Python Developer',
    "vacancy_url":'https://api.hh.ru/vacancies/110412718?host=hh.ru',
    "salary": {'currency': 'RUR', 'from': 75000, 'gross': False, 'to': None},
    "requirement": 'Базовые знания '
                    '<highlighttext>Python</highlighttext>. Опыт '
                    'написания REST приложений на любом '
                    '<highlighttext>Python</highlighttext> фреймворке '
                    '(Flask, FastAPI, Django и др.). Понимание основ '
                    'SQL и...'}
    
    #Преобразует набор данных в список объектов класса Vacancy:
    
    python_developer = Vacancy.cast_to_object_list(answer_api_example['items'])
    print(python_developer)
    
    #Выведет в конссоль: 
    
    Junior Python Developer
    https://api.hh.ru/vacancies?employer_id=10911658
    от 75000 RUR
    Базовые знания <highlighttext>Python</highlighttext>. Опыт написания REST приложений на любом 
    <highlighttext>Python</highlighttext> фреймворке (Flask, FastAPI, Django и др.). Понимание основ SQL и...

```

4. #### Класс FileChange
##### Описание:
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл (add_vacancies),
    получения данных из файла (get_data_from_file) и 
    удаления информации о вакансиях (delete_vacancy).

5. #### Класс JSONSaver
##### Описание:
    Класс для работы с данными в JSON-файле. Наследуется от класса FileChange.
    Атрибуты класса:
    __file_name: str - содержит название файла, с которым будут работать методы данного класса
    __path: str - содержит путь к файлу
    Методы данного класса:
    * get_data_from_file - метод получения данных из файла
    *  add_vacancies - метод добавления данные в файл 
    * delete_vacancy - метод удаления вакансии из файла. Проверяет по url.
##### Пример работы с объектами и методами класса:

```commandline
python
Пример работы с объектами и методами класса:
    
    #Создаёт объект класса JSONSaver
    json_saver = JSONSaver()
    
    #Добавляет объект example_vacancy в JSON-файл
    json_saver.add_vacancies([example_vacancy])
    
    #Удаляет объект example_vacancy из JSON-файла
    json_saver.delete_vacancy(example_vacancy)

```

6. #### Функция filter_vacancies
##### Описание:
    Сортирует вакансии по заданной строке, которая будет в поле значений ключа requirement 
    
##### Пример работы функции:
```commandline
python
Пример работы функции:
    
    #Запишет в переменную vacancies_filtered список вакансий со строками 'REST' и 'Python'
    vacancies_filtered = filter_vacancies(vacancies_list, ['REST', 'Python'])
    
```

7. #### Функция get_top_vacancies 
##### Описание:
    Собирает список из заданного количества вакансий с самой большой заработной платой. Количество вакансий 
    принимается на вход функции
##### Пример работы функции:

```commandline
python
Пример работы функции: 
      
    number_of_vacancies = 3
    #Запишет в переменную top_vacancies список из 3-ех вакансий с самой большой зарабатной платой
    top_vacancies = get_top_vacancies(vacancies_list, number_of_vacancies)
    
```

8. #### Функция get_vacancies_by_salary
##### Описание:
    Ищет вакансии с заработной платой, подходящие под заданный диапазон зарплат. Вакансия добавится в список, 
    если нижнее значение зарплаты из вакансии попадает в заданный диапазон зарплат.
##### Пример работы функции:

```commandline
python
Пример работы тфункции: 

    salary_range = '100000 - 150000'
    #Запишет в переменную sorted_vacancies список вакансий, у которых нижнее значение зарплаты попадает 
    #в заданный диапазон зарплат
    sorted_vacancies = get_vacancies_by_salary(vacancies_list, salary_range)
    
```

9. #### Функция user_interaction
##### Описание:
    Функция взаимодействует с пользователем через консоль. Возможности этой функции должны быть следующими:
    * по поисковому запросу от пользователя получает вакансии из hh.ru;
    * сортирует вакансии по заданным словам в поле requirement;
    * сортирует вакансии по заданному диапазону зарплат;
    * выводит топ N вакансий по зарплате (N запрашивает у пользователя);
    Полученный список вакансий записывается в файл и подается на выход данной программы

##### Пример работы функции:

```commandline
python
Пример работы функции:   
    
    #Запишет в переменную vacancies_list список вакансий, у которые будут удовлетворять всем требованиям пользователя 
    vacancies_list = user_interaction()
    
Пример данных в консоли:

   Введите поисковый запрос: Python
   Введите количество вакансий для вывода в топ N: 3
   Введите ключевые слова для фильтрации вакансий: Java
   Введите диапазон зарплат: (Например: 100000 - 150000) 0 - 150000
   Младший backend-разработчик
   https://api.hh.ru/vacancies/118348961?host=hh.ru
   80000 - 120000 RUR
   Базовые знания одного из языков программирования — <highlighttext>Python</highlighttext>, Java, C#, PHP, Ruby, Go 
   или JavaScript. У нас есть микросервисы почти на...
   QA-тестировщик /QA engineer (Middle/Senior)
   https://api.hh.ru/vacancies/110240273?host=hh.ru
   80000 - 150000 RUR
   Опыт настройки автотестов на языках, таких как <highlighttext>Python</highlighttext>, Java или JavaScript. Навыки 
   работы с инструментами автоматизации, например, Selenium, Appium, и...

```
---

## Тестирование:
Код данного проекта покрыт тестами фреймворка pytest более чем на 70 %. 

Для запуска тестов выполните команду:

'''
python
pytest
'''

Чтобы установить pytest через Poetry, используйте команду:

'''
python
poetry add --group dev pytest
'''

Модули с тестами хранятся в директории tests\. 

---

## Команда проекта:
* Губин Михаил — Back-End Engineer

---

## Источники:
* курс лекций и учебных материалов учебного центра "SkyPro"
