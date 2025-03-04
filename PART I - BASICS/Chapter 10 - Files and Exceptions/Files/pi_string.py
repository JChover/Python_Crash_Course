# Working with a File’s Contents - pi_string.py
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() # strip instead of rstrip to remove spaces on the left also

print(pi_string)
print(len(pi_string))

# Large Files: One Million Digits - pi_string.py
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() # strip instead of rstrip to remove spaces on the left also

print(f"{pi_string[:52]}...") # To display only the first 50 decimals
print(len(pi_string))

# Is Your Birthday Contained in Pi? - pi_string.py
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form ddmmyyyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi!")