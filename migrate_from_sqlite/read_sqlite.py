import os.path

from sqlite_context import conn_context


def get_sqlite_data(table):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db.sqlite")

    with conn_context(db_path) as conn:
        curs = conn.cursor()
        curs.execute(f"SELECT * FROM {table};")
        data = curs.fetchall()
        # print(dict(data[0]))

    return data


if __name__ == "__main__":
    data = get_sqlite_data('film_work')
    print(dict(data[0]))
    # print(len(data))
    # for row in data[0]:
    #     print(row)
