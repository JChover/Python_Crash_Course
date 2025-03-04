# 7-8 Deli
sandwich_orders = ['turkey breast', 'carved turkey', 'roast beef', 'subway club', 'roasted chicken', 'veggie deleite']

finished_sandwiches = []

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    print(f"Your {sandwich_order.title()} sandwich is now ready.")
    finished_sandwiches.append(sandwich_order)

print()
for sandwich in finished_sandwiches:
    print(f"I prepared a {sandwich.title()} sandwich.")
