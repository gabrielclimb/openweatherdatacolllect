CREATE TABLE IF NOT EXISTS city (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    country VARCHAR(255) NOT NULL,
    latitude DECIMAL(9, 7),
    longitude DECIMAL(10, 7)
);
