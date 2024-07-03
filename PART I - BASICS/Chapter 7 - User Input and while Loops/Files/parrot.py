# How the input() Function Works - parrot.py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Letting the User Choose When to Quit - parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n(Enter 'quit' to end the program.)\n "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

# Using a Flag - parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\n(Enter 'quit' to end the program.)\n "

active = True  # The Flag

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
