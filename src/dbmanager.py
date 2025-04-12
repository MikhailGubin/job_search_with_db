import psycopg2

from src.vacancy import Vacancy


class DBManager:
    """Класс, который может подключаться к базе данных и работать с ней"""

    database_name: str
    conn_params: dict

    def __init__(self, database_name, conn_params):
        """Конструктор создания объекта класса DBManager"""
        self.database_name = database_name
        self.conn_params = conn_params

    def get_companies_and_vacancies_count(self) -> None:
        """Получает список всех компаний и количество вакансий у каждой компании"""
        conn = psycopg2.connect(dbname=self.database_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT employer_title,COUNT(vacancy_url) as amount_vacancies
                FROM employers 
                LEFT JOIN vacancies USING(employer_id)
                GROUP BY employer_title
                """
            )

            employers_list = cur.fetchall()
            for employer in employers_list:
                print(f"Название компании: {employer[0]}. Количество вакансий: {employer[1]}\n")

        conn.commit()
        conn.close()

    def get_all_vacancies(self) -> None:
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии,
        зарплаты и ссылки на вакансию
        """

        conn = psycopg2.connect(dbname=self.database_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(
                """
            SELECT 
            employer_title, vacancy_name, salary_from, salary_to, currency, vacancy_url, requirement
            FROM vacancies    
            JOIN employers USING(employer_id)
            """
            )

            vacancies_list = cur.fetchall()
            self.print_data(vacancies_list)

        conn.commit()
        conn.close()

    def get_avg_salary(self) -> None:
        """Получает среднюю зарплату по вакансиям"""
        conn = psycopg2.connect(dbname=self.database_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(
                """
                    SELECT AVG(salary_from) AS avg_salary
                    FROM vacancies
                    """
            )

            average_salary = int(cur.fetchone()[0])
            print(f"Средняя зарплата по всем вакансиям составляет: {average_salary} RUR\n")

        conn.commit()
        conn.close()

    def get_vacancies_with_higher_salary(self) -> None:
        """Получает список всех вакансий, у которых зарплата выше средней зарплаты по всем вакансиям."""
        conn = psycopg2.connect(dbname=self.database_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(
                """
            SELECT 
            employer_title, vacancy_name, salary_from, salary_to, currency, vacancy_url, requirement
            FROM vacancies    
            JOIN employers USING(employer_id)            
            WHERE salary_from > (
            SELECT AVG(salary_from) AS avg_salary FROM vacancies
            WHERE currency  = 'RUR'
                                )
            ORDER BY employer_id
                            """
            )

            vacancies_list = cur.fetchall()
            self.print_data(vacancies_list)

        conn.commit()
        conn.close()

    def get_vacancies_with_keyword(self, keyword: str) -> None:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        conn = psycopg2.connect(dbname=self.database_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(
                f"""
            SELECT 
            employer_title, vacancy_name, salary_from, salary_to, currency, vacancy_url, requirement
            FROM vacancies    
            JOIN employers USING(employer_id)
            WHERE vacancy_name LIKE '%{keyword}%' 
            ORDER BY employer_id
                                    """
            )

            vacancies_list = cur.fetchall()

            if not vacancies_list:
                print("По Вашему запросу ничего не найдено.")

            self.print_data(vacancies_list)

        conn.commit()
        conn.close()

    @staticmethod
    def print_data(data_from_db: list[tuple]) -> None:
        """Переводит данные из БД в понятный текст"""
        for data in data_from_db:
            salary_dict = {"from": data[2], "to": data[3], "currency": data[4]}
            print(f"Название компании: {data[0]}\n", Vacancy(data[1], data[5], salary_dict, data[6]), "\n")
