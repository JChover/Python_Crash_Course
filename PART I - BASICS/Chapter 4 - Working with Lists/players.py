# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # This is called SLICING a LIST, prints only the first 3 ITEMS

print(players[1:4])  # You can start the SLICE at any position

print(players[:4])  # If omitted it will start from the position 0

print(players[2:])  # The same thing if we omit the end

print(players[-3:])  # By using negatives it starts from the end, in this case prints the last 3 items from the LIST

print(players[::2])  # You can use the 3d field to define a STEP

print(players[::-1])  # Step = -1 will return the list in inverse order

# Looping through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.capitalize())
