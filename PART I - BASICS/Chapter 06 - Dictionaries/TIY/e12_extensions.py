# 6-12 Extensions - from pizza_old.py
pizzas = {
    'prosciutto': {
        'toppings': ['tomato', 'mozzarella', 'ham', 'oregano'],
        'size': ['medium', 'large'],
        'prize': [9, 14]
    },

    'marinara': {
        'toppings': ['tomato', 'parsley', 'garlic'],
        'size': ['medium', 'large'],
        'prize': [8, 13]
    },
    'margarita': {
        'toppings': ['tomato', 'mozzarella', 'oregano'],
        'size': ['medium', 'large'],
        'prize': [7, 12]
    }
}

print(f"|--------------------PIZZA MENU--------------------|")

for pizza, pizza_info in pizzas.items():
    print(f"\n+ {pizza.upper()}")

    for topping in pizza_info['toppings']:
        print(f"\t- {topping.title()}")
    for size in pizza_info['size']:
        if size == 'medium':
            print(f"\t* Prize is ${pizza_info['prize'][0]} for a medium {pizza.title()}.")
        elif size == 'large':
            print(f"\t* Prize is ${pizza_info['prize'][1]} for a large {pizza.title()}.")
