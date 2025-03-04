philosophers = ['socrates', 'seneca', 'zenon', 'platon', 'marco aurelio']  # This is my LIST

print(philosophers)  # Here I print my LIST

print(len(philosophers))  # Here I print the LENGTH of my LIST

print(philosophers[1])  # Here I print an ITEM from my LIST

print(philosophers[1].title())  # I can still use METHODS to LISTS

print(philosophers[-1].title())  # By pointing to the ITEM -1 it will always return the last ITEM from the LIST

print(f"Mr {philosophers[2].title()} is my favorite philosopher.")  # Use an ITEM from a LIST inside an f-string

philosophers[0] = 'descartes'  # Modify a specific ITEM from a LIST directly

philosophers.append('socrates')  # Add an ITEM to the end of a LIST with append() method

philosophers.insert(0,'kant')  # Add an ITEM at any given position of a LIST with insert() method

del philosophers[5]  # Remove an ITEM from a LIST with DEL statement

missing_philosopher1 = philosophers.pop()  # You can remove the LAST ITEM but still use it with the pop() method

missing_philosopher2 = philosophers.pop(3)  # You can remove an SPECIFIC ITEM but still use it with the pop() method

philosophers.remove('platon')  # Or directly remove an ITEM if its VALUE its known using the remove() method

philosophers.sort()  # This SORTS the ITEMS in the LIST in alphabetical order PERMANENTLY

sorted(philosophers)  # This SORTS the ITEMS in the LIST in alphabetical order TEMPORALLY

philosophers.reverse()  # This SORTS the ITEMS in the LIST in REVERSE alphabetical order PERMANENTLY





