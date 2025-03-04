# 6-6 Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['john', 'sarah', 'steve', 'edward', 'mathew']

for name in people:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thanks for taking the poll.")
    if name not in favorite_languages.keys():
        print(f"{name.title()}, please take the poll.")
