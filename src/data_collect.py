from src.db.operations import get_all_cities

cities = get_all_cities()

for city in cities:
    print(city.city_name)
    print(city.country_name)
    print(city.latitude)
    print(city.longitude)
    print()
