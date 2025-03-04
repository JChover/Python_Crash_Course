# Working with Multiple Files - word_count.py
def count_words(filename):
    """Count the approximate number of words in a file."""
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

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)

# Failing Silently - word_count.py
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read() # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
    except FileNotFoundError:
        pass # By using the pass statement we will not inform of the exception and just keep going
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
