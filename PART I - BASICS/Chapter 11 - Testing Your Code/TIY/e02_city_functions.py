# Population - e02_city_functions.py
def get_formatted_places(city, country, population=None):
    """Generate a neatly formatted place!."""
    place = f"{city}, {country} - population {population}"
    return place.title()
