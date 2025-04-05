class Vacancy:
    """
    Класс для работы с вакансиями
    """

    __slots__ = ("name", "vacancy_url", "salary", "requirement")
    name: str
    vacancy_url: str
    salary: dict
    requirement: str

    def __init__(self, name, vacancy_url, salary, requirement) -> None:
        """
        Конструктор создания объектов класса Vacancy
        """

        self.name = self.__valid_attribute(name)
        self.vacancy_url = self.__valid_attribute(vacancy_url)
        self.salary = self.__valid_salary(salary)
        self.requirement = self.__valid_attribute(requirement)

    def __eq__(self, other) -> bool:
        """Устанавливает правило, когда объекты класса Vacancy между собой равны"""
        return self.salary["from"] == other.salary["from"]

    def __lt__(self, other) -> bool:
        """Устанавливает правило, когда один объект класса Vacancy меньше другого объекта класса Vacancy"""

        return self.salary["from"] < other.salary["from"]

    @staticmethod
    def __valid_attribute(attribute: str) -> str:
        """Проверяет валидацию атрибута"""
        if not attribute:
            return 'Не указано'
        return attribute

    @staticmethod
    def __valid_salary(salary: dict | None) -> dict:
        """Проверяет валидацию зарплаты"""
        # if isinstance(salary, dict) and isinstance(salary['from'], float):
        if isinstance(salary, dict):
            if not isinstance(salary["from"], float | int):
                salary["from"] = 0

            if not isinstance(salary["to"], float | int):
                salary["to"] = 0

            return salary
        return {"from": 0, "to": 0, "currency": "RUR"}

    @classmethod
    def cast_to_object_list(cls, api_answer: dict | list) -> list:
        """Преобразует набор данных в список объектов класса Vacancy"""
        if not api_answer:
            print("Пустой ответ от API")
            return []

        vacancies_list = []
        for vacancy in api_answer:
            if vacancy.get("snippet"):
                requirement = vacancy["snippet"]["requirement"]
            else:
                requirement = "Не указано"

            if vacancy.get("url"):
                vacancy_url = vacancy["url"]
            else:
                vacancy_url = vacancy["vacancies_url"]

            vacancy_collection = {
                "name": vacancy["name"],
                "vacancy_url": vacancy_url,
                "salary": vacancy["salary"],
                "requirement": requirement,
            }

            vacancies_list.append(cls(**vacancy_collection))

        return vacancies_list

    def cast_to_dict(self) -> dict:
        """Преобразует объект класса Vacancy в словарь"""
        return {
            "name": self.name,
            "vacancy_url": self.vacancy_url,
            "salary": self.salary,
            "requirement": self.requirement,
        }

    def __str__(self) -> str:
        """Настраивает отображения информации об объекте класса Vacancy"""

        text_salary = f'{self.salary['from']} - {self.salary["to"]} {self.salary['currency']}'

        if not self.salary["to"] and not self.salary["from"]:
            text_salary = "Зарплата не указана"
        elif not self.salary["to"]:
            text_salary = f"от {self.salary['from']} {self.salary['currency']}"
        elif not self.salary["from"]:
            text_salary = f'до {self.salary["to"]} {self.salary['currency']}'

        return f"{self.name}\n{self.vacancy_url}\n{text_salary}\n{self.requirement}"
