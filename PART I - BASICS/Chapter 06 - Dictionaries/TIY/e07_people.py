# 6-7 People
person1 = {
    'first_name': 'Lucio',
    'last_name': 'Seneca',
    'age': '69',
    'city': 'Cordoba'
}
person2 = {
    'first_name': 'Aristocles',
    'last_name': 'Platon',
    'age': '40',
    'city': 'Athens'
}
person3 = {
    'first_name': 'Aristotle',
    'last_name': 'The Stagirite',
    'age': '62',
    'city': 'Stagira'
}

people = [person1, person2, person3]

for person in people:
    print(f"His name was {person['first_name']}.")
    print(f"His last name was {person['last_name']}.")
    print(f"He died at the age of {person['age']}.")
    print(f"The city he was born was {person['city']}.\n")
