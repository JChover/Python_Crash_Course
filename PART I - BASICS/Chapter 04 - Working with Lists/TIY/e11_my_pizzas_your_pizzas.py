pizzas = ['prosciutto', 'marinara', 'margarita']

friend_pizzas = pizzas[:]

print(pizzas)
print(friend_pizzas)

pizzas.append('tuna')
friend_pizzas.append('salami')


print("\nMy favourite a pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print()

print("\nMy friend's favourite a pizzas are:")
for f_pizza in friend_pizzas:
    print(f_pizza.title())

print("\nWe really love pizzas, they are our favourite meal!")
