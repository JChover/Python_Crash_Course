# 7-4 Pizza Toppings
prompt = "\nTell me a topping for your pizza:\n"
prompt += "\n(Enter 'quit' to end the program.)\n "

active = True  # The Flag

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Sure, I will add {topping} to your pizza.")
