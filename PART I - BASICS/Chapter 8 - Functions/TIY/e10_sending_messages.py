# 8-10 Sending Messages
def show_messages(messages):
    """
    Prints each message in the provided list of messages.

    Parameters:
    messages (list): A list of text messages to be printed.
    """
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """
    Prints each message and moves it to a new list called sent_messages.

    Parameters:
    messages (list): A list of text messages to be processed.
    sent_messages (list): A list where the printed messages will be moved.
    """
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)  # Append the current message to the sent_messages list


# Create a list containing a series of short text messages
messages = [
    "Hello, how are you?",
    "This is a test message.",
    "Have a great day!",
    "Keep coding!"
]

# Create an empty list to store the sent messages
sent_messages = []

# Pass the list to the send_messages() function
send_messages(messages, sent_messages)

# Print both lists to verify that the messages were moved correctly
print("\nOriginal messages list:", messages)
print("Sent messages list:", sent_messages)
