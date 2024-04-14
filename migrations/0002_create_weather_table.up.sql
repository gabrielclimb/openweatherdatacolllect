CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city_id BIGINT,
    lon DECIMAL(9, 6),
    lat DECIMAL(9, 6),
    weather_id INT,
    weather_main TEXT,
    weather_description TEXT,
    weather_icon TEXT,
    base TEXT,
    temp DECIMAL,
    feels_like DECIMAL,
    temp_min DECIMAL,
    temp_max DECIMAL,
    pressure INT,
    humidity INT,
    sea_level INT,
    grnd_level INT,
    visibility INT,
    wind_speed DECIMAL,
    wind_deg INT,
    wind_gust DECIMAL,
    rain_1h DECIMAL,
    rain_3h DECIMAL,
    snow_1h DECIMAL,
    snow_3h DECIMAL,
    clouds_all INT,
    dt BIGINT,
    sys_type INT,
    sys_id BIGINT,
    sys_message TEXT,
    sys_country TEXT,
    sunrise BIGINT,
    sunset BIGINT,
    timezone INT,
    cod INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_city FOREIGN KEY (city_id) REFERENCES cities (id)
);
