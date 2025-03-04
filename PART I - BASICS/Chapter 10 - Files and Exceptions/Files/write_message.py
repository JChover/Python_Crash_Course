# Writing to an Empty File - write_message.py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# Writing Multiple Lines - write_message.py
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n") # Need to add \n so each line is inserted correctly.
    file_object.write("I love creating new games.\n")

# Appending to a File - write_message.py
filename = 'programming.txt'

with open(filename, 'a') as file_object: # We use 'a' mode to append.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
