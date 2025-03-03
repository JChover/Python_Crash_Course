# Reading an Entire File - file_reader.py
with open('pi_digits.txt') as file_object:
    contents = file_object.read() # This leaves a blank space at the end.
    print(contents) # We can do contents.rstrip() to remove the blank space.

# Reading Line by Line - file_reader.py
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a List of Lines from a File - file_reader.py
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())