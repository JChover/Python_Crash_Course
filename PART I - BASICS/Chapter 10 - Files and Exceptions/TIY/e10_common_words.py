# 10-10 Common Words - e10_common_words.py
def count_word_the(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read() # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Count the approximate number of words in the file.
        the_words = contents.lower().count('the ')
        print(f"The file {filename} has about {the_words} 'the' words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_word_the(filename)
