# 8-9 Messages
def show_messages(messages):
    """
    Prints each message in the provided list of messages.

    Parameters:
    messages (list): A list of text messages to be printed.
    """
    for message in messages:
        print(message)


# Create a list containing a series of short text messages
messages = [
    "Hello, how are you?",
    "This is a test message.",
    "Have a great day!",
    "Keep coding!"
]

# Pass the list to the show_messages() function
show_messages(messages)
