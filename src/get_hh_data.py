from typing import Any

from src.head_hunter_api import HeadHunterAPI
from src.vacancy import Vacancy


def get_hh_data(employers_id_list: list[str]) -> list[dict[str, Any]]:
    """
    Собирает данные о фирмах и их вакансиях, полученные с помощью API hh.ru, в один список
    """

    data = []

    hh_api = HeadHunterAPI()

    for employer_id in employers_id_list:
        employer_data = hh_api.get_employer(employer_id)
        vacancies_data = hh_api.get_vacancies(employer_id)
        vacancies_list = Vacancy.cast_to_object_list(vacancies_data)
        data.append(
            {
            'employer': employer_data,
            'vacancies': vacancies_list
        }
        )

    return data


if __name__ == "__main__":
    employer_ids = [
        '78638', '4181', '80',
        '2324020', '11732555', '640251',
        '561525', '25022', '11679140',
        '5599143'
    ]
    print(get_hh_data(employer_ids))

