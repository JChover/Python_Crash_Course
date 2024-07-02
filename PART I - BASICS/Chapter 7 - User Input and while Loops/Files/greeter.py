# Writing Clear Prompts - greeter.py
name = input("Please, enter your name: ")
print(f"\nHello, {name}!\n")

# Writing Clear Prompts(longer prompt) - greeter.py
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
