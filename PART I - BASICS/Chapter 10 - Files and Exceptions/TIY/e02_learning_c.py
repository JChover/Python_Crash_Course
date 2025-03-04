# 10-2 Learning C - e02_learning_c.py
filename = 'e01_learning_python.txt'

with open(filename) as file_object:
    p_lines = file_object.readlines()

for line in p_lines:
    c_line = line.replace('Python','C')
    print(c_line.rstrip())
