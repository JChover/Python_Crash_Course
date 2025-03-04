# 10-5 Programming Poll - e05_programming_poll.py
filename = 'e05_programming_poll.txt'

with open(filename, 'a') as file_object:
    while True:
        response = input("Why do you like programming?(q to quit): ")
        if response != 'q':
            file_object.write(f"{response}\n")
        else:
            print("Thank you!")
            break
