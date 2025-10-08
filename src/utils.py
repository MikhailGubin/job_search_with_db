from src.config import config
from src.create_db import create_db
from src.dbmanager import DBManager
from src.get_hh_data import get_hh_data
from src.save_data_to_db import save_data_to_db


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""

    params_for_db = config()

    print("Здравствуйте!\nДобро пожаловать в приложение для поиска вакансий с платформы hh.ru.")
    name_for_db = input("Введите название базы данных. Название БД по умолчанию hh_data ")
    answer_1 = input("Вывести на экран список всех компаний и количество вакансий у каждой компании? Да/Нет ")
    answer_2 = input(
        "Вывести на экран список всех вакансий с указанием названия компании, названия\n"
        "вакансии, зарплаты и ссылки на вакансию? Да/Нет "
    )
    answer_3 = input("Вывести на экран среднюю зарплату по всем вакансиям? Да/Нет ")
    answer_4 = input(
        "Вывести на экран список всех вакансий, у которых зарплата выше средней зарплаты\n"
        "по всем вакансиям? Да/Нет "
    )
    answer_5 = input(
        "Вывести на экран список всех вакансий, в названии которых содержатся переданные\n" "в метод слова? Да/Нет\n"
    )
    if answer_5:
        search_word = input("Введите слово для поиска\n")

    if not name_for_db:
        name_for_db = "hh_data"

    # Задаю id для работодателей
    company_ids = ["78638", "4181", "80", "2324020", "11732555", "640251", "561525", "25022", "1455", "5599143"]

    params_for_db = config()

    data = get_hh_data(company_ids)

    # Создаю базу данных из полученной информации о работодателях и их вакансиях с сайта hh.ru
    create_db(params_for_db, name_for_db)
    save_data_to_db(data, params_for_db, name_for_db)

    # Создаю экземпляр класса для работы с базой данных
    data_manager = DBManager(name_for_db, params_for_db)

    if answer_1.lower() == "да":
        data_manager.get_companies_and_vacancies_count()

    if answer_2.lower() == "да":
        data_manager.get_all_vacancies()

    if answer_3.lower() == "да":
        data_manager.get_avg_salary()

    if answer_4.lower() == "да":
        data_manager.get_vacancies_with_higher_salary()

    if answer_5.lower() == "да":
        data_manager.get_vacancies_with_keyword(search_word)
