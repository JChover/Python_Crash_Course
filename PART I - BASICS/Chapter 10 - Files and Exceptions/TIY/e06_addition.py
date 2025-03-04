# 10-06 Addition - e06_addition.py
print("Give me two numbers, and I'll ADD them(q to quit):")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You have to insert a number.!")
    else:
        print(f"Result: {answer}")
