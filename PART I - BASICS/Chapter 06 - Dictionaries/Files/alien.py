# A Simple Dictionary - alien.py
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Accessing Values in a Dictionary - alien.py
alien_0 = {'color': 'green'}

print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!\n")

# Adding New Key-Value Pairs - alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0  # Dictionaries are Dynamic, so you can add key-value pairs
alien_0['y_position'] = 25
print(alien_0)

# Staring With an Empty Dictionary - alien.py
alien_0 = {}
print(alien_0)

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values in a Dictionary - alien.py
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.\n")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}  # Complex Example
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment  # Modifying Position
print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs - alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']  # Simply use DEL to remove the unwanted Key-value
print(alien_0)
