# 6-3 Glossary
glossary = {
    'variable': 'An item where you can store a value all the times you want.',
    'list': 'A group of items, that can be modified.',
    'tuple': 'A group of items, that can not be modified.',
    'float': 'A type of variable used to store a floating point number.',
    'string': 'A type of variable used to store text.'
    }

for key, value in glossary.items():
    print(f'{key.title()}: {value}\n')
