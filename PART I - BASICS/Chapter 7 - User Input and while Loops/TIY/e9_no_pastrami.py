# 7-9 No Pastrami
sandwich_orders = ['pastrami', 'carved turkey', 'pastrami', 'subway club', 'pastrami', 'veggie deleite']

finished_sandwiches = []

print("Today we ran out of Pastrami!\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"Your {sandwich_order.title()} sandwich is now ready.")
    finished_sandwiches.append(sandwich_order)

print()
for sandwich in finished_sandwiches:
    print(f"I prepared a {sandwich.title()} sandwich.")
