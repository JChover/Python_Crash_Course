# 6-5 Rivers
rivers = {
    'senna': 'france',
    'thames': 'england',
    'ebro': 'spain'
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThis is the list of all the rivers:")
for river in rivers.keys():  # The .keys() method can be omitted here as its the default
    print(river.title())

print("\nThis is the list of all the countries:")
for country in rivers.values():
    print(country.title())
