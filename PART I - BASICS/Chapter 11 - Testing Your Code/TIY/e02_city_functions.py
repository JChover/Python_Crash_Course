# 11-2 Population - e02_city_functions.py
def get_formatted_places(city, country, population=''):
    """Generate a neatly formatted place!."""
    if population:
        place = f"{city}, {country} - population {population}"
    else:
        place = f"{city}, {country}"
    return place.title()
