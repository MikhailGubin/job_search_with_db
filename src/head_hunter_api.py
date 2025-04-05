import requests


class HeadHunterAPI:
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    __url: str
    __params: dict
    __vacancies: list

    def __init__(self):
        """
        Конструктор объектов класса HeadHunterAPI
        """
        self.__url_vacancies = "https://api.hh.ru/vacancies"
        self.__url_employers = "https://api.hh.ru/employers"
        self.__params = {
            "employer_id": "",
            "page": 0, "per_page": 20
        }
        self.__vacancies = []
        self.__employer = []

    def __connection_to_api_vacancies(self):
        """проверяет правильность подключения к API"""

        try:
            response = requests.get(self.__url_vacancies, params=self.__params)
        except requests.exceptions.RequestException:
            print("Ошибка при работе с HTTP запросом")
            return None

        if response.status_code != 200:
            print(f"Получены неправильные данные от API. Status_code = {response.status_code}")
            return None
        return response.status_code

    def get_vacancies(self, employer_id: str) -> list:
        """
        Получает вакансии с платформы hh.ru по id работодателя
        """
        self.__params["employer_id"] = employer_id
        if self.__connection_to_api_vacancies() != 200:
            print("Неправильный запрос в API")
            return []

        while self.__params.get("page") != 2:
            answer_api = requests.get(self.__url_vacancies, params=self.__params)
            vacancies = answer_api.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

        if not self.__vacancies:
            return []
        return self.__vacancies


    def get_employer(self, employer_id: str) -> dict:
        """
        Получает информацию о работодателях с платформы hh.ru
        """

        try:
            answer_api = requests.get(f'https://api.hh.ru/employers/{employer_id}')
            # answer_api = requests.get(self.__url_employers, params=employer_id)
            # https://api.hh.ru/employers/{employer_id}
        except requests.exceptions.RequestException:
            print("Ошибка при работе с HTTP запросом")
            return {}
        data_api = answer_api.json()
        self.__employer = {
            "name": data_api['name'],
            "open_vacancies": data_api['open_vacancies'],
            "description": data_api['description'],
            "area": data_api['area']['name']
        }

        if not self.__employer:
            print("Отсутствует работодатель с заданным идентификатором")
            return {}
        return self.__employer


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    # employer_ids = [
    #     '78638', '4181', '80',
    #     '2324020', '11732555', '640251',
    #     '561525', '25022', '11679140',
    #     '5599143'
    #                 ]
    print(hh_api.get_employer("78638"))
    print(hh_api.get_vacancies("78638"))