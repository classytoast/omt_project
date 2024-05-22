import unittest
from datetime import datetime

from migrate_from_sqlite.project_dataclasses import FilmWork, Genre, Person, GenreFilmWork, PersonFilmWork
from migrate_from_sqlite.dsn import dsn
from migrate_from_sqlite.read_sqlite import get_sqlite_data
from select_from_postgres import get_data_from_table
from dataclasses_for_tests import create_dataclasses


class TestDatabase(unittest.TestCase):

    movies_data_sqlite = get_sqlite_data('film_work')
    genres_data_sqlite = get_sqlite_data('genre')
    persons_data_sqlite = get_sqlite_data('person')
    genre_film_works_data_sqlite = get_sqlite_data('genre_film_work')
    person_film_works_data_sqlite = get_sqlite_data('person_film_work')

    movies_data_postgres = get_data_from_table('film_work', dsn)
    genres_data_postgres = get_data_from_table('genre', dsn)
    persons_data_postgres = get_data_from_table('person', dsn)
    genre_film_works_data_postgres = get_data_from_table('genre_film_work', dsn)
    person_film_works_data_postgres = get_data_from_table('person_film_work', dsn)

    def test_len_film_work(self):
        self.assertEqual(len(self.movies_data_sqlite), len(self.movies_data_postgres))

    def test_len_genre(self):
        self.assertEqual(len(self.genres_data_sqlite), len(self.genres_data_postgres))

    def test_len_person(self):
        self.assertEqual(len(self.persons_data_sqlite), len(self.persons_data_postgres))

    def test_len_genre_film_works(self):
        self.assertEqual(len(self.genre_film_works_data_sqlite), len(self.genre_film_works_data_postgres))

    def test_len_person_film_works(self):
        self.assertEqual(len(self.person_film_works_data_sqlite), len(self.person_film_works_data_postgres))

    def test_there_are_all_movies_from_sqlite(self):
        records_are_the_same = True
        for obj_sqlite in self.movies_data_sqlite:
            there_is = False
            for obj_postgres in self.movies_data_postgres:
                if list(obj_sqlite)[:3] == list(obj_postgres)[:3]:
                    there_is = True
                    break
            if not there_is:
                records_are_the_same = False
                break
        self.assertEqual(records_are_the_same, True)

    def test_there_are_all_genres_from_sqlite(self):
        records_are_the_same = True
        for obj_sqlite in self.movies_data_sqlite:
            there_is = False
            for obj_postgres in self.movies_data_postgres:
                if list(obj_sqlite)[:3] == list(obj_postgres)[:3]:
                    there_is = True
                    break
            if not there_is:
                records_are_the_same = False
                break
        self.assertEqual(records_are_the_same, True)

    def test_there_are_all_genre_film_works_from_sqlite(self):
        records_are_the_same = True
        for obj_sqlite in self.genre_film_works_data_sqlite:
            there_is = False
            for obj_postgres in self.genre_film_works_data_postgres:
                if list(obj_sqlite)[:1] == list(obj_postgres)[:1]:
                    there_is = True
                    break
            if not there_is:
                records_are_the_same = False
                break
        self.assertEqual(records_are_the_same, True)

    def test_there_are_all_persons_from_sqlite(self):
        records_are_the_same = True
        for obj_sqlite in self.persons_data_sqlite:
            there_is = False
            for obj_postgres in self.persons_data_postgres:
                if list(obj_sqlite)[:2] == list(obj_postgres)[:2]:
                    there_is = True
                    break
            if not there_is:
                records_are_the_same = False
                break
        self.assertEqual(records_are_the_same, True)

    def test_there_are_all_person_film_works_from_sqlite(self):
        records_are_the_same = True
        for obj_sqlite in self.person_film_works_data_sqlite:
            there_is = False
            for obj_postgres in self.person_film_works_data_postgres:
                if list(obj_sqlite)[:1] == list(obj_postgres)[:1]:
                    there_is = True
                    break
            if not there_is:
                records_are_the_same = False
                break
        self.assertEqual(records_are_the_same, True)


if __name__ == '__main__':
    unittest.main()
