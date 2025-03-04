# 10-4 Guest Book - e4_guest_book.py
filename = 'e4_guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        name = input("What is your name?(q to quit): ")
        if name != 'q':
            file_object.write(f"{name}\n")
            print(f"Nice to meet you {name}!\n")
        else:
            print("Thank you!")
            break
