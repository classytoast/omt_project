CREATE SCHEMA IF NOT EXISTS content;

CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    creation_date DATE,
    rating FLOAT,
    type TEXT NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name TEXT NOT NULL,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    genre_id uuid NOT NULL REFERENCES content.genre (id),
    film_work_id uuid NOT NULL REFERENCES content.film_work (id),
    created_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    person_id uuid NOT NULL REFERENCES content.person (id),
    film_work_id uuid NOT NULL REFERENCES content.film_work (id),
    role VARCHAR(256) NOT NULL,
    created_at timestamp with time zone
);

CREATE INDEX film_work_creation_date_idx ON content.film_work(creation_date);

CREATE UNIQUE INDEX film_work_person_idx ON content.person_film_work (film_work_id, person_id, role);

CREATE UNIQUE INDEX film_work_genre_idx ON content.genre_film_work (film_work_id, genre_id);