# 7-6 Three Exits
prompt = "\nTell me your age:"
prompt += "\n(Enter 'quit' to end the program.)\n "

active = True  # Active Variable to control the Loop(2)

while active:
    age = input(prompt)
    if age == 'quit':
        break  # Use of break to exit the loop(3)

    age = int(age)

    if age < 3:  # Conditional Test(1)
        price = 0
    elif 3 <= age <= 12:
        price = 10
    elif age > 12:
        price = 15

    print(f"Your ticket will cost ${price} ")
