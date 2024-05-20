from dataclasses import astuple, fields
import psycopg
from psycopg import ClientCursor
from psycopg.rows import dict_row

from dsn import dsn


def write_data_to_table(table_name, data_list):
    with psycopg.connect(**dsn, row_factory=dict_row, cursor_factory=ClientCursor) as conn, conn.cursor() as cursor:
        # Получаем названия колонок таблицы (полей датакласса)
        column_names = [field.name for field in fields(data_list[0])]  # [id, name]
        column_names_str = ','.join(column_names)  # id, name

        # В зависимости от количества колонок генерируем под них %s.
        col_count = ', '.join(['%s'] * len(column_names))  # '%s, %s

        bind_values = ','.join(cursor.mogrify(f"({col_count})", astuple(element)) for element in data_list)

        query = (f'INSERT INTO content.{table_name} ({column_names_str}) VALUES {bind_values} '
                 f'ON CONFLICT (id) DO NOTHING')

        cursor.execute(query)
