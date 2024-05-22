import contextlib

import psycopg2


def get_data_from_table(table_name, dsn):

    with contextlib.closing(psycopg2.connect(**dsn)) as conn, conn.cursor() as cur:
        cur.execute(f"""SELECT *
                        FROM content.{table_name}""")
        result = cur.fetchall()
        return result

