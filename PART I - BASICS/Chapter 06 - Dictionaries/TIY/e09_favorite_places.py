# 6-9 Favorite Places
favorite_places = {
    'seneca': ['corduba', 'rome', 'corsica'],
    'platon': ['athens', 'aegina', 'sicily'],
    'aristotle': ['stagira', 'chalcis', 'athens']
    }

for person, places in favorite_places.items():
    print(f"\nThis is the list of favorite places of {person.title()}:")
    for place in places:
        print(f"\t{place.title()}")
