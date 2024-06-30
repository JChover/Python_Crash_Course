# 6-10 Favorite Numbers
fav_numbers = {
    'seneca': ['10', '20', '30'],
    'platon': ['6', '12', '24'],
    'aristoteles': ['1', '2', '4'],
    'zenon': ['9', '18', '36'],
    'diogenes': ['3', '6', '12'],
}

for person, numbers in fav_numbers.items():
    print(f"\nThis is the list of favorite numbers of {person.title()}:")
    for number in numbers:
        print(f"\t{number}")
