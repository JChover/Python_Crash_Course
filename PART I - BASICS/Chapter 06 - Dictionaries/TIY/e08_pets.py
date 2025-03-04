# 6-8 Pets
pet1 = {'kind': 'cat', 'medium': 'earth', 'size': 'normal', 'owner': 'seneca'}
pet2 = {'kind': 'dog', 'medium': 'earth', 'size': 'normal', 'owner': 'platon'}
pet3 = {'kind': 'turtle', 'medium': 'water', 'size': 'small', 'owner': 'aristotle'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\nThis is all I know about {pet['kind']}s:")
    print(f"\t - Medium: {pet['medium'].title()}")
    print(f"\t - Size: {pet['size'].title()}")
    print(f"\t - Owner: {pet['owner'].title()}")
