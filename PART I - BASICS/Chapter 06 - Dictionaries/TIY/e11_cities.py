# 6-11 Cities
cities = {  # We nest a Dictionary inside the value of each key from the first Dictionary
    'paris': {
        'country': 'france',
        'population': 2102650,
        'fact': 'Is the 9th most populated city of Europe'
    },
    'london': {
        'country': 'united kingdom',
        'population': 8866180,
        'fact': 'Is the 3d most populated city of Europe'
    },
    'madrid': {
        'country': 'spain',
        'population': 3223334,
        'fact': 'Is the 6th most populated city of Europe'
    }
}

for city, city_info in cities.items():  # Nesting quickly adds complexity to the code
    print(f"\nInformation about {city.title()}:")
    print(f"\t - Country: {city_info['country'].title()}.")
    print(f"\t - Population: {city_info['population']:,} people.")
    print(f"\t - Curious Fact: {city_info['fact']}.")
