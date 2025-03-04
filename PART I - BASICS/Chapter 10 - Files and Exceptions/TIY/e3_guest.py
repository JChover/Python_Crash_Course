# 10-3 Guest - e3_guest.py
filename = 'e3_guest.txt'

with open(filename, 'w') as file_object:
    name = input("What is your name?: ")
    file_object.write(name)
