# 7-5 Movie Tickets
prompt = "\nTell me your age:"
prompt += "\n(Enter 'quit' to end the program.)\n "

while True:
    age = input(prompt)
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    elif age > 12:
        price = 15

    print(f"Your ticket will cost ${price} ")
