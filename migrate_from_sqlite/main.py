from read_sqlite import get_sqlite_data
from project_dataclasses import FilmWork, Genre, Person, GenreFilmWork, PersonFilmWork
from write_to_postgres import write_data_to_table


def create_dataclasses(data, dc):
    objects = []
    for count in range(len(data)):
        obj = dict(data[count])
        obj_with_true_fields = {}
        for field in obj:
            if field not in ('file_path',):
                obj_with_true_fields[field] = obj[field]
        objects.append(dc(**obj_with_true_fields))

    return objects


def run():
    movies_data = get_sqlite_data('film_work')
    genres_data = get_sqlite_data('genre')
    persons_data = get_sqlite_data('person')
    genre_film_works_data = get_sqlite_data('genre_film_work')
    person_film_works_data = get_sqlite_data('person_film_work')

    movies_objects = create_dataclasses(movies_data, FilmWork)
    genres_objects = create_dataclasses(genres_data, Genre)
    persons_objects = create_dataclasses(persons_data, Person)
    genre_film_works_objects = create_dataclasses(genre_film_works_data, GenreFilmWork)
    person_film_works_objects = create_dataclasses(person_film_works_data, PersonFilmWork)

    write_data_to_table('film_work', movies_objects)
    write_data_to_table('genre', genres_objects)
    write_data_to_table('person', persons_objects)
    write_data_to_table('genre_film_work', genre_film_works_objects)
    write_data_to_table('person_film_work', person_film_works_objects)


if __name__ == '__main__':
    run()
