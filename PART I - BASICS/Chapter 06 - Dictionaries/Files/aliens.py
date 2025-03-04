# A List of Dictionaries - aliens.py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# A List of Dictionaries - aliens.py
aliens = []  # Empty list of aliens

for alien_number in range(30):  # We will create 30 aliens
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print("The first 5 aliens are:")
for alien in aliens[:5]:  # This will show the first 5 created
    print(alien)

print(f"\nTotal number of aliens: {len(aliens)}")

# A List of Dictionaries - aliens.py
aliens = []  # Empty list of aliens

for alien_number in range(30):  # We will create 30 aliens
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:  # Modifying the 3 first aliens created
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'

print("The first 5 aliens are:")
for alien in aliens[:5]:  # This will show the first 5 created
    print(alien)

print(f"\nTotal number of aliens: {len(aliens)}")
