import psycopg2

from src.config import config


class DBManager:
    """ Класс, который может подключаться к базе данных и работать с ней """

    database_name: str
    conn_params: dict

    def __init__(self, database_name, conn_params):
        """ Конструктор создания объекта класса DBManager """
        self.database_name = database_name
        self.conn_params = conn_params


    def get_companies_and_vacancies_count(self) -> None:
        """ Получает список всех компаний и количество вакансий у каждой компании """
        conn = psycopg2.connect(dbname=self.database_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("""
                SELECT employer_title,COUNT(vacancy_url) as amount_vacancies
                FROM employers 
	            LEFT JOIN vacancies USING(employer_id)
	            GROUP BY employer_title
	            """)

            rows = cur.fetchall()
            for row in rows:
                print(row)

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
            cur.execute("""
            SELECT 
            employer_title, vacancy_name, salary_from, salary_to, currency, vacancy_url
            FROM vacancies    
            JOIN employers USING(employer_id)
            """)

            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()


    def get_avg_salary(self) -> None:
        """ Получает среднюю зарплату по вакансиям """
        conn = psycopg2.connect(dbname=self.database_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("""
                    SELECT AVG(salary_from) AS avg_salary
                    FROM vacancies
                    """)

            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_vacancies_with_higher_salary(self) -> None:
        """ Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям. """
        conn = psycopg2.connect(dbname=self.database_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("""
            SELECT * FROM vacancies
            WHERE salary_from > (
            SELECT AVG(salary_from) AS avg_salary FROM vacancies
                                )
            ORDER BY employer_id
                            """)

            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()

    def get_vacancies_with_keyword(self, keyword: str) -> None:
        """ Получает список всех вакансий, в названии которых содержатся переданные в метод слова """
        conn = psycopg2.connect(dbname=self.database_name, **self.conn_params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f"""
            SELECT * FROM vacancies
            WHERE vacancy_name LIKE '%{keyword}%' 
            ORDER BY employer_id
                                    """)

            rows = cur.fetchall()
            for row in rows:
                print(row)

        conn.commit()
        conn.close()


if __name__ == "__main__":

    params_for_db = config()
    data_manager = DBManager('hh_data',params_for_db)
    # data_manager.get_companies_and_vacancies_count()
    # data_manager.get_all_vacancies()
    # data_manager.get_avg_salary()
    # data_manager.get_vacancies_with_higher_salary()
    data_manager.get_vacancies_with_keyword('разработчик')
