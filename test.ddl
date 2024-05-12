INSERT INTO genre(id, name, description)
VALUES((SELECT gen_random_uuid()),
        'Комедия',
        'жанр кинопроизведений, в основе которых
        эстетические категории сатиры, юмора, буффонады.'
        );