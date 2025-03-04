# 9-15 Lottery Analysis
from random import choice

# Define the pool of characters (numbers and letters)
lottery_pool = ['A', 'J', 'M', 'C', 'S', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Randomly select 4 characters from the pool
winning_numbers = [choice(lottery_pool) for _ in range(4)]
print(f'The winning ticket is: {winning_numbers}')

attempts = 0
while True:
    my_ticket = [choice(lottery_pool) for _ in range(4)]
    if winning_numbers == my_ticket:
        print(f"You won! It took {attempts} attempts to match the winning ticket.")
        break
    elif winning_numbers != my_ticket:
        attempts += 1
