# 8-6 City Names
def city_country(city, country):
    """Prints a String with a City and Country"""
    return f"{city.title()}, {country.title()}"


print(city_country('tokio', 'japan'))
print(city_country('seoul', 'south korea'))
print(city_country('madrid', 'spain'))
