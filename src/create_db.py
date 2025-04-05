import psycopg2

from src.config import config


def create_db(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о работодателях и вакансиях"""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers (
                employer_id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                open_vacancies INTEGER,
                description TEXT,                
                area VARCHAR(100)
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                vacancy_id SERIAL PRIMARY KEY,
                employer_id INT REFERENCES employers(employer_id),
                vacancy_name VARCHAR(255) NOT NULL,
                vacancy_url VARCHAR(255) NOT NULL,                
                salary_from INTEGER,
                salary_to INTEGER,
                currency VARCHAR (3),
                requirement TEXT                
            )
        """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    params_for_db = config()
    create_db('hh_data', params_for_db)