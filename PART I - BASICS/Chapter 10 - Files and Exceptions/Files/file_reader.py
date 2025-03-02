# Reading an Entire File - file_reader.py
with open('pi_digits.txt') as file_object:
    contents = file_object.read() # This leaves a blank space at the end.
    print(contents) # We can do contents.rstrip() to remove the blank space.




