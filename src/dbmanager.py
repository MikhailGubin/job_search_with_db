import psycopg2

from src.config import config


class DBManager:
    """ Класс, который может подключаться к базе данных и работать с ней """

    @staticmethod
    def get_companies_and_vacancies_count(conn_params: dict):
        """ Получает список всех компаний и количество вакансий у каждой компании """

        conn = psycopg2.connect(dbname='postgres', **conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("SELECT name, open_vacancies FROM employers")

            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии,
        зарплаты и ссылки на вакансию
        """
        pass

    def get_avg_salary(self):
        """ Получает среднюю зарплату по вакансиям """
        pass

    def get_vacancies_with_higher_salary(self):
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям. """
        pass

    def get_vacancies_with_keyword(self):
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова """
        pass


if __name__ == "__main__":

    params_for_db = config()
    data_manager = DBManager()
    data_manager.get_companies_and_vacancies_count(params_for_db)
