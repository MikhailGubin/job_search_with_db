import os

from src.config import config
from src.create_db import create_db
from src.dbmanager import DBManager
from src.get_hh_data import get_hh_data
from src.save_data_to_db import save_data_to_db


def main():
    #Задаю id для работодателей
    company_ids = [
        '78638', '4181', '80',
        '2324020', '11732555', '640251',
        '561525', '25022', '11679140',
        '5599143'
    ]

    params_for_db = config()

    data = get_hh_data(company_ids)

    create_db('hh_data', params_for_db)
    save_data_to_db(data, 'hh_data', params_for_db)
    data_manager = DBManager('hh_data', params_for_db)
    data_manager.get_companies_and_vacancies_count()

if __name__ == '__main__':
    main()

