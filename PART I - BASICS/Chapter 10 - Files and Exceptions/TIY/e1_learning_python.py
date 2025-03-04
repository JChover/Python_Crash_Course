# 10-1 Learning Python - e1_learning_python.py
filename = 'e1_learning_python.txt'

# Reading the Entire File
with open(filename) as file_object:
    content = file_object.read()
    print(content)

# Reading by Looping the file_object
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Reading by storing in a List
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
