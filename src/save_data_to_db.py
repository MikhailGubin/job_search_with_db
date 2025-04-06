from typing import Any
import psycopg2


def save_data_to_db(data: list[dict[str, Any]], database_name: str, params: dict):
    """Сохраняет данные о работодателях и вакансиях в базу данных"""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:

        for data_object in data:
            employer_data = data_object['employer']

            cur.execute(
                """
                INSERT INTO employers (employer_title, open_vacancies, description, area)
                VALUES (%s, %s, %s, %s)
                RETURNING employer_id
                """,
                (employer_data['name'], employer_data['open_vacancies'], employer_data['description'],
                 employer_data['area'])
            )
            employer_id = cur.fetchone()[0]
            print(employer_id)
            vacancies_data = data_object['vacancies']
            print(vacancies_data)

            for vacancy in vacancies_data:

                cur.execute(
                    """
                    INSERT INTO vacancies (
                    employer_id, vacancy_name, vacancy_url, 
                    salary_from, salary_to, currency, 
                    requirement
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (employer_id, vacancy.name, vacancy.vacancy_url,
                     vacancy.salary['from'], vacancy.salary['to'],
                     vacancy.salary['currency'], vacancy.requirement
                     )
                )


    conn.commit()
    conn.close()
