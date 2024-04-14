CREATE TABLE IF NOT EXISTS cities (
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255) NOT NULL PRIMARY KEY,
    country_name VARCHAR(255) NOT NULL,
    latitude DECIMAL(9, 7),
    longitude DECIMAL(10, 7)
);

INSERT INTO
    cities (city_name, country_name, latitude, longitude)
VALUES
    ('Sao Paulo', 'Brazil', -23.5475000, -46.6361122),
    ('Lisbon', 'Portugal', 38.7166667, -9.1333332),
    ('Porto', 'Portugal', 41.1500000, -8.6166668),
    ('Zurich', 'Switzerland', 47.3666667, 8.5500002);
