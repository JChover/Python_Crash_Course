# 6-4 Glossary 2
glossary = {
    'variable': 'An item where you can store a value all the times you want.',
    'list': 'A group of items, that can be modified.',
    'tuple': 'A group of items, that can not be modified.',
    'float': 'A type of variable used to store a floating point number.',
    'string': 'A type of variable used to store text.',
    'integer': 'An item where you can store a whole number.',
    'slice': 'The action of taking just a part of a list.',
    'dictionary': 'A collection of key-value pairs.',
    'set': 'The unique elements that dont repeat in a list of items.',
    'boolean': 'A type of variable used to store a state.'
    }

for key, value in glossary.items():
    print(f'{key.title()}: {value}\n')
