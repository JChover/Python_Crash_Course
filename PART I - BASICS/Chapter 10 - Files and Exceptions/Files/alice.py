# Handling the FileNotFoundError Exception - alice.py
filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read() # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'

# Handling the FileNotFoundError Exception - alice.py
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read() # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

# Analyzing Text - alice.py
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read() # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
